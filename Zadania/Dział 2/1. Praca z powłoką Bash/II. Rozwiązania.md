![](../../../grafiki/2-1-rozwiazania.png)

# Rozwiązania – Praca z powłoką Bash

> Zestawy odpowiadają kolejnym tematom modułu; numeracja zaczyna się od nowa w każdym z nich.

## Praca na powłoce

### 1. Sprawdź, w jakim katalogu aktualnie się znajdujesz.

```
Polecenie:
pwd

Wyjaśnienie:
- pwd = Print Working Directory
- Pokazuje pełną ścieżkę bieżącego katalogu
- Używa absolutnej ścieżki (zaczynającej się od /)

Przykładowe wyjście:
/home/username
/Users/username (macOS)
/root (gdy jesteś rootem)
```

---

### 2. Wyświetl zawartość bieżącego katalogu.

```
Podstawowe polecenie:
ls

Dodatkowe opcje:
ls -l      # Długi format z szczegółami
ls -la     # Włącznie z plikami ukrytymi
ls -lh     # Z rozmiarem w czytelnym formacie
ls -lt     # Sortowane według czasu modyfikacji
ls -lS     # Sortowane według rozmiaru

Informacje w ls -l:
drwxr-xr-x  2 user group  4096 Oct 23 10:30 katalog
-rw-r--r--  1 user group  1024 Oct 23 10:25 plik.txt

Pierwszy znak: d=katalog, -=plik, l=link
Następne 9 znaków: uprawnienia (właściciel, grupa, inni)
Liczba: liczba linków
user: właściciel
group: grupa
4096: rozmiar w bajtach
Data i czas: ostatnia modyfikacja
```

---

### 3. Utwórz nowy katalog o nazwie `szkolenie` w bieżącej lokalizacji.

```
Polecenie:
mkdir szkolenie

Weryfikacja:
ls -ld szkolenie

Dodatkowe opcje mkdir:
mkdir -p ścieżka/do/katalogu    # Tworzy całą ścieżkę rekurencyjnie
mkdir -m 755 szkolenie          # Ustawia konkretne uprawnienia
mkdir katalog1 katalog2         # Tworzy wiele katalogów jednocześnie

Przykład tworzenia zagnieżdżonych katalogów:
mkdir -p projekt/src/main/java
```

---

### 4. Przejdź do katalogu `szkolenie`.

```
Polecenie:
cd szkolenie

Weryfikacja:
pwd

Inne sposoby nawigacji:
cd /ścieżka/absolutna          # Ścieżka absolutna
cd ../katalog                  # Ścieżka względna
cd ~                          # Katalog domowy użytkownika
cd -                          # Poprzedni katalog
cd                            # Katalog domowy (bez argumentu)
cd ..                         # Katalog wyżej

Przydatne zmienne środowiskowe:
$HOME - katalog domowy
$OLDPWD - poprzedni katalog
$PWD - bieżący katalog
```

---

### 5. Utwórz pięć plików: `plik1`, `plik2`, `plik3`, `plik4`, `plik5` – za pomocą jednego polecenia.

```
Różne sposoby:

Touch z wieloma argumentami:
touch plik1 plik2 plik3 plik4 plik5

Touch z brace expansion:
touch plik{1,2,3,4,5}
touch plik{1..5}

Seq z xargs:
seq 1 5 | xargs -I {} touch plik{}

For loop w jednej linii:
for i in {1..5}; do touch plik$i; done

Weryfikacja:
ls -l plik*
```

---

### 6. Utwórz ukryty plik o nazwie `.ukryty.txt`.

```
Polecenie:
touch .ukryty.txt

Wyjaśnienie:
- Pliki ukryte w Linux zaczynają się od kropki (.)
- Nie są wyświetlane przez standardowe ls
- Są widoczne z opcją ls -a

Inne sposoby tworzenia plików:
echo "" > .ukryty.txt
cat > .ukryty.txt
# (Ctrl+D aby zakończyć)

Weryfikacja istnienia:
ls -la .ukryty.txt
file .ukryty.txt
```

---

### 7. Wyświetl pełną zawartość katalogu, łącznie z plikami ukrytymi.

```
Polecenie:
ls -la

Alternatywy:
ls -al      # Identyczne
ls -a -l    # To samo, oddzielne opcje
ll -a       # Jeśli ll jest aliasem dla ls -l

Wyjaśnienie opcji:
-l: długi format (long)
-a: wszystkie pliki (all), włącznie z ukrytymi

Przykładowe wyjście:
total 24
drwxr-xr-x  2 user group 4096 Oct 23 10:30 .
drwxr-xr-x  3 user group 4096 Oct 23 10:25 ..
-rw-r--r--  1 user group    0 Oct 23 10:30 .ukryty.txt
-rw-r--r--  1 user group    0 Oct 23 10:30 plik1
-rw-r--r--  1 user group    0 Oct 23 10:30 plik2
...

Specjalne katalogi:
. - bieżący katalog
.. - katalog nadrzędny
```

---

### 8. Zmień nazwę pliku `.ukryty.txt` na `plik6`.

```
Polecenie:
mv .ukryty.txt plik6

Wyjaśnienie:
- mv = move (przenieś)
- Służy do przenoszenia i zmiany nazwy
- Pierwszy argument: źródło
- Drugi argument: cel

Weryfikacja:
ls -la | grep plik6
ls -la .ukryty.txt  # Powinno pokazać "No such file"

Inne użycia mv:
mv plik katalog/           # Przeniesienie do katalogu
mv plik1 plik2 katalog/    # Przeniesienie wielu plików
mv katalog1 katalog2       # Zmiana nazwy katalogu
mv *.txt backup/           # Przeniesienie wszystkich plików .txt
```

---

### 9. Zapisz tekst `Szkolenie Linux` do pliku `plik3`.

```
Różne sposoby:

Echo z przekierowaniem:
echo "Szkolenie Linux" > plik3

Printf:
printf "Szkolenie Linux\n" > plik3

Cat z heredoc:
cat > plik3 << EOF
Szkolenie Linux
EOF

Tee:
echo "Szkolenie Linux" | tee plik3

Weryfikacja:
cat plik3
head plik3
less plik3

Różnica między > i >>:
> - nadpisuje plik (truncate)
>> - dopisuje na końcu pliku (append)
```

---

### 10. Wyświetl zawartość pliku `plik3`.

```
Podstawowe polecenia:

Cat (najczęściej używane):
cat plik3

Less (dla większych plików):
less plik3
# q - wyjście, spacja - następna strona, b - poprzednia strona

More (starsze, mniej funkcjonalne):
more plik3

Head (pierwsze linie):
head plik3
head -n 5 plik3    # Pierwsze 5 linii

Tail (ostatnie linie):
tail plik3
tail -n 5 plik3    # Ostatnie 5 linii

Grep (wyszukiwanie):
grep "Linux" plik3
```

---

### 11. Z aktualnej lokalizacji utwórz folder `/tmp/test`.

```
Polecenie:
mkdir -p /tmp/test

Wyjaśnienie:
- Używamy ścieżki absolutnej (/tmp/test)
- Opcja -p tworzy katalogi rekurencyjnie
- Jeśli /tmp nie istnieje, zostanie utworzony
- Opcja -p nie zgłasza błędu jeśli katalog już istnieje

Weryfikacja:
ls -ld /tmp/test
ls -la /tmp/ | grep test

Bez opcji -p (gdyby /tmp nie istniał):
mkdir: cannot create directory '/tmp/test': No such file or directory
```

---

### 12. Czym jest katalog `/tmp`? Jakie ma właściwości?

```
Katalog /tmp (temporary):

Przeznaczenie:
- Przechowywanie plików tymczasowych
- Pliki mogą być usunięte przy restarcie systemu
- Dostępny dla wszystkich użytkowników

Właściwości:
- Uprawnienia: drwxrwxrwt (sticky bit)
- Sticky bit (t): tylko właściciel może usuwać swoje pliki
- World-writable: każdy może tworzyć pliki
- Często montowany jako tmpfs (w pamięci RAM)

Lokalizacja w różnych systemach:
/tmp - standardowy katalog tymczasowy
/var/tmp - dla plików o dłuższym czasie życia
/dev/shm - shared memory (tmpfs)

Zarządzanie:
- systemd-tmpfiles czyści stare pliki
- tmpwatch usuwa niewykorzystane pliki
- Polityki czyszczenia konfigurowalne

Sprawdzenie typu systemu plików:
df -T /tmp
mount | grep tmp

Zmienne środowiskowe:
$TMPDIR - katalog tymczasowy dla aplikacji
$TMP, $TEMP - alternatywne zmienne

Bezpieczeństwo:
- Uważaj na race conditions
- Używaj mktemp do tworzenia bezpiecznych nazw
- Sprawdzaj uprawnienia plików
```

---

### 13. Skopiuj całą zawartość bieżącego katalogu do `/tmp/test`.

```
Polecenie:
cp -r * /tmp/test/

Wyjaśnienie opcji:
-r: rekurencyjnie (dla katalogów)
*: wszystkie pliki i katalogi (wildcard)

Alternatywne metody:

Kopiowanie z ukrytymi plikami:
cp -r .* * /tmp/test/ 2>/dev/null

Rsync (bardziej zaawansowane):
rsync -av . /tmp/test/

Find z exec:
find . -type f -exec cp {} /tmp/test/ \;

Tar (kopiowanie przez archiwum):
tar -cf - . | (cd /tmp/test && tar -xf -)

Uwagi:
- cp * nie kopiuje plików ukrytych (zaczynających się od .)
- Opcja -a zachowuje atrybuty (timestamps, permissions)
- Opcja -v pokazuje kopiowane pliki (verbose)

Weryfikacja:
ls -la /tmp/test/
```

---

### 14. Wyświetl zawartość katalogu `/tmp/test`.

```
Polecenie:
ls -la /tmp/test

Alternatywy:
ls -la /tmp/test/
find /tmp/test -ls
tree /tmp/test (jeśli zainstalowane)

Porównanie z oryginalnym katalogiem:
ls -la szkolenie
ls -la /tmp/test

Sprawdzenie czy kopiowanie się udało:
diff -r . /tmp/test/

Liczenie plików:
ls -1 /tmp/test | wc -l
find /tmp/test -type f | wc -l
```

---

### 15. Przejdź jeden katalog wyżej.

```
Polecenie:
cd ..

Weryfikacja:
pwd

Wyjaśnienie:
.. - katalog nadrzędny (parent directory)
. - bieżący katalog (current directory)

Inne sposoby:
cd $OLDPWD  # Poprzedni katalog
cd -        # Poprzedni katalog (skrót)

Przejście o wiele poziomów wyżej:
cd ../..       # Dwa poziomy wyżej
cd ../../..    # Trzy poziomy wyżej

Sprawdzenie ścieżki:
pwd
echo $PWD
```

---

### 16. Wyświetl zawartość `/tmp`, pokazując tylko folder `test`.

```
Polecenia:

Grep z ls:
ls -la /tmp | grep test

Ls z wzorcem:
ls -ld /tmp/test

Find:
find /tmp -maxdepth 1 -name "test" -type d

Ls z wildcard:
ls -ld /tmp/test*

Tylko nazwa (bez szczegółów):
ls /tmp | grep "^test$"

Sprawdzenie typu:
file /tmp/test
ls -ld /tmp/test | grep "^d"
```

---

### 17. Przejdź do katalogu `/tmp/test` i usuń wszystkie znajdujące się w nim pliki.

```
Kroki:
1. cd /tmp/test
2. rm *

Alternatywne metody usuwania:

Wszystkie pliki (bez katalogów):
rm -f *

Wszystkie pliki włącznie z ukrytymi:
rm -f .* *
rm -f .[^.]* ..?* *  # Bezpieczniejsze

Tylko pliki (nie katalogi):
find . -type f -delete
find . -maxdepth 1 -type f -exec rm {} \;

Z potwierdzeniem:
rm -i *

Bez pytań:
rm -f *

Weryfikacja:
ls -la
# Powinno pokazać tylko . i ..

Uwagi bezpieczeństwa:
- Sprawdź pwd przed rm *
- Używaj rm -i dla ważnych danych
- Rozważ backup przed usuwaniem
- Uważaj na spacje w nazwach plików
```

---

### 18. Wróć katalog wyżej.

```
Polecenie:
cd ..

Alternatywy:
cd /tmp
cd $OLDPWD (jeśli wcześniej byłeś w /tmp)

Weryfikacja lokalizacji:
pwd
# Powinno pokazać: /tmp

Inne sposoby nawigacji:
cd -    # Toggle między dwoma ostatnimi katalogami
popd    # Jeśli używasz pushd/popd stack
```

---

### 19. Usuń pusty katalog `test`.

```
Polecenie:
rmdir test

Alternatywy:
rm -d test    # Nowsze wersje rm
rm -rf test   # Usuwa rekurencyjnie (nawet niepusty)

Wyjaśnienie:
- rmdir usuwa tylko puste katalogi
- Zgłosi błąd jeśli katalog nie jest pusty
- rm -rf usuwa rekurencyjnie wszystko

Weryfikacja:
ls -la | grep test
ls -ld test  # Powinno pokazać "No such file or directory"

Sprawdzenie czy katalog jest pusty:
ls -la test
find test -mindepth 1 -print -quit
```

---

### 20. Przejdź do katalogu domowego użytkownika.

```
Różne sposoby:

Najkrótszy:
cd

Używając tyldy:
cd ~

Używając zmiennej HOME:
cd $HOME

Pełna ścieżka:
cd /home/username     # Linux
cd /Users/username    # macOS

Dla innego użytkownika:
cd ~username

Weryfikacja:
pwd
echo $HOME

Sprawdzenie gdzie jesteśmy:
whoami
id
```

---

### 21. Wyświetl historię ostatnio używanych poleceń.

```
Podstawowe polecenie:
history

Opcje history:
history 10        # Ostatnie 10 poleceń
history | tail    # Ostatnie polecenia
history | head    # Pierwsze polecenia
history | grep ls # Wszystkie polecenia zawierające "ls"

Numeracja w historii:
!123     # Wykonaj polecenie numer 123
!!       # Ostatnie polecenie
!-2      # Przedostatnie polecenie
!ls      # Ostatnie polecenie zaczynające się od "ls"

Pliki historii:
~/.bash_history    # Bash
~/.zsh_history     # Zsh
~/.history         # Niektóre shelle

Zmienne środowiskowe:
$HISTSIZE - rozmiar historii w pamięci
$HISTFILE - plik historii
$HISTFILESIZE - rozmiar pliku historii

Czyszczenie historii:
history -c    # Wyczyść historię w pamięci
history -w    # Zapisz historię do pliku
> ~/.bash_history  # Wyczyść plik historii
```

---

### 22. Zapisz historię poleceń do pliku `historia.txt`.

```
Różne sposoby:

History z przekierowaniem:
history > historia.txt

History z ostatnimi N poleceniami:
history 50 > historia.txt

Z numeracją:
history | cat -n > historia.txt

Bez numerów (tylko polecenia):
history | cut -d' ' -f2- > historia.txt
history | sed 's/^[ ]*[0-9]*[ ]*//' > historia.txt

Dopisanie na koniec:
history >> historia.txt

Z timestampem:
HISTTIMEFORMAT="%F %T " history > historia.txt

Weryfikacja:
cat historia.txt
wc -l historia.txt
head -5 historia.txt
tail -5 historia.txt

Kopiowanie pliku historii:
cp ~/.bash_history historia.txt

Filtrowanie historii:
history | grep -v "history" > historia.txt  # Bez poleceń history
```

## Prompt

### 1. Wygeneruj swój własny styl wiersza poleceń dla powłoki bash.

```
Generatory prompt dla bash:

Popularne strony do generowania:
- https://scriptim.github.io/bash-prompt-generator/
- https://bashrcgenerator.com/
- https://ezprompt.net/

Proces tworzenia custom prompt:

1. Wybierz elementy prompt:
   - Nazwa użytkownika (\u)
   - Nazwa hosta (\h)
   - Bieżący katalog (\w lub \W)
   - Czas (\t, \T, \@)
   - Data (\d)
   - Numer polecenia (\#)

2. Wybierz kolory:
   - \[\033[31m\] - czerwony
   - \[\033[32m\] - zielony
   - \[\033[33m\] - żółty
   - \[\033[34m\] - niebieski
   - \[\033[35m\] - magenta
   - \[\033[36m\] - cyan
   - \[\033[0m\]  - reset koloru

3. Przykładowe custom prompt:

Podstawowy kolorowy prompt:
export PS1="\[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[0m\]\$ "

Zaawansowany prompt z czasem:
export PS1="\[\033[36m\][\t]\[\033[0m\] \[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[0m\]\$ "

Prompt z git branch (wymaga git):
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="\[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[0m\]\$ "

Wieloliniowy prompt:
export PS1="\[\033[36m\]┌─[\[\033[32m\]\u@\h\[\033[36m\]]─[\[\033[34m\]\w\[\033[36m\]]\n└─\[\033[0m\]\$ "

Prompt z statusem ostatniego polecenia:
export PS1='\[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[0m\]$(if [ $? -eq 0 ]; then echo "\[\033[32m\] ✓"; else echo "\[\033[31m\] ✗"; fi)\[\033[0m\]\$ '

Zmienne używane w prompt:
\u - nazwa użytkownika
\h - nazwa hosta (krótka)
\H - pełna nazwa hosta
\w - pełna ścieżka do katalogu roboczego
\W - nazwa bieżącego katalogu
\d - data w formacie "Wkd Mon Date"
\t - czas w formacie 24-godzinnym HH:MM:SS
\T - czas w formacie 12-godzinnym HH:MM:SS
\@ - czas w formacie 12-godzinnym z AM/PM
\# - numer polecenia w historii
\! - numer polecenia w historii
\$ - wyświetla $ dla zwykłego użytkownika, # dla root
```

---

### 2. Zapisz wygenerowany bash w pliku konfiguracyjnym .bashrc.

```
Kroki edycji .bashrc:

1. Przejdź do katalogu domowego:
cd ~

2. Otwórz .bashrc w edytorze:
nano .bashrc

3. Znajdź sekcję PS1 lub dodaj na końcu pliku:
# Custom prompt
export PS1="twój_wygenerowany_prompt"

Przykład dodania do .bashrc:

# Backup oryginalnego prompt
# export PS1='\u@\h:\w\$ '

# Custom colorful prompt
export PS1="\[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[0m\]\$ "

Alternatywne metody:

Dodaj za pomocą echo:
echo 'export PS1="\[\033[32m\]\u@\h\[\033[0m\]:\[\033[34m\]\w\[\033[0m\]\$ "' >> ~/.bashrc

Edytuj z vim:
vim ~/.bashrc

Sprawdź zawartość .bashrc:
cat ~/.bashrc | grep PS1

Backup .bashrc przed zmianami:
cp ~/.bashrc ~/.bashrc.backup

Lokalizacje plików konfiguracyjnych bash:
~/.bashrc - dla non-login shells
~/.bash_profile - dla login shells
~/.profile - uniwersalny dla różnych shell'i
/etc/bash.bashrc - systemowy bashrc

Debugowanie .bashrc:
bash -x ~/.bashrc  # Uruchom z debugowaniem

Sprawdź składnię:
bash -n ~/.bashrc  # Sprawdź składnię bez wykonywania
```

---

### 3. Załaduj ponownie powłokę.

```
Różne sposoby przeładowania konfiguracji:

1. Source .bashrc:
source ~/.bashrc

2. Dot command (identyczny z source):
. ~/.bashrc

3. Nowa instancja bash:
bash

4. Exec bash (zastąpi obecną sesję):
exec bash

5. Logout i login ponownie:
exit
# Zaloguj się ponownie

6. Dla nowych terminali:
# Otwórz nowy terminal - automatycznie załaduje .bashrc

Weryfikacja czy prompt się zmienił:
- Prompt powinien wyglądać zgodnie z konfiguracją
- Sprawdź czy kolory działają
- Sprawdź czy wszystkie elementy są wyświetlane

Debugowanie problemów:

Sprawdź czy .bashrc jest ładowany:
echo "Bashrc loaded" >> ~/.bashrc
source ~/.bashrc

Sprawdź zmienną PS1:
echo $PS1

Tymczasowe testowanie prompt:
PS1="test prompt\$ "  # Zmieni tylko dla bieżącej sesji

Powrót do oryginalnego prompt:
unset PS1  # Użyje domyślnego
source ~/.bashrc  # Lub przeładuj konfigurację

Sprawdź która powłoka jest używana:
echo $SHELL
ps -p $$

Sprawdź czy to login shell:
echo $0
# Jeśli zaczyna się od '-', to login shell

Różnice między typami shell:
- Login shell: ładuje ~/.bash_profile, ~/.profile
- Non-login shell: ładuje ~/.bashrc
- Interactive vs non-interactive

Dodatkowe konfiguracje prompt:

PROMPT_COMMAND - wykonywane przed każdym prompt:
export PROMPT_COMMAND='echo "Czas: $(date)"'

PS2 - prompt dla wieloliniowych poleceń:
export PS2="> "

PS3 - prompt dla select:
export PS3="Wybierz opcję: "

PS4 - prompt dla debug mode:
export PS4="+ "

Przydatne funkcje w prompt:

# Funkcja pokazująca git branch
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Funkcja pokazująca load average
load_avg() {
    uptime | awk '{print $10 $11 $12}'
}

# Prompt z funkcjami
export PS1="\u@\h:\w\$(parse_git_branch) \$ "
```

## Aliasy

### 1. Utwórz tymczasowy alias `czas` do wyświetlenia aktualnej daty i godziny.

```
Polecenie:
alias czas='date'

Alternatywne wersje:
alias czas='date "+%Y-%m-%d %H:%M:%S"'
alias czas='date "+%A, %B %d, %Y - %H:%M:%S"'

Testowanie aliasu:
czas

Sprawdzenie czy alias istnieje:
alias czas
alias | grep czas

Usunięcie aliasu:
unalias czas

Wyjaśnienie:
- Alias jest aktywny tylko w bieżącej sesji
- Po zamknięciu terminala alias zostanie usunięty
- date wyświetla aktualną datę i czas systemowy
```

---

### 2. Utwórz tymczasowy alias `etc` do szybkiego wyświetlenia zawartości katalogu `/etc`.

```
Polecenie:
alias etc='ls -la /etc'

Alternatywne wersje:
alias etc='ls -lh /etc'              # Z czytelnym rozmiarem
alias etc='ls -la /etc | less'       # Z paginacją
alias etc='find /etc -maxdepth 1 -ls' # Z find

Testowanie:
etc

Bardziej zaawansowane wersje:
alias etc='ls -la /etc --color=auto'
alias etc='tree /etc -L 1'  # Jeśli tree jest zainstalowane

Przydatne warianty:
alias etc-conf='ls -la /etc/*.conf'
alias etc-d='ls -la /etc/*d/'
```

---

### 3. Utwórz tymczasowy alias `pakiety` do wyświetlenia listy wszystkich zainstalowanych pakietów.

```
Dla systemów RPM (RHEL, CentOS, Fedora):
alias pakiety='rpm -qa'
alias pakiety='yum list installed'
alias pakiety='dnf list installed'

Dla systemów DEB (Debian, Ubuntu):
alias pakiety='dpkg -l'
alias pakiety='apt list --installed'

Z sortowaniem i formatowaniem:
alias pakiety='rpm -qa | sort'
alias pakiety='rpm -qa | sort | less'

Z liczeniem pakietów:
alias pakiety='echo "Zainstalowane pakiety: $(rpm -qa | wc -l)" && rpm -qa | sort'

Testowanie:
pakiety

Warianty z filtrowaniem:
alias pakiety-kernel='rpm -qa | grep kernel'
alias pakiety-lib='rpm -qa | grep lib'
```

---

### 4. Utwórz tymczasowy alias `dom` do szybkiego przejścia do katalogu domowego.

```
Polecenie:
alias dom='cd ~'

Alternatywne wersje:
alias dom='cd $HOME'
alias dom='cd && pwd'    # Z wyświetleniem lokalizacji
alias dom='cd ~ && ls'   # Z listą plików

Testowanie:
dom

Sprawdzenie lokalizacji:
pwd

Przydatne warianty:
alias dom-ls='cd ~ && ls -la'
alias dom-size='cd ~ && du -sh .'
alias dom-backup='cd ~/backup'
alias dom-downloads='cd ~/Downloads'

Kombinacja z innymi poleceniami:
alias dom-clean='cd ~ && rm -f *.tmp'
```

---

### 5. Utwórz tymczasowy alias `dysk` do wyświetlenia zajętości dysku w formie czytelnej dla użytkownika.

```
Polecenie:
alias dysk='df -h'

Alternatywne wersje:
alias dysk='df -h | grep -v tmpfs'     # Bez systemów tymczasowych
alias dysk='df -h /'                   # Tylko root filesystem

Bardziej szczegółowe:
alias dysk='df -h && echo && du -sh ~' # Z rozmiarem katalogu domowego

Z kolorami (jeśli dostępne):
alias dysk='df -h --output=source,fstype,size,used,avail,pcent,target'

Testowanie:
dysk

Warianty specjalistyczne:
alias dysk-inode='df -i'              # Wykorzystanie i-node'ów
alias dysk-type='df -T'               # Z typami systemów plików
alias dysk-all='df -a'                # Wszystkie systemy plików

Z formatowaniem:
alias dysk='echo "=== Zajętość dysków ===" && df -h | head -1 && df -h | grep -v tmpfs | tail -n +2'
```

---

### 6. Utwórz stały alias `aktualizuj` do wykonania aktualizacji systemu, wyczyszczenia cache oraz wyświetlenia komunikatu o powodzeniu.

```
Dla systemów RPM (RHEL/CentOS/Fedora):

YUM:
alias aktualizuj='sudo yum update -y && sudo yum clean all && echo "System został zaktualizowany!"'

DNF:
alias aktualizuj='sudo dnf update -y && sudo dnf clean all && echo "System został zaktualizowany!"'

Dla systemów DEB (Debian/Ubuntu):
alias aktualizuj='sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean && echo "System został zaktualizowany!"'

Zapisanie stałego aliasu w .bashrc:

1. Otwórz .bashrc:
nano ~/.bashrc

2. Dodaj na końcu pliku:
# Custom aliases
alias aktualizuj='sudo yum update -y && sudo yum clean all && echo "System został zaktualizowany!"'

3. Przeładuj konfigurację:
source ~/.bashrc

Weryfikacja stałego aliasu:
alias aktualizuj
grep aktualizuj ~/.bashrc

Testowanie:
aktualizuj

Zaawansowane wersje z logowaniem:
alias aktualizuj='sudo yum update -y && sudo yum clean all && echo "$(date): System zaktualizowany" >> ~/update.log && echo "System został zaktualizowany!"'

Z backup'em przed aktualizacją:
alias aktualizuj='sudo cp /etc/yum.conf /etc/yum.conf.backup.$(date +%Y%m%d) && sudo yum update -y && sudo yum clean all && echo "System został zaktualizowany!"'

Inne przydatne stałe aliasy do dodania w .bashrc:

# Nawigacja
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'

# Bezpieczeństwo
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Kolory
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# System
alias psg='ps aux | grep'
alias h='history'
alias j='jobs -l'
alias mount='mount | column -t'

# Sieć
alias ping='ping -c 5'
alias fastping='ping -c 100 -s.2'
alias ports='netstat -tulanp'

Zarządzanie aliasami:

Lista wszystkich aliasów:
alias

Sprawdzenie konkretnego aliasu:
alias nazwa_aliasu

Usunięcie aliasu (tymczasowo):
unalias nazwa_aliasu

Usunięcie wszystkich aliasów:
unalias -a

Sprawdzenie czy polecenie to alias:
type polecenie
which polecenie

Backup aliasów:
alias > ~/aliases_backup.txt

Przywrócenie aliasów:
source ~/aliases_backup.txt
```

## Dowiązania – symlink i hardlink

### 1. W swoim katalogu domowym utwórz podkatalog „links". Przejdź do tego katalogu. Utwórz plik „abc" z dowolną treścią.

```
Kroki:
1. cd ~                              # Przejście do katalogu domowego
2. mkdir links                       # Utworzenie katalogu links
3. cd links                          # Przejście do katalogu links
4. echo "Treść pliku abc" > abc      # Utworzenie pliku z treścią

Alternatywne sposoby utworzenia pliku:
cat > abc << EOF
To jest zawartość pliku abc
Druga linia
EOF

touch abc && echo "Treść pliku" > abc

nano abc
# (wpisz treść i zapisz)

Weryfikacja:
pwd                    # Sprawdź lokalizację
ls -la                 # Lista plików
cat abc               # Zawartość pliku
```

---

### 2. Sprawdź informacje pliku abc. W szczególności zwróć uwagę na jego numer i-węzła, jego rozmiar i uprawnienia.

```
Szczegółowe informacje o pliku:

ls -li abc
# -i pokazuje numer i-node
# -l pokazuje szczegółowe informacje

stat abc
# Pełne informacje o pliku

file abc
# Typ pliku

Przykładowe wyjście ls -li:
1234567 -rw-r--r-- 1 user group 18 Oct 23 10:30 abc

Interpretacja:
- 1234567: numer i-node
- -rw-r--r--: uprawnienia (rw- dla właściciela, r-- dla grupy i innych)
- 1: liczba linków (hard links)
- user: właściciel
- group: grupa
- 18: rozmiar w bajtach
- Oct 23 10:30: data i czas ostatniej modyfikacji
- abc: nazwa pliku

Dodatkowe polecenia:
du -b abc             # Rozmiar w bajtach
wc -c abc             # Liczba znaków
ls -s abc             # Rozmiar w blokach
```

---

### 3. Utwórz dowiązanie stałe o nazwie „def" do pliku abc. Spójrz na cechy tego pliku.

```
Utworzenie hard link:
ln abc def

Sprawdzenie cech obu plików:
ls -li abc def

Porównanie:
stat abc
stat def

Obserwacje po utworzeniu hard link:
- Oba pliki mają ten sam numer i-node
- Liczba linków zwiększyła się do 2
- Oba pliki mają identyczny rozmiar
- Identyczne uprawnienia
- Ta sama data modyfikacji

Przykładowe wyjście:
1234567 -rw-r--r-- 2 user group 18 Oct 23 10:30 abc
1234567 -rw-r--r-- 2 user group 18 Oct 23 10:30 def

Ważne cechy hard links:
- Wskazują na ten sam i-node
- Modyfikacja jednego pliku wpływa na drugi
- Usunięcie jednego nie usuwa danych (dopóki link count > 0)
- Działają tylko w obrębie tego samego systemu plików
- Nie można tworzyć hard links do katalogów (zwykle)

Weryfikacja zawartości:
cat abc
cat def
# Identyczna zawartość
```

---

### 4. Zmodyfikuj uprawnienia pliku def (np. 400). Następnie spójrz na uprawnienia abc.

```
Zmiana uprawnień:
chmod 400 def

Sprawdzenie uprawnień obu plików:
ls -l abc def

Obserwacje:
- Uprawnienia abc również się zmieniły na 400 (r--------)
- Hard links dzielą te same metadane
- Zmiana uprawnień jednego pliku wpływa na wszystkie hard links

Wyjaśnienie uprawnień 400:
4 = read (r)
0 = no write (-)
0 = no execute (-)
Tylko właściciel może czytać plik

Testowanie dostępu:
cat abc           # Powinno działać (jesteś właścicielem)
cat def           # Również powinno działać

Przywrócenie normalnych uprawnień:
chmod 644 abc

Sprawdzenie:
ls -l abc def
# Oba pliki powinny mieć uprawnienia 644

Inne przykłady uprawnień:
chmod 755 def     # rwxr-xr-x
chmod 600 abc     # rw-------
chmod u+x def     # Dodaj execute dla właściciela
```

---

### 5. Spójrz na charakterystykę systemu plików i zanotuj/zapamiętaj rozmiar.

```
Sprawdzenie charakterystyki systemu plików:

df -h .
# Pokazuje wykorzystanie systemu plików dla bieżącego katalogu

df -i .
# Pokazuje wykorzystanie i-nodes

du -sh .
# Rozmiar bieżącego katalogu

stat -f .
# Szczegółowe informacje o systemie plików

Zanotuj następujące informacje:
- Całkowity rozmiar systemu plików
- Dostępne miejsce
- Wykorzystane miejsce
- Procent wykorzystania
- Liczba dostępnych i-nodes
- Typ systemu plików

Przykład:
df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  5.2G   14G  28% /

Informacje do zanotowania:
- Used: 5.2G (przed operacjami)
- Avail: 14G
- Use%: 28%

Sprawdzenie i-nodes:
df -i .
Filesystem      Inodes   IUsed   IFree IUse% Mounted on
/dev/sda1      1310720   45234 1265486    4% /
```

---

### 6. Usuń plik abc. Zobacz, co się stało z plikiem def.

```
Usunięcie pliku abc:
rm abc

Sprawdzenie co się stało z def:
ls -li def
cat def

Obserwacje:
- Plik def nadal istnieje i jest dostępny
- Zawartość def pozostała niezmieniona
- Liczba linków zmniejszyła się z 2 do 1
- Numer i-node pozostał ten sam

Sprawdzenie:
ls -li def
# Powinno pokazać link count = 1

Wyjaśnienie:
- Hard link nie jest "skrótem" do pliku
- To równoprawne wskazanie na i-node
- Dane są usuwane dopiero gdy link count = 0
- Usunięcie "oryginalnego" pliku nie wpływa na hard linki

Próba dostępu do abc:
ls abc
cat abc
# Powinno pokazać "No such file or directory"

Test funkcjonalności def:
echo "Nowa linia" >> def
cat def
# Plik def w pełni funkcjonalny
```

---

### 7. Spójrz na charakterystykę systemu plików i sprawdź rozmiar.

```
Sprawdzenie systemu plików po usunięciu abc:

df -h .
du -sh .

Porównanie z poprzednimi wartościami:
- Rozmiar wykorzystanego miejsca powinien być taki sam
- Dane nie zostały usunięte z dysku
- I-node nadal jest w użyciu (przez plik def)

Sprawdzenie i-nodes:
df -i .

Obserwacje:
- Liczba używanych i-nodes nie zmieniła się
- Dane fizycznie nadal istnieją na dysku
- System plików nie odzyskał miejsca

Wyjaśnienie:
Gdy istnieją hard linki, usunięcie jednego z plików:
- Zmniejsza link count
- NIE usuwa danych z dysku
- NIE zwalnia i-node
- NIE zwalnia miejsca na dysku

Miejsce zostanie zwolnione dopiero gdy:
- Wszystkie hard linki zostaną usunięte
- Link count osiągnie 0
- System wykona garbage collection
```

---

### 8. Skasuj plik def.

```
Usunięcie ostatniego hard link:
rm def

Sprawdzenie:
ls -la
# Katalog powinien być pusty (poza . i ..)

find . -name "def"
# Nie powinno znaleźć pliku

Próba dostępu:
cat def
# "No such file or directory"

Co się stało:
- Link count dla i-node osiągnął 0
- System oznaczy i-node jako wolny
- Dane będą oznaczone do usunięcia
- Miejsce na dysku zostanie zwolnione
```

---

### 9. Ponownie sprawdź rozmiar systemu plików.

```
Sprawdzenie po usunięciu wszystkich hard links:

df -h .
du -sh .

Porównanie z początkowymi wartościami:
- Wykorzystane miejsce powinno się zmniejszyć
- Dostępne miejsce powinno się zwiększyć
- Procent wykorzystania powinien spaść

Sprawdzenie i-nodes:
df -i .

Obserwacje:
- Liczba używanych i-nodes zmniejszyła się
- I-node został zwolniony
- Miejsce na dysku zostało odzyskane

Przykład różnicy:
Przed: Used 5.2G, Avail 14G
Po:    Used 5.2G, Avail 14G (rozmiar pliku był mały)

Weryfikacja zwolnienia miejsca:
# Utwórz większy plik do testu
dd if=/dev/zero of=duzy_plik bs=1M count=10
ln duzy_plik hard_link
ls -li duzy_plik hard_link
df -h .

rm duzy_plik
df -h .  # Miejsce nadal zajęte

rm hard_link  
df -h .  # Miejsce zwolnione

Czyszczenie:
cd ..
rmdir links  # Usuń pusty katalog

Kluczowe różnice między Hard Links a Soft Links (Symbolic Links):

Hard Links:
- Wskazują bezpośrednio na i-node
- Działają tylko w obrębie jednego systemu plików
- Nie można tworzyć do katalogów
- Nie "psują się" gdy oryginalny plik jest usunięty
- Licznik referencji w i-node

Soft Links (ln -s):
- Wskazują na ścieżkę do pliku
- Działają między systemami plików
- Można tworzyć do katalogów
- "Psują się" gdy cel zostanie usunięty
- Są oddzielnym plikiem z własnym i-node

Tworzenie soft link (dla porównania):
ln -s /path/to/target symlink_name
ls -la symlink_name  # Widać strzałkę ->
```

## Edytory tekstu

### 1. Utwórz nowy plik tekstowy o nazwie `temp.txt` za pomocą dowolnego edytora.

```
Różne sposoby utworzenia pliku temp.txt:

Nano:
nano temp.txt

Vi/Vim:
vi temp.txt
vim temp.txt

Gedit (w środowisku graficznym):
gedit temp.txt

Touch + edytor:
touch temp.txt
nano temp.txt

Echo:
echo "" > temp.txt
```

---

### 2. Wpisz do pliku frazę: `Szkolenie Linux`

```
W nano:
1. Otwórz: nano temp.txt
2. Wpisz: Szkolenie Linux
3. Tekst pojawia się bezpośrednio

W vi:
1. Otwórz: vi temp.txt
2. Naciśnij 'i' (tryb INSERT)
3. Wpisz: Szkolenie Linux
4. Naciśnij ESC (powrót do trybu COMMAND)
```

---

### 3. Zapisz plik i wyjdź z edytora.

```
W nano:
Ctrl+O (zapisz)
Enter (potwierdź nazwę pliku)
Ctrl+X (wyjdź)

W vi:
ESC (tryb COMMAND)
:wq (write and quit)
Enter

Alternatywne metody w vi:
:w (tylko zapisz)
:q (tylko wyjdź)
ZZ (zapisz i wyjdź - shortcut)
```

---

### 4. Otwórz plik `temp.txt` w edytorze `vi`.

```
Polecenie:
vi temp.txt

Po otwarciu:
- Plik otwiera się w trybie COMMAND
- Zawartość pliku jest widoczna
- Kursor znajduje się na początku pierwszego znaku
- Status line pokazuje informacje o pliku
```

---

### 5. Dopisz do istniejącej frazy słowa `jest proste` korzystając ze skrótu `A`.

```
Kroki w vi:
1. Upewnij się, że jesteś w trybie COMMAND (naciśnij ESC)
2. Naciśnij 'A' (duże A)
   - Kursor przeskoczy na koniec linii
   - Automatyczne przejście do trybu INSERT
3. Wpisz: " jest proste"
4. Naciśnij ESC (powrót do trybu COMMAND)

Rezultat: "Szkolenie Linux jest proste"

Inne przydatne skróty vi:
- a: append (wstaw po kursorze)
- A: append at end of line (wstaw na końcu linii)
- i: insert (wstaw przed kursorem)
- I: insert at beginning of line (wstaw na początku linii)
- o: open new line below (nowa linia poniżej)
- O: open new line above (nowa linia powyżej)
```

---

### 6. Wyjdź z edytora `vi` bez zapisywania zmian.

```
Polecenie w trybie COMMAND:
:q!

Wyjaśnienie:
: - przejście do trybu poleceń
q - quit (wyjdź)
! - force (wymuś, ignoruj niezapisane zmiany)

Inne opcje wyjścia z vi:
:q - wyjdź (tylko jeśli brak zmian)
:wq - zapisz i wyjdź
:x - zapisz i wyjdź (jeśli były zmiany)
ZQ - wyjdź bez zapisywania (shortcut)
ZZ - zapisz i wyjdź (shortcut)
```

---

### 7. Pobierz "Pana Tadeusza" w formacie `.txt` przy użyciu `wget`.

```
Polecenie:
wget https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt

Proces:
1. wget nawiąże połączenie z serwerem
2. Pobierze plik pan-tadeusz.txt
3. Zapisze w bieżącym katalogu

Weryfikacja pobrania:
ls -la pan-tadeusz.txt
file pan-tadeusz.txt
wc -l pan-tadeusz.txt

Alternatywne źródła:
wget http://www.gutenberg.org/files/28564/28564-0.txt -O pan-tadeusz.txt
curl -o pan-tadeusz.txt https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt

Opcje wget:
-O filename - zapisz pod konkretną nazwą
-c - kontynuuj przerwane pobieranie
-t 3 - maksymalnie 3 próby
--timeout=30 - timeout 30 sekund
```

---

### 8. Otwórz pobraną książkę (`pan-tadeusz.txt`) za pomocą edytora `vi`.

```
Polecenie:
vi pan-tadeusz.txt

Uwagi przy otwieraniu dużego pliku:
- Ładowanie może chwilę potrwać
- Vi/vim dobrze radzi sobie z dużymi plikami
- Plik otwiera się w trybie COMMAND
- Kursor na początku pierwszej linii

Podstawowe nawigacje w vi dla dużych plików:
G - przejdź na koniec pliku
gg - przejdź na początek pliku
:liczba - przejdź do konkretnej linii
Ctrl+F - strona w dół
Ctrl+B - strona w górę
Ctrl+D - pół strony w dół
Ctrl+U - pół strony w górę
```

---

### 9. Wyszukaj w tekście imię "Tadeusz" i przejdź przez kolejne wystąpienia.

```
Wyszukiwanie w vi:
1. Upewnij się, że jesteś w trybie COMMAND (ESC)
2. Wpisz: /Tadeusz
3. Naciśnij Enter
4. Vi znajdzie pierwsze wystąpienie i podświetli

Przechodzenie przez wystąpienia:
n - next (następne wystąpienie)
N - previous (poprzednie wystąpienie)

Dodatkowe opcje wyszukiwania:
/Tadeusz\c - wyszukiwanie bez uwzględnienia wielkości liter
?Tadeusz - wyszukiwanie wstecz
* - wyszukaj słowo pod kursorem (w przód)
# - wyszukaj słowo pod kursorem (w tył)

Zastępowanie:
:%s/Tadeusz/TADEUSZ/g - zamień wszystkie wystąpienia
:%s/Tadeusz/TADEUSZ/gc - zamień z potwierdzeniem

Highlight search:
:set hlsearch - podświetlanie wyników
:nohlsearch - wyłączenie podświetlania (lub :noh)
```

---

### 10. Uruchom plik `pan-tadeusz.txt` w edytorze `nano`.

```
Polecenie:
nano pan-tadeusz.txt

Charakterystyka nano:
- Edytor przyjazny dla początkujących
- Skróty klawiszowe wyświetlane na dole ekranu
- Bezpośrednia edycja (bez trybów jak w vi)
- Dobra obsługa dużych plików

Podstawowe skróty w nano:
Ctrl+G - pomoc (help)
Ctrl+X - wyjście (exit)
Ctrl+O - zapisz (write Out)
Ctrl+R - wczytaj plik (Read file)
Ctrl+W - wyszukaj (Where is)
Ctrl+K - wytnij linię (cut)
Ctrl+U - wklej (paste/Uncut)
Ctrl+C - pokaż pozycję kursora
```

---

### 11. Wyszukaj frazę `Tadeusz` i przejdź przez kolejne wystąpienia.

```
Wyszukiwanie w nano:
1. Naciśnij Ctrl+W
2. Wpisz: Tadeusz
3. Naciśnij Enter
4. Nano znajdzie pierwsze wystąpienie

Przechodzenie przez kolejne wystąpienia:
1. Naciśnij ponownie Ctrl+W
2. Naciśnij Enter (bez wpisywania - użyje ostatniego wyszukiwania)
3. Powtarzaj krok 2 dla kolejnych wystąpień

Alternatywna metoda:
Ctrl+W, wpisz "Tadeusz", Alt+W - kontynuuj wyszukiwanie

Dodatkowe opcje wyszukiwania w nano:
Alt+W - powtórz ostatnie wyszukiwanie
Ctrl+\ - znajdź i zamień (Where Is, then Replace)
Alt+R - wyszukiwanie z wyrażeniami regularnymi

Opcje wyszukiwania (po Ctrl+W):
Alt+C - case sensitive (wielkość liter)
Alt+B - backward search (wyszukiwanie wstecz)
Alt+R - regex search (wyrażenia regularne)
```

---

### 12. Wyjdź z edytora `nano` bez zapisywania zmian.

```
Kroki:
1. Naciśnij Ctrl+X (exit)
2. Jeśli były zmiany, nano zapyta: "Save modified buffer?"
3. Naciśnij 'N' (No)
4. Nano zamknie się bez zapisywania

Komunikaty nano:
"Save modified buffer? (Answering "No" will DISCARD changes.)"
- Y: Yes (zapisz)
- N: No (nie zapisuj)
- Ctrl+C: Cancel (anuluj wyjście)

Skróty wyjścia:
Ctrl+X - standardowe wyjście
Ctrl+C (dwukrotnie) - force exit w niektórych sytuacjach
```

---

### 13. Otwórz plik `temp.txt` za pomocą edytora `nano`.

```
Polecenie:
nano temp.txt

Po otwarciu:
- Plik wyświetla się w edytorze
- Kursor na początku pliku
- Skróty klawiszowe widoczne na dole ekranu
- Bezpośrednia możliwość edycji (brak trybów)

Status line pokazuje:
- Nazwę pliku
- Czy plik został zmodyfikowany
- Pozycję kursora (linia, kolumna)
```

---

### 14. Usuń cały wiersz za pomocą odpowiedniego skrótu.

```
Skrót w nano:
Ctrl+K - usuwa całą linię (cut line)

Proces:
1. Ustaw kursor gdziekolwiek w linii do usunięcia
2. Naciśnij Ctrl+K
3. Cała linia zostanie usunięta

Dodatkowe skróty usuwania w nano:
Alt+Del - usuń słowo po lewej stronie kursora
Ctrl+Del - usuń słowo po prawej stronie kursora
Alt+T - usuń od kursora do końca linii
Ctrl+U - wklej ostatnio wycięty tekst (uncut)

Wielokrotne usuwanie:
- Ctrl+K wykonane kilka razy usuwa kolejne linie
- Usunięte linie trafiają do bufora
- Można je przywrócić za pomocą Ctrl+U
```

---

### 15. Wpisz nową frazę: `Używam edytora nano`

```
Proces:
1. Po usunięciu poprzedniej linii kursor jest gotowy do wpisania
2. Wpisz bezpośrednio: Używam edytora nano
3. Tekst pojawia się natychmiast (brak trybów jak w vi)

Nano pozwala na:
- Bezpośrednie wpisywanie tekstu
- Użycie strzałek do nawigacji
- Standardowe zachowanie klawiatury
- Copy/paste systemowe (Ctrl+Shift+C/V w terminalu)
```

---

### 16. Zapisz zmiany i wyjdź z edytora.

```
Kroki:
1. Ctrl+O (WriteOut - zapisz)
   - Nano pokaże: "File Name to Write: temp.txt"
2. Naciśnij Enter (potwierdź nazwę pliku)
   - Komunikat: "[ Wrote 1 line ]"
3. Ctrl+X (Exit - wyjdź)
   - Nano zamknie się

Alternatywna metoda (szybsza):
Ctrl+X, następnie Y (tak, zapisz), Enter (potwierdź nazwę)

Opcje zapisu:
Ctrl+O - zapisz pod bieżącą nazwą
Alt+F - nowa nazwa pliku podczas zapisu
Ctrl+T - przeglądaj pliki (file browser)

Weryfikacja:
cat temp.txt
# Powinno pokazać: "Używam edytora nano"
```

---

### Dodatkowe zasoby i ćwiczenia

```
Przydatne strony do nauki vi/vim:
- https://vim.is/#exercise - interaktywne ćwiczenia
- https://www.openvim.com/ - tutorial online
- vimtutor - wbudowany tutorial (polecenie w terminalu)

Przydatne strony do nauki nano:
- man nano - pełna dokumentacja
- nano --help - szybki help
- https://www.nano-editor.org/dist/latest/cheatsheet.html

Porównanie edytorów:

Vi/Vim:
+ Bardzo potężny i konfigurowalny
+ Dostępny na każdym systemie Unix/Linux
+ Efektywny dla zaawansowanych użytkowników
- Stroma krzywa uczenia
- Tryby mogą być mylące dla początkujących

Nano:
+ Łatwy do nauki
+ Intuicyjny dla nowych użytkowników
+ Skróty wyświetlane na ekranie
- Mniej funkcji niż vim
- Może nie być domyślnie zainstalowany wszędzie

Emacs:
+ Bardzo rozszerzalny
+ Potężne funkcje programistyczne
- Bardzo złożony
- Duże zużycie zasobów
```
