# Rozwiązania – Dokumentacja i pomoc

## 1. Sekcje podręcznika

```bash
man man
```

Podręcznik ma 8 sekcji (plus warianty z literami). Sekcja 1 – polecenia użytkownika, sekcja 5 – formaty plików (np. `/etc/passwd`, `/etc/fstab`), sekcja 8 – polecenia administracyjne i demony.

## 2. Strona ls

```bash
man ls
```

Nagłówek `LS(1)` – sekcja 1. Opcje sortowania (szukaj `/sort`): `-t` (czas modyfikacji), `-S` (rozmiar), `-X` (rozszerzenie), `-v` (numery wersji), `-r` (odwrócenie kolejności), `--sort=WORD`. Koniec strony: `G`, początek: `g`.

## 3. Notacja SYNOPSIS

Nawiasy kwadratowe `[OPTION]` oznaczają element opcjonalny, wielokropek `...` – że element można powtórzyć wiele razy. `SOURCE` i `DEST` są bez nawiasów, więc są **wymagane** – `cp plik1` bez celu nie jest zgodne z wzorem i zakończy się błędem („missing destination file operand”).

## 4. passwd w kilku sekcjach

```bash
whatis passwd        # albo: man -f passwd
man 5 passwd
```

`whatis` pokaże co najmniej `passwd (1)` i `passwd (5)`. W `man 5 passwd`: trzecie pole wiersza `/etc/passwd` to **UID** – numeryczny identyfikator użytkownika.

## 5. Szukanie po opisach

```bash
apropos rename       # albo: man -k rename
```

Wynik wskaże m.in. `rename(1)` i `mv(1)`.

## 6. Budowa indeksu

```bash
sudo mandb
```

`apropos` i `whatis` czytają indeks baz man – na świeżym/minimalnym systemie trzeba go zbudować.

## 7. Położenie pliku strony

```bash
man -w 5 passwd
```

Typowy wynik: `/usr/share/man/man5/passwd.5.gz`.

## 8. Nawigacja w info

```bash
info coreutils
```

Odnośnik: `Tab` (najechanie) + `Enter` (wejście); poziom wyżej: `u`; wyjście: `q`. Info jest podzielone na węzły (rozdziały/podrozdziały) połączone odnośnikami i menu – jak książka ze spisem treści, podczas gdy strona man to jeden płaski dokument.

## 9. info pwd

```bash
info pwd
man pwd
```

Dokument info (rozdział coreutils) jest zwykle obszerniejszy i pisany stylem podręcznika. Narzędzia GNU dokumentuje projekt GNU w formacie Texinfo – strona man bywa tylko skrótem, co sama sygnalizuje odsyłaczem „Full documentation … via info”.

## 10. pinfo

```bash
sudo dnf install pinfo
pinfo coreutils
```

W pinfo odnośniki są podświetlone, nawigacja działa strzałkami: góra/dół – między odnośnikami, prawo – wejście, lewo – powrót. Treść dokumentów jest ta sama.

## 11. type i help

```bash
type cd ls pwd history
help cd
help history
```

`cd` i `history` to polecenia wbudowane w bash (pomoc: `help`), `ls` to zwykle alias do `ls --color=auto` (a pod spodem program), `pwd` bywa jednocześnie wbudowane i dostępne jako `/usr/bin/pwd` – `type` pokazuje to, czego powłoka użyje.

## 12. --help

```bash
tar --help | less
```

Opcja rozpakowania: `-x` / `--extract`. Pomoc `--help` wystarcza, gdy pamiętasz, że opcja istnieje, a szukasz tylko litery.

## 13. Dokumentacja mc

```bash
sudo dnf install mc
man mc
ls /usr/share/doc/mc/
```

`mc` ma stronę man i katalog dokumentacji (README itd.). Pomoc wewnątrz programu: klawisz **F1**.

## 14. Pliki pakietu bez instalacji

```bash
dnf repoquery -l tree | grep /usr/share/man
```

Wynik pokaże m.in. `/usr/share/man/man1/tree.1.gz` – `repoquery -l` pyta repozytorium, więc pakiet nie musi być zainstalowany.

## 15. tldr

```bash
sudo dnf install tealdeer     # wymaga włączonego EPEL
tldr --update
tldr tar
```

`tldr` pokazuje kilka najczęstszych przykładów użycia z opisami; `man tar` – kompletny opis wszystkich opcji. Ściąga jest szybsza, gdy wiesz, *co* chcesz zrobić; man niezbędny, gdy potrzebujesz szczegółów lub rzadkiej opcji.

## 16. Dokumentacja online

Red Hat: `docs.redhat.com` (przewodniki po RHEL), Rocky Linux: `docs.rockylinux.org`, AlmaLinux: `wiki.almalinux.org`. Rocky i Alma są odbudowanymi klonami RHEL (zgodność binarna), więc procedury z dokumentacji Red Hat stosują się do nich niemal w całości.

## 17. Dobre zgłoszenie problemu

Potrzebne: (1) dystrybucja i wersja systemu (`cat /etc/os-release`), (2) dokładne polecenie, które zostało wydane, (3) pełny komunikat błędu skopiowany jako tekst, (4) co już sprawdzono i z jakim skutkiem. Zdjęcie ekranu jest złe, bo tekstu z niego nie można przeszukać, skopiować do wyszukiwarki ani zacytować w odpowiedzi – a często jest ucięty.
