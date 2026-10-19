![](../../../grafiki/2-04-rozwiazania.png)

# Rozwiązania – Zdalna administracja

> **1. Stan serwera SSH:**

```bash
systemctl status sshd
systemctl is-enabled sshd
```

Usługa nazywa się `sshd`; `active (running)` oznacza, że działa, a `enabled` – że wstanie po restarcie.

**2. Pierwsze połączenie:**

```bash
ssh anna@localhost
```

Na pytanie „Are you sure you want to continue connecting?” odpowiadamy całym słowem `yes` – odcisk klucza serwera zostanie zapamiętany. Po zalogowaniu `hostname` i `whoami`, wylogowanie: `exit`.

**3. Plik known_hosts:**

```bash
cat ~/.ssh/known_hosts
```

Plik przechowuje odciski kluczy serwerów, z którymi już się łączyliśmy; chroni przed podstawieniem innego (fałszywego) serwera pod znany adres – przy zmianie klucza klient przerwie połączenie.

**4. Usunięcie odcisku:**

```bash
ssh-keygen -R localhost
ssh anna@localhost
```

Po usunięciu wpisu klient znowu pyta o potwierdzenie odcisku, jak przy pierwszym połączeniu.

**5. Pojedyncze zdalne polecenie:**

```bash
ssh anna@localhost 'df -h /'
```

Polecenie wykonuje się na serwerze, wynik wraca do lokalnego terminala, sesja kończy się sama.

**6. Plik config:**

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
cat >> ~/.ssh/config <<'EOF'
Host ja
HostName localhost
User anna
EOF
chmod 600 ~/.ssh/config
ssh ja
```

Bez uprawnień `600` klient odmówi użycia pliku (`Bad owner or permissions`).

**7. Tryb diagnostyczny:**

```bash
ssh -v ja
```

W wyjściu szukamy: `Reading configuration data /home/anna/.ssh/config` (plik konfiguracyjny), `Connecting to localhost ... port 22` (port), `Authentications that can continue: publickey,password` (metody uwierzytelnienia).

**8. Generowanie pary kluczy:**

```bash
ssh-keygen -t ed25519 -C "anna"
ls -l ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub
```

Koledze wolno wysłać tylko `id_ed25519.pub` (klucz publiczny – „kłódkę”); klucz prywatny `id_ed25519` nigdy nie opuszcza naszego komputera.

**9. Wgranie klucza:**

```bash
ssh-copy-id anna@localhost
ssh anna@localhost          # loguje bez hasła konta
ls -ld ~/.ssh               # drwx------ (700)
ls -l ~/.ssh/authorized_keys  # -rw------- (600)
cat ~/.ssh/authorized_keys
```

`ssh-copy-id` dopisał klucz publiczny do `authorized_keys` i ustawił wymagane uprawnienia.

**10. Psucie uprawnień:**

```bash
chmod 644 ~/.ssh/authorized_keys
chmod 755 ~/.ssh
ssh anna@localhost
# przywrócenie:
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Przy `644`/`755` (brak zapisu dla grupy i innych) logowanie kluczem zwykle nadal działa – `StrictModes` odrzuca dopiero pliki i katalogi **zapisywalne** dla grupy lub innych (np. `775` na katalogu domowym albo `.ssh`; wtedy w dzienniku `journalctl -u sshd` pojawia się `Authentication refused: bad ownership or modes`). Dobre praktyki to mimo wszystko `700`/`600`.

**11. Plik konfiguracyjny serwera:**

```bash
sudo tee /etc/ssh/sshd_config.d/00-szkolenie.conf <<'EOF'
PermitRootLogin no
MaxAuthTries 3
AllowUsers anna
EOF
sudo sshd -t
sudo systemctl reload sshd
```

`sshd -t` bez komunikatu = składnia poprawna; `reload` nie zrywa istniejących sesji. Test w drugim oknie: `ssh anna@localhost`.

**12. Efektywna konfiguracja:**

```bash
sudo sshd -T | grep -Ei 'permitrootlogin|maxauthtries'
```

`sshd -T` wypisuje wartości po złożeniu wszystkich plików konfiguracji – to, co naprawdę obowiązuje.

**13. Baner:**

```bash
echo "System szkoleniowy. Dostep tylko dla upowaznionych." | sudo tee /etc/issue.net
echo "Banner /etc/issue.net" | sudo tee -a /etc/ssh/sshd_config.d/00-szkolenie.conf
sudo sshd -t && sudo systemctl reload sshd
ssh anna@localhost
```

Tekst baneru pojawia się przed pytaniem o hasło/klucz.

**14. Zmiana portu na 2222 i powrót:**

```bash
# 1. zapora
sudo firewall-cmd --permanent --add-port=2222/tcp && sudo firewall-cmd --reload
# 2. SELinux (pakiet policycoreutils-python-utils)
sudo semanage port -a -t ssh_port_t -p tcp 2222
# 3. konfiguracja
echo "Port 2222" | sudo tee -a /etc/ssh/sshd_config.d/00-szkolenie.conf
sudo sshd -t && sudo systemctl reload sshd
ssh -p 2222 anna@localhost

# powrót do portu 22:
sudo sed -i '/^Port 2222/d' /etc/ssh/sshd_config.d/00-szkolenie.conf
sudo sshd -t && sudo systemctl reload sshd
sudo semanage port -d -t ssh_port_t -p tcp 2222
sudo firewall-cmd --permanent --remove-port=2222/tcp && sudo firewall-cmd --reload
ssh anna@localhost
```

Kolejność przy zmianie: zapora → SELinux → konfiguracja; przy sprzątaniu odwrotnie.

**15. scp i rsync:**

```bash
mkdir -p ~/cwiczenia-scp
echo a > ~/cwiczenia-scp/a.txt; echo b > ~/cwiczenia-scp/b.txt; echo c > ~/cwiczenia-scp/c.txt
scp ~/cwiczenia-scp/a.txt anna@localhost:/tmp/
scp -r ~/cwiczenia-scp anna@localhost:/tmp/
rsync -avz ~/cwiczenia-scp/ anna@localhost:kopia/
rsync -avz ~/cwiczenia-scp/ anna@localhost:kopia/
```

Drugi `rsync` nie przesłał plików, bo porównuje obie strony i kopiuje tylko różnice – a nic się nie zmieniło.

**16. Sesja sftp:**

```bash
sftp anna@localhost
```

```text
sftp> pwd
sftp> lpwd
sftp> get kopia/a.txt
sftp> put cwiczenia-scp/b.txt
sftp> bye
```

Polecenia z przedrostkiem `l` dotyczą strony lokalnej, bez – zdalnej; `get` pobiera, `put` wysyła.

**17. Lustro z --delete:**

```bash
echo "zmiana" >> ~/cwiczenia-scp/a.txt
rm ~/cwiczenia-scp/c.txt
rsync -avz --delete -n ~/cwiczenia-scp/ anna@localhost:kopia/   # próba na sucho
rsync -avz --delete ~/cwiczenia-scp/ anna@localhost:kopia/
```

Z `-n` rsync tylko wypisuje plan (w tym `deleting c.txt`); bez `-n` wykonuje go naprawdę – kopia staje się wiernym lustrem źródła.

**18. (Dla chętnych) RDP, VNC i tunel:**

xrdp wybierzemy, gdy z Windows potrzebujemy pełnego pulpitu graficznego serwera („Podłączanie pulpitu zdalnego”, każdy dostaje własną sesję, ruch szyfrowany). VNC – gdy klient to Linux/macOS albo narzędzia firmowe używają VNC. Portu 5901 nie wystawiamy, bo VNC sam w sobie nie szyfruje ruchu ani hasła. Tunel:

```bash
ssh -L 5901:localhost:5901 anna@serwer
```

Następnie klienta VNC kierujemy na `localhost:5901` – ruch idzie wewnątrz szyfrowanego SSH.
