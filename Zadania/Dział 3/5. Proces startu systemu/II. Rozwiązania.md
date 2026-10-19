![](../../../grafiki/3-5-rozwiazania.png)

# Rozwiązania – Proces startu systemu

> Zestawy odpowiadają kolejnym tematom modułu; numeracja zaczyna się od nowa w każdym z nich.

## GRUB i rozruch

### 1. Przejrzyj plik konfiguracyjny i sprawdź jakie ma opcje /etc/default/grub

```
Wyświetlenie pliku konfiguracyjnego GRUB:
cat /etc/default/grub

Główne opcje w /etc/default/grub:

GRUB_TIMEOUT=5
# Czas oczekiwania na wybór systemu (sekundy)

GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
# Nazwa dystrybucji wyświetlana w menu

GRUB_DEFAULT=saved
# Domyślny wpis do uruchomienia
# 0 = pierwszy wpis, saved = ostatnio wybrany

GRUB_DISABLE_SUBMENU=true
# Wyłącza podmenu (wszystkie kernele w głównym menu)

GRUB_TERMINAL_OUTPUT="console"
# Typ terminala wyjściowego

GRUB_CMDLINE_LINUX="crashkernel=auto rhgb quiet"
# Parametry kernela przekazywane podczas startu
# rhgb = Red Hat Graphical Boot
# quiet = ograniczone komunikaty podczas startu

GRUB_DISABLE_RECOVERY="true"
# Wyłącza opcje recovery mode

Edycja konfiguracji:
sudo nano /etc/default/grub

Po zmianach regeneruj konfigurację:
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

Dodatkowe opcje:
GRUB_TIMEOUT_STYLE=menu     # Styl wyświetlania timeout
GRUB_GFXMODE=auto          # Rozdzielczość graficzna
GRUB_DISABLE_OS_PROBER=true # Wyłącz szukanie innych OS
GRUB_SAVEDEFAULT=true      # Zapisuj ostatni wybór jako domyślny
```

---

### 2. Sprawdź pliki znajdujące się na partycji /boot, co tam możesz znaleźć?

```
Lista zawartości /boot:
ls -la /boot/

Główne pliki i katalogi w /boot:

grub2/
# Katalog z konfiguracją GRUB2
ls -la /boot/grub2/

vmlinuz-*
# Skompresowane obrazy kernela
ls -la /boot/vmlinuz-*

initramfs-*
# Initial RAM filesystem - sterowniki potrzebne do startu
ls -la /boot/initramfs-*

config-*
# Konfiguracja kompilacji kernela
ls -la /boot/config-*

System.map-*
# Mapowanie symboli kernela (debugowanie)
ls -la /boot/System.map-*

efi/ (jeśli system używa UEFI)
# Pliki UEFI
ls -la /boot/efi/

Szczegółowa analiza:
du -sh /boot/*                    # Rozmiary plików
file /boot/vmlinuz-*             # Typ plików kernela
file /boot/initramfs-*           # Typ plików initramfs

Sprawdzenie konfiguracji GRUB:
cat /boot/grub2/grub.cfg | head -20

Sprawdzenie systemu plików /boot:
df -h /boot
mount | grep boot
lsblk | grep boot

Weryfikacja integralności:
rpm -V kernel
rpm -qa | grep kernel
```

---

### 3. Użyj polecenia rpm, aby stworzyć listę wszystkich zainstalowanych kerneli w twoim systemie.

```
Lista zainstalowanych kerneli:
rpm -qa kernel*

Sortowanie według daty instalacji:
rpm -qa kernel* --last

Szczegółowe informacje o kernelach:
rpm -qi kernel
rpm -qa kernel* | xargs rpm -qi

Lista wszystkich pakietów związanych z kerelem:
rpm -qa | grep kernel

Sprawdzenie plików zainstalowanych przez kernel:
rpm -ql kernel-$(uname -r)

Weryfikacja pakietów kernel:
rpm -V kernel-$(uname -r)

Informacje o rozmiarze:
rpm -qa kernel* --queryformat '%{NAME}-%{VERSION}-%{RELEASE} %{SIZE}\n'

Historia instalacji kerneli:
rpm -qa kernel* --last | head -10

Sprawdzenie zależności kernela:
rpm -qR kernel-$(uname -r)

Alternative z dnf:
dnf list installed kernel*
dnf history | grep kernel

Sprawdzenie dostępnych kerneli:
dnf list available kernel*

Porównanie wersji:
rpm -qa kernel* | sort -V
```

---

### 4. Sprawdź wersję jądra, która jest aktualnie uruchomiona.

```
Podstawowe polecenie:
uname -r

Szczegółowe informacje o kernelu:
uname -a

Wersja kernela z dodatkowymi informacjami:
cat /proc/version

Informacje o kompilacji kernela:
uname -v

Architektura systemu:
uname -m

Nazwa systemu:
uname -s

Wszystkie informacje systemowe:
hostnamectl

Sprawdzenie w /proc:
cat /proc/sys/kernel/osrelease
cat /proc/sys/kernel/version

Porównanie z zainstalowanymi:
echo "Uruchomiony: $(uname -r)"
echo "Zainstalowane:"
rpm -qa kernel* | sort

Sprawdzenie czy to najnowszy kernel:
latest_kernel=$(rpm -qa kernel --last | head -1 | cut -d' ' -f1)
current_kernel="kernel-$(uname -r)"
echo "Najnowszy: $latest_kernel"
echo "Aktualny: $current_kernel"

Informacje z dmesg:
dmesg | grep -i "Linux version"

Sprawdzenie uptime:
uptime
cat /proc/uptime
```

---

### 5. Sprawdź listę aktualnie załadowanych modułów.

```
Lista wszystkich załadowanych modułów:
lsmod

Sortowanie według nazwy:
lsmod | sort

Liczba załadowanych modułów:
lsmod | wc -l

Szczegółowe informacje o module:
modinfo nazwa_modulu

Przykład szczegółowych informacji:
modinfo e1000e    # Sterownik karty sieciowej
modinfo ext4      # System plików

Sprawdzenie czy moduł jest załadowany:
lsmod | grep nazwa_modulu

Informacje o module z /proc:
cat /proc/modules

Sprawdzenie zależności modułów:
modprobe --show-depends nazwa_modulu

Drzewo zależności:
modprobe --show-depends e1000e

Ładowanie/usuwanie modułów:
sudo modprobe nazwa_modulu      # Załaduj
sudo modprobe -r nazwa_modulu   # Usuń

Sprawdzenie dostępnych modułów:
find /lib/modules/$(uname -r) -name "*.ko" | wc -l

Moduły kernela według kategorii:
ls /lib/modules/$(uname -r)/kernel/

Sprawdzenie blacklisted modułów:
cat /etc/modprobe.d/blacklist.conf

Moduły załadowane podczas startu:
dmesg | grep -i "module"

Statystyki modułów:
cat /proc/modules | awk '{print $1, $2}' | sort -k2 -nr

Sprawdzenie parametrów modułu:
cat /sys/module/nazwa_modulu/parameters/*

Historia ładowania modułów:
journalctl -k | grep -i module
```

---

### Dodatkowe informacje o GRUB i boot

```
Zarządzanie GRUB:

Sprawdzenie wersji GRUB:
grub2-install --version

Regeneracja konfiguracji:
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

Ustawienie domyślnego wpisu:
sudo grub2-set-default 0

Sprawdzenie domyślnego wpisu:
grub2-editenv list

UEFI vs BIOS:
# UEFI:
ls /sys/firmware/efi
efibootmgr -v

# BIOS:
sudo grub2-install /dev/sda

Bootloader rescue:
# Jeśli system nie startuje:
# 1. Boot z LiveCD/USB
# 2. Mount partycji root
# 3. chroot do systemu
# 4. Regeneruj GRUB

Sprawdzenie czasu startu:
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain

Informacje o initramfs:
lsinitrd /boot/initramfs-$(uname -r).img | head -20

Regeneracja initramfs:
sudo dracut --force --verbose

Diagnostyka startu:
journalctl -b    # Logi z ostatniego startu
dmesg           # Komunikaty kernela
```

## Demony i systemctl

### 1. Wyświetl wszystkie serwisy w systemie i ich aktualny stan oraz lokalizację

```
Lista wszystkich serwisów z statusem:
systemctl list-units --type=service --all

Tylko aktywne serwisy:
systemctl list-units --type=service --state=active

Lista wszystkich plików unit (włącznie z lokalizacją):
systemctl list-unit-files --type=service

Szczegółowe informacje z lokalizacją:
systemctl list-unit-files --type=service | head -20

Sprawdzenie lokalizacji konkretnego serwisu:
systemctl show nginx -p FragmentPath
systemctl cat nginx

Wszystkie serwisy z pełnymi informacjami:
systemctl list-units --type=service --all --no-pager

Status konkretnego serwisu:
systemctl status nazwa_serwisu
systemctl show nazwa_serwisu

Serwisy w różnych stanach:
systemctl list-units --type=service --state=failed    # Nieudane
systemctl list-units --type=service --state=running   # Uruchomione
systemctl list-units --type=service --state=inactive  # Nieaktywne

Lokalizacje plików systemd:
/usr/lib/systemd/system/    # Domyślne pliki unit
/etc/systemd/system/        # Lokalne/custom pliki unit
/run/systemd/system/        # Tymczasowe pliki unit

Sprawdzenie ścieżek systemd:
systemd-analyze unit-paths
```

---

### 2. Zainstaluj silnik stron internetowych nginx i uruchom jego deamona

```
Instalacja nginx:
sudo dnf install nginx                    # RHEL/CentOS/Fedora
sudo apt install nginx                   # Debian/Ubuntu
sudo yum install nginx                   # Starsze RHEL/CentOS

Uruchomienie serwisu nginx:
sudo systemctl start nginx

Weryfikacja instalacji:
which nginx
nginx -v
rpm -qi nginx                           # RHEL/CentOS
dpkg -l nginx                          # Debian/Ubuntu

Sprawdzenie konfiguracji nginx:
sudo nginx -t                          # Test konfiguracji
sudo nginx -T                          # Pokaż pełną konfigurację

Sprawdzenie plików nginx:
ls -la /etc/nginx/
ls -la /var/log/nginx/
ls -la /usr/share/nginx/

Lokalizacja głównego pliku konfiguracyjnego:
cat /etc/nginx/nginx.conf

Sprawdzenie procesów nginx:
ps aux | grep nginx
pgrep nginx

Sprawdzenie portów nginx:
ss -tlnp | grep nginx
netstat -tlnp | grep nginx
lsof -i :80

Test działania:
curl localhost
curl -I localhost                      # Tylko headers
```

---

### 3. Sprawdź czy serwis nginx'a jest uruchomiony

```
Sprawdzenie statusu nginx:
systemctl status nginx

Krótkie sprawdzenie czy jest aktywny:
systemctl is-active nginx

Sprawdzenie czy jest włączony (autostart):
systemctl is-enabled nginx

Sprawdzenie czy działa:
systemctl is-running nginx

Szczegółowe informacje:
systemctl show nginx
systemctl show nginx -p ActiveState -p SubState

Sprawdzenie procesów:
ps aux | grep nginx
pgrep -l nginx

Sprawdzenie czy nasłuchuje na porcie:
ss -tlnp | grep :80
netstat -tlnp | grep :80

Test połączenia:
curl -s -o /dev/null -w "%{http_code}" localhost
wget --spider -q localhost && echo "OK" || echo "FAILED"

Sprawdzenie logów:
journalctl -u nginx --no-pager
tail /var/log/nginx/access.log
tail /var/log/nginx/error.log

Monitoring w czasie rzeczywistym:
journalctl -u nginx -f
systemctl status nginx -l
```

---

### 4. Zastopuj działanie serwisu nginx

```
Zatrzymanie serwisu nginx:
sudo systemctl stop nginx

Weryfikacja zatrzymania:
systemctl status nginx
systemctl is-active nginx

Sprawdzenie czy procesy zostały zatrzymane:
ps aux | grep nginx
pgrep nginx

Sprawdzenie czy porty są zwolnione:
ss -tlnp | grep :80
netstat -tlnp | grep :80

Test czy serwis nie odpowiada:
curl localhost
# Powinno pokazać błąd połączenia

Alternative metody zatrzymania:
sudo nginx -s stop                     # Natychmiastowe zatrzymanie
sudo nginx -s quit                     # Graceful shutdown
sudo nginx -s reload                   # Przeładowanie konfiguracji

Sprawdzenie w logach:
journalctl -u nginx --since "1 minute ago"
tail /var/log/nginx/error.log

Wymuszenie zatrzymania (jeśli normalne nie działa):
sudo systemctl kill nginx
sudo pkill nginx
```

---

### 5. Ponownie sprawdź czy serwis nginx'a jest uruchomiony

```
Sprawdzenie statusu po zatrzymaniu:
systemctl status nginx

Status powinien pokazać:
Active: inactive (dead)

Krótkie sprawdzenie:
systemctl is-active nginx
# Powinno zwrócić: inactive

Sprawdzenie procesów:
ps aux | grep nginx
pgrep nginx
# Nie powinno pokazać procesów nginx

Sprawdzenie portów:
ss -tlnp | grep :80
netstat -tlnp | grep :80
# Port 80 nie powinien być zajęty przez nginx

Test połączenia:
curl localhost
# Powinno pokazać błąd: Connection refused

Sprawdzenie w różny sposób:
systemctl is-running nginx             # inactive
systemctl show nginx -p ActiveState   # ActiveState=inactive

Logi zatrzymania:
journalctl -u nginx --since "2 minutes ago"
```

---

### 6. Uruchom serwis nginx'a i sprawdź czy działa

```
Uruchomienie nginx:
sudo systemctl start nginx

Sprawdzenie czy się uruchomił:
systemctl status nginx
systemctl is-active nginx              # Powinno zwrócić: active

Sprawdzenie procesów:
ps aux | grep nginx
pgrep -l nginx

Sprawdzenie portów:
ss -tlnp | grep :80
ss -tlnp | grep nginx

Test funkcjonalności:
curl localhost
curl -I localhost

Sprawdzenie w przeglądarce:
# Otwórz http://localhost lub http://IP_SERWERA

Sprawdzenie konfiguracji:
sudo nginx -t

Logi uruchomienia:
journalctl -u nginx --since "1 minute ago"
tail /var/log/nginx/access.log

Sprawdzenie wszystkich informacji:
systemctl show nginx -p ActiveState -p SubState -p Result

Test zaawansowany:
curl -s -o /dev/null -w "HTTP Code: %{http_code}\nTime: %{time_total}s\n" localhost
```

---

### 7. Włącz autostart serwisu nginx w trakcie startu systemu

```
Włączenie autostartu nginx:
sudo systemctl enable nginx

Sprawdzenie czy autostart jest włączony:
systemctl is-enabled nginx             # Powinno zwrócić: enabled

Lista wszystkich serwisów z autostartem:
systemctl list-unit-files --type=service --state=enabled

Sprawdzenie konkretnie nginx:
systemctl list-unit-files | grep nginx

Sprawdzenie symlinków (utworzonych przez enable):
ls -la /etc/systemd/system/multi-user.target.wants/ | grep nginx

Informacje o targecie:
systemctl list-dependencies nginx
systemctl show nginx -p WantedBy

Test autostartu (symulacja):
systemctl is-enabled nginx && echo "Uruchomi się automatycznie"

Sprawdzenie wszystkich enabled serwisów:
systemctl list-unit-files --state=enabled --no-pager

Wyłączenie autostartu (gdyby było potrzebne):
sudo systemctl disable nginx

Sprawdzenie dependency:
systemctl list-dependencies multi-user.target | grep nginx

Weryfikacja konfiguracji systemd:
systemctl daemon-reload                # Po zmianach w plikach unit
```

---

### 8. Sprawdź czy serwis firewalld jest włączony. Jeżeli tak to wyłącz i z poziomu przeglądarki wejdź na adres IP swojego serwera.

```
Sprawdzenie statusu firewalld:
systemctl status firewalld
systemctl is-active firewalld
systemctl is-enabled firewalld

Sprawdzenie konfiguracji firewall:
sudo firewall-cmd --state
sudo firewall-cmd --list-all

Sprawdzenie aktualnych reguł:
sudo firewall-cmd --list-services
sudo firewall-cmd --list-ports

Zatrzymanie firewalld:
sudo systemctl stop firewalld

Wyłączenie autostartu firewalld:
sudo systemctl disable firewalld

Weryfikacja wyłączenia:
systemctl status firewalld
systemctl is-active firewalld          # inactive
systemctl is-enabled firewalld         # disabled

Sprawdzenie czy porty są otwarte:
ss -tlnp | grep :80
nmap localhost -p 80

Sprawdzenie IP serwera:
ip addr show
hostname -I
curl ifconfig.me                       # Publiczne IP (jeśli dostępne)

Test z przeglądarki:
# Otwórz w przeglądarce:
# http://ADRES_IP_SERWERA
# http://localhost (jeśli lokalnie)

Test z curl:
curl http://ADRES_IP_SERWERA
curl -I http://ADRES_IP_SERWERA

Alternative - otwarcie portu zamiast wyłączania firewall:
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-all

Sprawdzenie iptables (low-level):
sudo iptables -L
sudo iptables -t nat -L

Przywrócenie firewall (po testach):
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

---

### Dodatkowe polecenia systemctl

```
Podstawowe operacje:
sudo systemctl start serwis            # Uruchom
sudo systemctl stop serwis             # Zatrzymaj
sudo systemctl restart serwis          # Restartuj
sudo systemctl reload serwis           # Przeładuj konfigurację
sudo systemctl enable serwis           # Włącz autostart
sudo systemctl disable serwis          # Wyłącz autostart

Informacje o serwisach:
systemctl status serwis                # Status
systemctl show serwis                  # Szczegóły
systemctl cat serwis                   # Pokaż plik unit
systemctl list-dependencies serwis     # Zależności

Zarządzanie systemem:
sudo systemctl daemon-reload           # Przeładuj konfigurację systemd
sudo systemctl reset-failed           # Resetuj failed units
systemctl list-units --failed         # Pokaż nieudane units

Cele systemowe (targets):
systemctl list-units --type=target     # Lista targets
systemctl get-default                  # Domyślny target
sudo systemctl set-default multi-user.target  # Ustaw domyślny

Logi i diagnostyka:
journalctl -u serwis                   # Logi serwisu
journalctl -u serwis -f               # Follow logs
journalctl -u serwis --since today    # Logi z dzisiaj
systemctl list-units --state=failed   # Serwisy z błędami

Tworzenie własnych serwisów:
# Przykład pliku /etc/systemd/system/moj-serwis.service
[Unit]
Description=Mój Custom Serwis
After=network.target

[Service]
Type=simple
ExecStart=/path/to/program
Restart=always
User=myuser

[Install]
WantedBy=multi-user.target
```
