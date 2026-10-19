![](../../../grafiki/2-2-zadania.png)

# Zadania – Zarządzanie plikami i katalogami

> Pracuj jako zwykły użytkownik z dostępem do `sudo`. Zadania 1–6 dotyczą uprawnień, 7–12 wyszukiwania, 13–18 przeglądania i potoków, 19–21 edycji strumieniowej `sed`.

## Uprawnienia

**1.** Utwórz w katalogu domowym plik `notatki.txt` i katalog `projekt`. Wyświetl ich uprawnienia tak, aby dla katalogu zobaczyć wiersz samego katalogu, a nie jego zawartość.

**2.** Odczytaj wiersz `ls -l` pliku `notatki.txt` na głos: kto jest właścicielem, jaka jest grupa i co wolno każdej z trzech kategorii? Zapisz te same uprawnienia jedną liczbą ósemkową.

**3.** Ustaw plikowi `notatki.txt` uprawnienia: właściciel czyta i pisze, grupa tylko czyta, pozostali nic. Zrób to raz zapisem ósemkowym, a raz symbolicznym.

**4.** Odbierz katalogowi `projekt` prawo `x` dla siebie i spróbuj do niego wejść (`cd`). Co się stało i dlaczego? Przywróć uprawnienie.

**5.** Utwórz plik `skrypt.sh` z treścią `echo "Działam!"` i spraw, żeby dało się go uruchomić poleceniem `./skrypt.sh`.

**6.** Sprawdź swoją maskę `umask`, a następnie w tej samej sesji zmień ją tak, by nowe pliki były całkowicie prywatne. Utwórz nowy plik i udowodnij poleceniem `ls -l`, że maska zadziałała.

> **Wskazówka:** nowy plik dostaje `666` minus maska, nowy katalog `777` minus maska.

**7.** Wyjaśnij: dlaczego w katalogu `/tmp` każdy może tworzyć pliki, ale nie może usuwać cudzych, skoro uprawnienia to `rwxrwxrwt`? Jak nazywa się ten mechanizm?

## Wyszukiwanie

**8.** Znajdź w swoim katalogu domowym wszystkie pliki z rozszerzeniem `.txt`.

**9.** Znajdź w katalogu `/etc` wszystkie pliki o nazwie zawierającej `host`, nie rozróżniając wielkości liter i bez komunikatów o braku dostępu.

**10.** Znajdź w katalogu `/var/log` pliki większe niż 1 MB oraz – osobnym poleceniem – pliki zmodyfikowane w ciągu ostatniej doby.

**11.** Znajdź wszystkie pliki należące do Twojego użytkownika w `/home` oraz wszystkie katalogi o nazwie `ssh` w całym systemie.

**12.** Utwórz katalog `~/smieci` z trzema plikami `*.tmp`. Jednym poleceniem `find` znajdź te pliki i je usuń – ale najpierw pokaż polecenie, którym sprawdzisz listę przed usunięciem.

**13.** Zainstaluj pakiet z poleceniem `locate`, zbuduj bazę i znajdź w niej plik `sshd_config`. Następnie utwórz nowy plik `~/nowy-plik-locate.txt` i wyjaśnij, dlaczego `locate` go nie widzi. Co zrobić, żeby zobaczył?

## Przeglądanie i potoki

**14.** Wyświetl: pierwsze 5 wierszy pliku `/etc/passwd`, ostatnie 3 wiersze oraz cały plik z numerami wierszy.

**15.** Otwórz `/etc/services` w `less`: znajdź w nim słowo `http`, przejdź do końca pliku, wróć na początek i wyjdź. Wypisz użyte klawisze.

**16.** Obserwuj dziennik `/var/log/messages` na żywo (`tail -f`), a w drugim terminalu wygeneruj wpis poleceniem `logger "test szkoleniowy"`. Przerwij obserwację.

**17.** Jednym potokiem policz, ile kont w `/etc/passwd` ma powłokę `/sbin/nologin`.

**18.** Jednym potokiem wypisz posortowaną alfabetycznie listę samych nazw kont (pierwsze pole `/etc/passwd`) i zapisz ją do pliku `~/konta.txt`.

> **Wskazówka:** przyda się `cut -d: -f1`.

## sed

**19.** Utwórz plik `~/test-sed.txt` z trzema wierszami zawierającymi słowo `kot`. Wyświetl plik z zamianą `kot` → `pies` we wszystkich wystąpieniach, nie zmieniając pliku. Potem wykonaj tę samą zamianę w pliku, zostawiając kopię zapasową.

**20.** Skopiuj `/etc/ssh/sshd_config` do katalogu domowego i wyświetl go bez wierszy komentarza i bez wierszy pustych.

**21.** W kopii `~/sshd_config` ustaw opcję `MaxAuthTries` na wartość `3` tak, aby polecenie zadziałało niezależnie od tego, czy wiersz jest zakomentowany (`#MaxAuthTries 6`), czy nie. Najpierw pokaż podgląd, potem zapisz z kopią.
