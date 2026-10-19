![](../../../grafiki/3-4-rozwiazania.png)

# Rozwiązania – Konfiguracja sieci

> **1. Przegląd interfejsów:**

```bash
ip -br a
```

Przykładowo: interfejs `ens192`, stan `UP`, adres `192.168.10.20/24`. (`lo` to pętla zwrotna.)

**2. Adres sieci i część hosta:**

Dla `192.168.10.20/24` adres sieci to `192.168.10.0/24` (pierwsze trzy liczby – „ulica”), a `20` to część hosta („numer domu”). Przy masce /24 dostępne są adresy .1–.254, czyli 254 maszyny.

**3. Brama domyślna:**

```bash
ip route
```

Wiersz `default via 192.168.10.1 ...` wskazuje bramę. Brama to router, któremu maszyna oddaje cały ruch kierowany poza sieć lokalną (np. do internetu).

**4. Adres MAC:**

```bash
ip link show ens192     # pole link/ether
ip -br link             # kolumna z adresem MAC
```

**5. Tablica sąsiadów:**

```bash
ip neigh
```

Wpis (np. `192.168.10.1 ... lladdr 70:4f:57:12:ab:cd REACHABLE`) oznacza, że system ustalił, jaki fizyczny adres karty (MAC) odpowiada danemu adresowi IP w sieci lokalnej – bez tego nie wysłałby do niego ramki.

**6. Adres tymczasowy:**

```bash
sudo ip addr add 192.168.77.5/24 dev ens192
ip -br a
sudo ip addr del 192.168.77.5/24 dev ens192
```

Polecenie `ip` zmienia tylko bieżący stan jądra; przy starcie systemu konfigurację ustawia NetworkManager z profili – tymczasowy adres nie jest w żadnym profilu, więc znika.

**7. ifconfig i następcy:**

```bash
ifconfig          # bash: ifconfig: command not found
sudo dnf whatprovides ifconfig   # pakiet net-tools
```

Odpowiedniki: `ifconfig -a` → `ip a`, `route -n` → `ip route`, `netstat -tulpn` → `ss -tulpn`.

**8. Urządzenia i profile:**

```bash
nmcli device status
nmcli connection show
```

Urządzenie to fizyczny interfejs (np. `ens192`); połączenie to zapisany profil ustawień (adres, brama, DNS), który można przypisać do urządzenia – jedno urządzenie może mieć kilka profili.

**9. Metoda IPv4 profilu:**

```bash
nmcli connection show ens192 | grep ipv4.method
```

`auto` = DHCP, `manual` = adres statyczny.

**10. Konfiguracja statyczna i powrót:**

```bash
# odczyt obecnych wartości
ip -br a; ip route
# ustawienie (przykładowe wartości – podstaw własne)
sudo nmcli connection modify ens192 ipv4.method manual \
ipv4.addresses 192.168.10.20/24 ipv4.gateway 192.168.10.1 \
ipv4.dns "192.168.10.1 8.8.8.8"
sudo nmcli connection up ens192
ip -br a; cat /etc/resolv.conf
# powrót do DHCP
sudo nmcli connection modify ens192 ipv4.method auto \
ipv4.addresses "" ipv4.gateway "" ipv4.dns ""
sudo nmcli connection up ens192
```

Pamiętaj o dwóch krokach: `modify` zapisuje, dopiero `up` stosuje.

**11. Plik profilu:**

```bash
sudo cat /etc/NetworkManager/system-connections/ens192.nmconnection
ls -l /etc/NetworkManager/system-connections/
```

Serwery DNS są w sekcji `[ipv4]`, klucz `dns=192.168.10.1;8.8.8.8;`. Plik ma uprawnienia `600` (tylko root), bo profile mogą zawierać hasła (np. do sieci Wi-Fi).

**12. resolv.conf i ręczna edycja profili:**

`/etc/resolv.conf` jest generowany przez NetworkManager – ręczne zmiany zostaną nadpisane przy najbliższym podniesieniu połączenia. Poprawnie: `sudo nmcli con mod ens192 ipv4.dns "…"` + `sudo nmcli con up ens192`. Po ręcznej edycji pliku `.nmconnection`:

```bash
sudo nmcli connection reload
sudo nmcli connection up ens192
```

**13. Wpis w /etc/hosts:**

```bash
echo "127.0.0.1 mojserwer" | sudo tee -a /etc/hosts
ping -c 2 mojserwer
sudo sed -i '/mojserwer/d' /etc/hosts
```

Działa, bo system (zgodnie z `/etc/nsswitch.conf`) sprawdza plik `/etc/hosts` **przed** zapytaniem DNS.

**14. Nazwa komputera:**

```bash
hostnamectl                                  # odczyt (zanotuj starą nazwę)
sudo hostnamectl set-hostname stacja1.szkolenie.local
hostnamectl
sudo hostnamectl set-hostname stara-nazwa    # przywrócenie
```

**15. Diagnostyka od dołu do góry:**

```bash
ip -br a                 # 1. brak adresu/DOWN = problem lokalny (kabel, interfejs, DHCP)
ping -c 3 192.168.10.1   # 2. brak odpowiedzi = sieć lokalna (switch, maska, brama)
ping -c 3 8.8.8.8        # 3. brak = zła trasa domyślna albo łącze dostawcy
ping -c 3 onet.pl        # 4. brak (a krok 3 działa) = DNS
curl -I https://onet.pl  # 5. brak (a krok 4 działa) = konkretna usługa, nie sieć
```

**16. Adres domeny czterema sposobami:**

```bash
dig www.example.com
nslookup www.example.com
host www.example.com
dig @8.8.8.8 www.example.com
```

W wyjściu `dig` serwer, który odpowiedział, widać w stopce: `;; SERVER: 8.8.8.8#53(8.8.8.8)`.

**17. Porty nasłuchujące:**

```bash
sudo ss -tulpn
nc -zv localhost 22
```

Na porcie 22 nasłuchuje `sshd`. `sudo` jest potrzebne, by `ss` pokazał nazwy procesów; `nc -zv` potwierdza: `Connected to localhost:22`.

**18. Skan własnej maszyny:**

```bash
nmap localhost
```

Lista `open` powinna pokrywać się z portami z `ss -tulpn` (dla adresów dostępnych z zewnątrz; usługi na `127.0.0.1` widać tylko przy skanie localhost). Cudzych adresów nie skanujemy, bo skan portów bez zgody właściciela jest traktowany jak rekonesans przed atakiem – może naruszać prawo i regulaminy sieci.
