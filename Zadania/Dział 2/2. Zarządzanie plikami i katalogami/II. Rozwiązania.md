![](../../../grafiki/2-2-rozwiazania.png)

# Rozwiązania – Zarządzanie plikami i katalogami

## 1.

```bash
touch ~/notatki.txt
mkdir ~/projekt
ls -l ~/notatki.txt
ls -ld ~/projekt
```

`-d` każe `ls` pokazać sam katalog zamiast jego zawartości.

---

## 2.

```bash
ls -l ~/notatki.txt
```

Typowy wynik `-rw-rw-r--` czytamy: zwykły plik, właściciel czyta i pisze (`rw-` = 6), grupa czyta i pisze (`rw-` = 6), pozostali tylko czytają (`r--` = 4) – ósemkowo `664`.

---

## 3.

```bash
chmod 640 ~/notatki.txt
chmod u=rw,g=r,o= ~/notatki.txt
```

Oba zapisy ustawiają dokładnie te same uprawnienia `rw-r-----`.

---

## 4.

```bash
chmod u-x ~/projekt
cd ~/projekt        # Permission denied
chmod u+x ~/projekt
```

Dla katalogu `x` oznacza prawo wejścia – bez niego `cd` jest niemożliwe, nawet gdy `r` pozwala listować nazwy.

---

## 5.

```bash
echo 'echo "Działam!"' > ~/skrypt.sh
chmod u+x ~/skrypt.sh
~/skrypt.sh
```

Uruchomienie `./plik` wymaga bitu `x` dla uruchamiającego.

---

## 6.

```bash
umask          # zwykle 0002
umask 077
touch ~/prywatny.txt
ls -l ~/prywatny.txt    # -rw-------
```

Maska `077` odbiera grupie i pozostałym wszystko: 666 − 077 → `600`.

---

## 7.

To **bit sticky** (litera `t` na końcu uprawnień). W katalogu z tym bitem plik może usunąć tylko jego właściciel (oraz właściciel katalogu i root), mimo że prawo `w` do katalogu mają wszyscy.

---

## 8.

```bash
find ~ -type f -name "*.txt"
```

Cudzysłów chroni `*` przed rozwinięciem przez powłokę.

---

## 9.

```bash
find /etc -iname "*host*" 2>/dev/null
```

`-iname` ignoruje wielkość liter, a `2>/dev/null` ukrywa błędy `Permission denied`.

---

## 10.

```bash
find /var/log -type f -size +1M 2>/dev/null
find /var/log -type f -mtime -1 2>/dev/null
```

`+1M` = więcej niż 1 MB; `-mtime -1` = zmodyfikowane mniej niż dobę temu.

---

## 11.

```bash
find /home -user "$USER" 2>/dev/null
sudo find / -type d -name ssh 2>/dev/null
```

---

## 12.

```bash
mkdir ~/smieci && touch ~/smieci/a.tmp ~/smieci/b.tmp ~/smieci/c.tmp
find ~/smieci -type f -name "*.tmp"            # najpierw podgląd
find ~/smieci -type f -name "*.tmp" -delete    # potem usunięcie
```

`-delete` zawsze na końcu polecenia i zawsze po obejrzeniu listy.

---

## 13.

```bash
sudo dnf install plocate     # na starszych systemach: mlocate
sudo updatedb
locate sshd_config
touch ~/nowy-plik-locate.txt
locate nowy-plik-locate      # brak wyniku
sudo updatedb && locate nowy-plik-locate
```

`locate` przeszukuje bazę budowaną przez `updatedb` – nie zna plików utworzonych po jej ostatniej aktualizacji.

---

## 14.

```bash
head -n 5 /etc/passwd
tail -n 3 /etc/passwd
cat -n /etc/passwd
```

---

## 15.

```bash
less /etc/services
```

Klawisze: `/http` + Enter (szukanie), `n` (następne trafienie), `G` (koniec pliku), `g` (początek), `q` (wyjście).

---

## 16.

```bash
sudo tail -f /var/log/messages
# drugi terminal:
logger "test szkoleniowy"
# powrót, Ctrl+C przerywa tail -f
```

`logger` dopisuje własny komunikat do dziennika systemowego – wygodny do testów.

---

## 17.

```bash
grep -c "/sbin/nologin" /etc/passwd
```

Albo potokiem: `cat /etc/passwd | grep /sbin/nologin | wc -l` – `grep -c` liczy pasujące wiersze sam.

---

## 18.

```bash
cut -d: -f1 /etc/passwd | sort > ~/konta.txt
```

`cut` wycina pierwsze pole rozdzielane dwukropkiem, `sort` sortuje, `>` zapisuje do pliku.

---

## 19.

```bash
printf 'kot pierwszy\nkot drugi kot\nkot trzeci\n' > ~/test-sed.txt
sed 's/kot/pies/g' ~/test-sed.txt          # podgląd, plik bez zmian
sed -i.bak 's/kot/pies/g' ~/test-sed.txt   # zapis, oryginał w test-sed.txt.bak
```

---

## 20.

```bash
cp /etc/ssh/sshd_config ~/sshd_config
sed -e '/^#/d' -e '/^$/d' ~/sshd_config
```

Pierwsze wyrażenie usuwa komentarze, drugie puste wiersze; plik pozostaje nietknięty.

---

## 21.

```bash
sed 's/^#\?MaxAuthTries .*/MaxAuthTries 3/' ~/sshd_config | grep MaxAuthTries   # podgląd
sed -i.bak 's/^#\?MaxAuthTries .*/MaxAuthTries 3/' ~/sshd_config                # zapis z kopią
```

`\?` dopuszcza opcjonalny `#` na początku, a `.*` zastępuje dotychczasową wartość do końca wiersza.
