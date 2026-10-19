![](../../../grafiki/2-1-rozwiazania.png)

# Rozwiązania – Praca z powłoką Bash

> Numeracja odpowiada plikowi [I. Zadania.md](I.%20Zadania.md). Przy każdym zadaniu podajemy polecenie i krótkie wyjaśnienie; tam, gdzie jest kilka dobrych dróg, pokazujemy najprostszą.

## 1. Użytkownik, komputer, powłoka

```bash
whoami
hostname
echo $SHELL
```

`whoami` wypisuje nazwę zalogowanego użytkownika, `hostname` nazwę komputera, a zmienna `SHELL` zawiera ścieżkę Twojej domyślnej powłoki (np. `/bin/bash`).

---

## 2. Komunikat błędu

```bash
lss
```

Wynik: `bash: lss: command not found`. Komunikat zgłasza sam Bash (pierwszy człon) – nie znalazł polecenia `lss` ani wśród aliasów, ani wśród poleceń wbudowanych, ani w katalogach z `PATH`. Przyczyną jest literówka (powinno być `ls`) albo brak zainstalowanego programu.

---

## 3. Historia i czyszczenie ekranu

```bash
# ostatnie 10 poleceń z numerami
history 10
# powtórz polecenie o numerze np. 205
!205
# albo: strzałka w górę i Enter, albo Ctrl+R i fragment polecenia
```

```bash
# czyszczenie ekranu – dwa sposoby
clear
# oraz skrót klawiszowy Ctrl+L
```

`!numer` wykonuje polecenie o danym numerze z historii, `!!` powtarza ostatnie. Czyszczenie ekranu nie kasuje historii – tylko odświeża widok.

---

## 4. Nawigacja

```bash
pwd            # gdzie jestem
cd /var/log    # ścieżka bezwzględna
cd ..          # poziom wyżej (/var)
cd             # katalog domowy (samo cd = cd ~)
cd -           # powrót do poprzedniego katalogu (/var)
```

`cd -` przełącza między dwoma ostatnimi katalogami i wypisuje, dokąd przeszedł.

---

## 5. `/etc` od najnowszych, czytelne rozmiary

```bash
ls -lht /etc
```

`-l` długa lista, `-h` rozmiary „dla ludzi”, `-t` sortowanie od najnowszej modyfikacji. Od najstarszych: `ls -lhtr /etc`.

---

## 6. Pliki ukryte

```bash
ls -la ~
```

`-a` pokazuje pliki zaczynające się od kropki. `.` to katalog bieżący, `..` to katalog nadrzędny – te dwa wpisy istnieją w każdym katalogu i dzięki nim działają ścieżki względne typu `cd ..`.

---

## 7. Czytanie `ls -l`

```bash
ls -l /etc/hostname
```

```text
-rw-r--r--. 1 root root 7 10 paź 08:40 /etc/hostname
```

Kolejno: typ i uprawnienia (`-` = zwykły plik; kropka = etykieta SELinux), liczba dowiązań twardych (1), właściciel (`root`), grupa (`root`), rozmiar w bajtach (7), data ostatniej modyfikacji, nazwa.

---

## 8. Ścieżka bezwzględna i względna

```bash
cd ~
ls /var/log        # bezwzględna – od korzenia
ls ../../var/log   # względna – z /home/anna dwa poziomy w górę, potem var/log
```

Ścieżka względna zależy od katalogu bieżącego, bezwzględna działa z każdego miejsca.

---

## 9. Katalog, pięć plików, plik ukryty

```bash
cd ~
mkdir szkolenie
cd szkolenie
touch plik1 plik2 plik3 plik4 plik5    # albo: touch plik{1..5}
touch .ukryty.txt
ls -a                                  # ukryty widać tylko z -a
mv .ukryty.txt plik6
```

`mv` w tym samym katalogu to po prostu zmiana nazwy.

---

## 10. Zapis i dopisanie

```bash
echo "Szkolenie Linux" > plik3    # > nadpisuje (tu: tworzy)
echo "RHEL 9" >> plik3            # >> dopisuje na końcu
cat plik3
```

```text
Szkolenie Linux
RHEL 9
```

Gdyby w drugim poleceniu użyć `>`, pierwszy wiersz by zginął.

---

## 11. Wynik polecenia do pliku

```bash
ls -l /etc > ~/szkolenie/spis-etc.txt
```

Przekierowanie `>` działa z każdym poleceniem – do pliku trafia to, co normalnie poszłoby na ekran.

---

## 12. Kopiowanie do /tmp/test

```bash
mkdir -p /tmp/test
cp -r ~/szkolenie/* /tmp/test/
ls -la /tmp/test
```

`-r` jest potrzebne, gdyby w `szkolenie` były podkatalogi. Uwaga: wzorzec `*` nie obejmuje plików ukrytych – dlatego w `/tmp/test` nie będzie np. `.ukryty.txt` (u nas już przemianowanego).

---

## 13. Symbole wieloznaczne

```bash
cd ~/szkolenie
ls plik?        # plik + dokładnie jeden znak: plik1 … plik6
ls plik[135]    # jeden znak z listy: plik1, plik3, plik5
```

`?` zastępuje dokładnie jeden znak, `[135]` – jeden znak spośród wymienionych.

---

## 14. Usuwanie i `rmdir`

```bash
cd /tmp/test
rm *
cd ..
rmdir test
```

`rmdir` usuwa **wyłącznie puste** katalogi – jeśli coś przeoczysz, zatrzyma się z błędem, zamiast po cichu skasować zawartość. `rm -r` nie daje tej ochrony.

---

## 15. `rm -rf *` – odpowiedź

W katalogu domowym `rm -rf *` usunęłoby **bez żadnego pytania** wszystkie nieukryte pliki i katalogi: dokumenty, projekty, pobrane pliki. `-r` wchodzi w głąb katalogów, `-f` wyłącza pytania i komunikaty o błędach, a Kosza w terminalu nie ma. Dlatego przed `rm` ze wzorcem wykonuje się `ls` z tym samym wzorcem – lista `ls` to dokładnie lista tego, co `rm` skasuje.

---

## 16. Historia do pliku

```bash
history > ~/szkolenie/historia.txt
wc -l ~/szkolenie/historia.txt
```

Przekierowanie zapisuje całą numerowaną historię; `wc -l` pokazuje, ile poleceń trafiło do pliku.

---

## 17. Elementy promptu

```bash
echo $PS1
```

```text
[\u@\h \W]\$
```

W `[anna@serwer ~]$`: `anna` – użytkownik (`\u`), `serwer` – nazwa komputera (`\h`), `~` – katalog bieżący, tylko ostatni człon (`\W`), `$` – znak zwykłego użytkownika. U roota zamiast `$` jest `#` – to ostrzeżenie, że polecenia wykonują się z pełnymi uprawnieniami.

---

## 18. Trzy warianty promptu

```bash
# (a) pełna ścieżka
PS1='[\u@\h \w]\$ '
# (b) dodatkowo godzina
PS1='\t [\u@\h \w]\$ '
# (c) zielony, z kolorami w \[ \]
PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '
cd /etc    # prompt powinien pokazać /etc (wariant a, b) i zielony kolor (c)
```

`\[` i `\]` mówią powłoce, że kody koloru nie zajmują miejsca na ekranie – bez nich kursor „skacze” przy edycji długich poleceń. Spacja na końcu wzoru oddziela prompt od polecenia.

---

## 19. Prompt na stałe

```bash
nano ~/.bashrc
# dopisz na końcu wiersz:
# PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '
source ~/.bashrc
```

Wpis trafia do `~/.bashrc`, bo ten plik czyta **każda** powłoka interaktywna – i logowania (przez `~/.bash_profile`), i nowe okno terminala. `source` wczytuje zmiany w bieżącej sesji.

---

## 20. Zmienna powłoki a środowiskowa

```bash
KURS=Linux
echo $KURS            # Linux
bash -c 'echo $KURS'  # pusto – zmienna powłoki nie przechodzi do procesów potomnych
export KURS
bash -c 'echo $KURS'  # Linux – po export zmienna jest środowiskowa
```

`export` przekazuje zmienną każdemu programowi uruchamianemu z tej powłoki.

---

## 21. `PATH`

```bash
echo $PATH
```

```text
/home/anna/.local/bin:/home/anna/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
```

Powłoka przeszukuje katalogi **od lewej do prawej** i uruchamia pierwszy znaleziony plik o danej nazwie. Katalogu bieżącego (`.`) na liście nie ma – to zabezpieczenie przed podrzuconymi programami – więc skrypt z bieżącego katalogu uruchamiasz, jawnie podając ścieżkę: `./skrypt.sh`.

---

## 22. Aliasy tymczasowe

```bash
alias czas='date'
alias dom='cd ~ && pwd'
alias dysk='df -h'
czas
dom
dysk
alias czas dom dysk   # pokaż definicje
```

Aliasy zdefiniowane w sesji znikają po jej zamknięciu. `unalias czas` usuwa alias.

---

## 23. Alias na stałe

```bash
echo "alias ll='ls -lah'" >> ~/.bashrc
source ~/.bashrc
ll
```

Właściwy plik to `~/.bashrc` – czytają go wszystkie powłoki interaktywne użytkownika, więc alias działa i po SSH, i w nowym oknie terminala. Pliki w `/etc` zmieniałyby ustawienia wszystkim użytkownikom i wymagają uprawnień roota.

---

## 24. Plik i jego i-węzeł

```bash
cd ~
mkdir links
cd links
echo "treść pliku abc" > abc
ls -li abc
```

```text
1835201 -rw-r--r--. 1 anna anna 18 18 paź 12:10 abc
```

Pierwsza kolumna to numer i-węzła, `1` po uprawnieniach to licznik dowiązań twardych, `18` to rozmiar w bajtach. Pełne metadane pokazuje `stat abc`.

---

## 25. Dowiązanie twarde

```bash
ln abc def
ls -li abc def
```

```text
1835201 -rw-r--r--. 2 anna anna 18 18 paź 12:10 abc
1835201 -rw-r--r--. 2 anna anna 18 18 paź 12:10 def
```

Ten sam i-węzeł, ten sam rozmiar, licznik dowiązań wzrósł do 2 – to jeden plik o dwóch nazwach.

```bash
chmod 400 def
ls -l abc def
```

Uprawnienia `abc` też zmieniły się na `r--------`, bo uprawnienia są zapisane w i-węźle, wspólnym dla obu nazw. (Przywróć: `chmod 644 abc`.)

---

## 26. Dowiązanie symboliczne i usunięcie oryginału

```bash
ln -s abc skrot
ls -li
rm abc
cat def      # działa – dane przeżyły, bo def to druga nazwa tego samego i-węzła
cat skrot    # "No such file or directory" – skrot wskazywał NAZWĘ abc, która znikła
ls -l skrot  # dowiązanie "wisi" (w kolorowym terminalu świeci na czerwono)
```

Dowiązanie twarde dzieli i-węzeł, więc przeżywa usunięcie pierwszej nazwy. Dowiązanie symboliczne przechowuje tylko ścieżkę – po usunięciu celu prowadzi donikąd.

---

## 27. Vim – podstawy

```bash
vim temp.txt
```

---

**1.** `i` – tryb wstawiania, wpisz `Szkolenie Linux`, `Esc`.

---

**2.** `:wq` + `Enter` – zapis i wyjście.

```bash
vim temp.txt
```

---

**3.** `A` (wielkie) – kursor skacze na koniec wiersza i włącza się wstawianie; wpisz ` jest proste`, `Esc`.

---

**4.** `:q!` + `Enter` – wyjście bez zapisu; w pliku zostaje samo `Szkolenie Linux` (sprawdź: `cat temp.txt`).

---

## 28. Vim – duży plik i szukanie

```bash
wget https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt
vim pan-tadeusz.txt
```

W trybie normalnym: `G` – koniec pliku, `gg` – początek, `/Tadeusz` + `Enter` – pierwsze wystąpienie, `n` trzy razy – kolejne wystąpienia (`N` cofa). Wyjście: `:q!` (nic nie zmienialiśmy, wystarczyłoby też `:q`).

---

## 29. Nano – szukanie i edycja

```bash
nano pan-tadeusz.txt
```

`Ctrl+W`, wpisz `Zosia`, `Enter` – pierwsze wystąpienie; `Alt+W` – następne. Wyjście: `Ctrl+X` (bez zmian nano nie pyta o zapis).

```bash
nano temp.txt
```

`Ctrl+K` usuwa cały wiersz; wpisz `Używam edytora nano`; zapis i wyjście: `Ctrl+O`, `Enter`, `Ctrl+X` (albo od razu `Ctrl+X`, `Y`, `Enter`).

```bash
cat temp.txt
```

```text
Używam edytora nano
```

---

## 30. Sprzątanie

```bash
cd ~
ls -d szkolenie links temp.txt pan-tadeusz.txt   # kontrola: dokładnie to zniknie
rm -r szkolenie links
rm temp.txt pan-tadeusz.txt
```

Kontrolne `ls` przed `rm -r` pokazuje dokładnie te ścieżki, które za chwilę skasujesz – jeśli lista Cię zaskoczy, jeszcze nic się nie stało.
