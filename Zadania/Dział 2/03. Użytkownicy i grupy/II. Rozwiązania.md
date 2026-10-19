![](../../../grafiki/2-03-rozwiazania.png)

# Rozwiązania – Użytkownicy i grupy

## 1.

Root (UID 0) ma nieograniczony dostęp do wszystkich plików, procesów i ustawień – system nie sprawdza dla niego uprawnień. Na co dzień pracujemy na zwykłym koncie, bo każda pomyłka roota (literówka w `rm`, zły plik konfiguracyjny) dotyka całego systemu, a praca przez `sudo` zostawia ślad w dzienniku i ogranicza skutki błędów.

---

## 2.

```bash
sudo -l
sudo head -3 /etc/shadow
```

`sudo -l` wypisuje reguły obowiązujące Twoje konto; `/etc/shadow` jest czytelny tylko dla roota, więc bez `sudo` zobaczysz `Permission denied`.

---

## 3.

`su` i `su -` pytają o **hasło roota**; `sudo -i` o **Twoje własne**. `su` bez myślnika zachowuje stare środowisko (m.in. PATH bez `/usr/sbin`), `su -` i `sudo -i` uruchamiają pełną powłokę logowania roota z jego środowiskiem.

---

## 4.

```bash
sudo useradd -c "Konto testowe" tester
sudo passwd tester
sudo usermod -aG wheel tester
su - tester
sudo -l
exit
```

Na RHEL prawo do sudo daje członkostwo w grupie `wheel`; nowa grupa działa od świeżego zalogowania.

---

## 5.

```bash
sudo visudo -f /etc/sudoers.d/tester
# treść pliku:
# tester ALL=(root) NOPASSWD: /usr/bin/systemctl status sshd
su - tester
sudo systemctl status sshd      # działa bez hasła
sudo cat /etc/shadow            # pyta o hasło / odmawia zgodnie z regułami
exit
sudo journalctl -g sudo --since today
```

`visudo` sprawdza składnię przed zapisem; dziennik pokazuje, kto i jakie polecenie wykonał.

---

## 6.

```bash
sudo useradd -c "Tux Pierwszy" tux1
sudo useradd -c "Tux Drugi" tux2
sudo passwd tux1
sudo passwd tux2
id tux1; id tux2
```

---

## 7.

```bash
sudo ls -la /home/tux1
ls -la /etc/skel
```

Pliki startowe (`.bashrc`, `.bash_profile`…) zostały skopiowane z szablonu `/etc/skel` w chwili tworzenia konta przez `useradd`.

---

## 8.

```bash
su - tux1        # działa
exit
sudo usermod -L tux1
su - tux1        # hasło odrzucane – w /etc/shadow przed skrótem pojawił się "!"
sudo usermod -U tux1
```

---

## 9.

```bash
sudo chage -d 0 tux1
sudo chage -l tux1
```

`-d 0` oznacza „hasło nigdy nie zmieniane”, więc system wymusi zmianę przy najbliższym logowaniu.

---

## 10.

```bash
sudo chage -M 90 -W 7 tux2
sudo chage -l tux2
```

---

## 11.

```bash
sudo usermod -aG wheel tux1
id tux1
```

Konieczna jest opcja `-a` (append). Samo `usermod -G wheel tux1` **zastąpiłoby** całą listę grup dodatkowych – tux1 wypadłby ze wszystkich pozostałych.

---

## 12.

```bash
w
last | head
```

`w` pokazuje zalogowanych i ich aktywność, `last` – historię logowań z `/var/log/wtmp`.

---

## 13.

```bash
sudo groupadd pingwiny
sudo gpasswd -M tux1,tux2 pingwiny
getent group pingwiny
```

Zamiast `-M` można dwa razy `gpasswd -a` albo `usermod -aG pingwiny tux1` itd.

---

## 14.

Grupa główna (dokładnie jedna) jest zapisana w czwartym polu `/etc/passwd` i to ona staje się grupą nowo tworzonych plików użytkownika. Grupy dodatkowe (dowolnie wiele) są wymienione przy grupie w `/etc/group` i dają dostęp do zasobów zespołowych.

---

## 15.

```bash
sudo mkdir -p /srv/pingwiny
sudo chown root:pingwiny /srv/pingwiny
sudo chmod 2770 /srv/pingwiny
sudo -u tux1 touch /srv/pingwiny/test.txt
ls -l /srv/pingwiny
```

`2` z przodu to SGID – nowy plik `test.txt` należy do grupy `pingwiny`, a nie do prywatnej grupy `tux1`.

---

## 16.

```bash
sudo gpasswd -d tux2 pingwiny
id tux2
```

---

## 17.

```bash
getent passwd tux1
```

Pola: nazwa konta, `x` (hasło przeniesione do `/etc/shadow`, bo `passwd` musi być czytelny dla wszystkich), UID, GID grupy głównej, opis (GECOS), katalog domowy, powłoka.

---

## 18.

```bash
sudo grep "^tux1:" /etc/shadow
```

Konto zablokowane ma `!` na początku drugiego pola (przed skrótem hasła). Skrót SHA-512 zaczyna się od `$6$` (yescrypt, spotykany w nowszych systemach, od `$y$`).

---

## 19.

`getent` pyta wszystkie skonfigurowane źródła kont – także LDAP/AD – więc działa również dla kont, których nie ma w lokalnym pliku; poza tym dopasowuje całą nazwę, a nie przypadkowy fragment wiersza. Do ręcznej edycji służy `sudo vipw` (oraz `vigr` dla grup) – blokuje plik i pilnuje składni.

---

## 20.

(a) Jedno konto i hasło na całą infrastrukturę: założenie, blokada i usunięcie konta w jednym miejscu działa wszędzie. (b) PAM to warstwa, przez którą przechodzi każde logowanie i która decyduje o wpuszczeniu; sssd to demon pośredniczący – odpytuje AD/LDAP i przechowuje wyniki w pamięci podręcznej. (c) `sudo realm join firma.local -U Administrator` (po instalacji pakietów realmd/sssd/adcli/oddjob-mkhomedir). (d) Dzięki pamięci podręcznej sssd – przy braku łącza uwierzytelnia na podstawie zapamiętanych danych.

---

## 21.

```bash
sudo userdel -r tux1
sudo userdel -r tux2
sudo userdel -r tester
sudo rm -f /etc/sudoers.d/tester
sudo groupdel pingwiny 2>/dev/null
sudo rm -rf /srv/pingwiny
sudo find /home -nouser
```

Grupa `pingwiny` mogła zniknąć wcześniej tylko wtedy, gdyby była czyjąś grupą główną – tu jest dodatkowa, więc `groupdel` działa. `find -nouser` wyszukuje osierocone pliki.
