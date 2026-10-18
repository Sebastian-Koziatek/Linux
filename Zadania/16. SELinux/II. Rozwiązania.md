# Rozwiązania – SELinux

## 1. Tryb pracy

```bash
getenforce
sestatus
```

`getenforce` zwraca jedno słowo (`Enforcing`), `sestatus` — pełne podsumowanie, w tym `Loaded policy name: targeted`.

## 2. Konteksty

```bash
id -Z
ls -Zd /var/www/html
ls -Z /etc/passwd
```

Typ to przedostatnie pole kontekstu, zakończone `_t`: odpowiednio `unconfined_t` (powłoka użytkownika), `httpd_sys_content_t` (treści WWW), `passwd_file_t`.

## 3. Permissive i z powrotem

```bash
sudo setenforce 0
getenforce          # Permissive
sudo setenforce 1
getenforce          # Enforcing
```

`setenforce` zmienia tryb tylko w działającym jądrze; na stałe decyduje wiersz `SELINUX=` w `/etc/selinux/config`, czytany przy starcie systemu.

## 4. Plik przeniesiony przez mv

```bash
sudo dnf install httpd
sudo systemctl enable --now httpd
echo "test" > ~/index.html
sudo mv ~/index.html /var/www/html/
ls -Z /var/www/html/index.html    # typ: user_home_t
curl -s -o /dev/null -w "%{http_code}\n" http://localhost/index.html   # 403
```

`mv` zachowuje etykietę pliku z miejsca pochodzenia (`user_home_t`), a polityka nie pozwala procesowi `httpd_t` czytać plików tego typu — DAC przepuszcza, MAC blokuje.

## 5. Naprawa etykiety

```bash
sudo restorecon -v /var/www/html/index.html
ls -Z /var/www/html/index.html    # typ: httpd_sys_content_t
curl http://localhost/index.html
```

`restorecon` nakłada etykietę wynikającą z reguł polityki dla tej ścieżki — dla `/var/www/html` jest to `httpd_sys_content_t`.

## 6. Odczyt odmowy AVC

```bash
sudo ausearch -m AVC -ts recent
```

W znalezionym wpisie: `scontext=...httpd_t...` (typ procesu), `tcontext=...user_home_t...` (typ pliku), `avc: denied { read }` (odmówiona operacja odczytu), `comm="httpd"` (nazwa procesu).

## 7. Strona w /srv/strona

```bash
sudo mkdir -p /srv/strona
echo "strona" | sudo tee /srv/strona/index.html
sudo dnf install policycoreutils-python-utils
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/strona(/.*)?"
sudo restorecon -Rv /srv/strona
sudo semanage fcontext -l | grep /srv/strona
```

Reguła dodana przez `semanage fcontext` trafia do lokalnej konfiguracji polityki — widać ją w `semanage fcontext -l`, więc każde kolejne etykietowanie (`restorecon`, relabel całego systemu) odtworzy właściwe typy. (Żeby Apache faktycznie serwował z tej ścieżki, potrzebna jest jeszcze jego własna konfiguracja — to już nie SELinux.)

## 8. Boolean dla baz danych

```bash
sudo getsebool -a | grep httpd
sudo setsebool -P httpd_can_network_connect_db on
getsebool httpd_can_network_connect_db
```

Opcja `-P` zapisuje zmianę trwale (przetrwa restart); bez niej boolean wróci do wartości domyślnej.

## 9. Port 8090 dla WWW

```bash
sudo semanage port -l | grep http_port_t
sudo semanage port -a -t http_port_t -p tcp 8090
sudo semanage port -l | grep http_port_t
```

Po dodaniu port 8090 pojawia się na liście typu `http_port_t` — dopiero teraz `httpd` może na nim nasłuchiwać. (Pamiętaj, że dostęp z zewnątrz wymaga jeszcze otwarcia portu w zaporze.)

## 10. sealert

```bash
sudo dnf install setroubleshoot-server
sudo sealert -a /var/log/audit/audit.log
```

`ausearch` pokazuje surowe wpisy audytu; `sealert` grupuje je, tłumaczy na opis zrozumiały dla człowieka i proponuje konkretne polecenia naprawy (`restorecon`, `setsebool`, `semanage`) wraz z oceną, które rozwiązanie jest najbezpieczniejsze.
