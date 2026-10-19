![](../../../grafiki/4-06-rozwiazania.png)

# Rozwiązania – Lynis

**1.** Instalacja z EPEL:
```bash
sudo dnf install epel-release
sudo dnf install lynis
lynis show version
```

---

**2.** Pełny audyt:
```bash
sudo lynis audit system
``` Liczby warnings/suggestions i hardening index stoją w sekcji `-[ Lynis results ]-` na końcu wyniku.

---

**3.** Wynik z pliku raportu:
```bash
sudo grep hardening_index /var/log/lynis-report.dat
``` Plik `lynis-report.dat` przechowuje dane audytu jako `klucz=wartość`.

---

**4.** Szczegóły testu SSH:
```bash
sudo lynis show details SSH-7408
``` Zwykle proponuje m.in. `PermitRootLogin no`, `MaxAuthTries 3`, `AllowTcpForwarding no`, `X11Forwarding no` – każda pozycja z aktualną i zalecaną wartością.

---

**5.** Starzenie haseł:
```bash
sudo vi /etc/login.defs
# PASS_MAX_DAYS 180 / PASS_MIN_DAYS 1 / PASS_WARN_AGE 7
sudo chage -M 180 -m 1 -W 7 anna
sudo chage -l anna
``` `login.defs` działa tylko dla nowych kont, dlatego istniejące poprawiamy `chage`.

---

**6.** Jakość haseł:
```bash
sudo vi /etc/security/pwquality.conf
# minlen = 12
# minclass = 3
passwd    # próba ustawienia hasła "kot" kończy się odmową (BAD PASSWORD)
``` Uwaga: root może wymusić słabe hasło mimo ostrzeżenia – test rób jako zwykły użytkownik.

---

**7.** Banery:
```bash
echo "Dostep wylacznie dla uprawnionych uzytkownikow. Aktywnosc jest rejestrowana." | sudo tee /etc/issue /etc/issue.net
sudo lynis audit system --quick   # testy BANN-7126/BANN-7130 znikają z sugestii
``` Baner w SSH wymaga jeszcze `Banner /etc/issue.net` w konfiguracji sshd.

---

**8.** Audyt zdarzeń:
```bash
sudo dnf install audit
sudo systemctl enable --now auditd
systemctl status auditd
sudo tail -n 3 /var/log/audit/audit.log
```

---

**9.** Utwardzenie SSH:
```bash
sudo tee /etc/ssh/sshd_config.d/90-hardening.conf <<'EOF'
PermitRootLogin no
MaxAuthTries 3
EOF
sudo sshd -t && sudo systemctl restart sshd
# w DRUGIM oknie: ssh anna@serwer – musi działać, zanim zamkniesz obecną sesję
``` `sshd -t` sprawdza składnię; restart wykonuj dopiero po `echo $?` równym 0.

---

**10.** Audyt kontrolny:
```bash
sudo lynis audit system --quick
sudo grep hardening_index /var/log/lynis-report.dat
``` Po zadaniach 5–9 hardening index zwykle rośnie o kilka–kilkanaście punktów; dokładna wartość zależy od stanu początkowego maszyny.

---

**11.** Lynis z GitHuba:
```bash
sudo dnf install git
sudo git clone https://github.com/CISOfy/lynis /usr/local/lynis
cd /usr/local/lynis
sudo ./lynis audit system --quick
./lynis show version
lynis show version
``` Kopia z GitHuba to zawsze bieżące wydanie; pakiet z EPEL bywa starszy. Uruchamiana z katalogu (`./lynis`) nie koliduje z wersją z pakietu.
