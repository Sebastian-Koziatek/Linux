![](../../../grafiki/2-01-zadania.png)

# Zadania – Praca z powłoką Bash

> Zadania są ułożone w kolejności lekcji modułu 05. Wykonuj je jako zwykły użytkownik na maszynie szkoleniowej (RHEL 9/10 lub pochodna). Rozwiązania znajdziesz w pliku [II. Rozwiązania.md](II.%20Rozwiązania.md) – zaglądaj do nich dopiero po własnej próbie.

## Podstawy pracy w terminalu (lekcja 1)

**1.** Sprawdź, jak nazywa się Twój użytkownik, jak nazywa się komputer i jaka powłoka Cię obsługuje.

**2.** Wpisz polecenie `lss` (celowo z literówką). Przeczytaj komunikat błędu i wyjaśnij własnymi słowami, kto go zgłasza i co oznacza.

**3.** Wyświetl 10 ostatnich poleceń z historii i powtórz jedno z nich, nie przepisując go ręcznie. Na koniec wyczyść ekran terminala na dwa różne sposoby.

> **Wskazówka:** historia ma numery, a strzałka w górę też się liczy.

## Poruszanie się po systemie (lekcja 2)

**4.** Sprawdź, w którym katalogu się znajdujesz, a potem przejdź kolejno: do `/var/log`, do katalogu nadrzędnego, do swojego katalogu domowego i z powrotem do poprzedniego katalogu – jednym poleceniem bez podawania ścieżki.

**5.** Wyświetl zawartość katalogu `/etc` posortowaną od najnowszych plików, z czytelnymi rozmiarami.

**6.** Wyświetl pełną zawartość swojego katalogu domowego, łącznie z plikami ukrytymi. Wyjaśnij, czym są wpisy `.` i `..` na początku listy.

**7.** Wykonaj `ls -l /etc/hostname` i opisz znaczenie każdej kolumny wyniku.

**8.** Będąc w katalogu domowym, wyświetl zawartość `/var/log` raz ścieżką bezwzględną, a raz względną.

## Operacje na plikach i katalogach (lekcja 3)

**9.** W katalogu domowym utwórz katalog `szkolenie`, a w nim – jednym poleceniem – pięć plików: `plik1` … `plik5`. Dodaj ukryty plik `.ukryty.txt`, upewnij się, że istnieje, a następnie zmień jego nazwę na `plik6`.

> **Wskazówka:** `touch` przyjmuje wiele argumentów, a nawiasy klamrowe generują listę.

**10.** Zapisz tekst `Szkolenie Linux` do pliku `plik3`, a potem dopisz do niego drugi wiersz `RHEL 9` tak, żeby pierwszy nie zginął. Wyświetl zawartość pliku.

**11.** Zapisz wynik polecenia `ls -l /etc` do pliku `spis-etc.txt` w katalogu `szkolenie`.

**12.** Utwórz katalog `/tmp/test` i skopiuj do niego całą zawartość katalogu `szkolenie`. Sprawdź wynik kopiowania.

**13.** Wyświetl z katalogu `szkolenie` tylko pliki pasujące do wzorca `plik` + jeden znak, a potem tylko pliki `plik1`, `plik3` i `plik5` – jednym poleceniem z listą znaków.

**14.** Usuń wszystkie pliki w `/tmp/test`, wróć poziom wyżej i usuń pusty katalog `test` poleceniem, które działa **tylko** na pustych katalogach. Wyjaśnij, dlaczego takie polecenie jest bezpieczniejsze niż `rm -r`.

**15.** Wyjaśnij (bez wykonywania!), co zrobiłoby polecenie `rm -rf *` uruchomione w katalogu domowym i dlaczego przed każdym `rm` ze wzorcem warto najpierw wykonać `ls` z tym samym wzorcem.

**16.** Zapisz historię swoich poleceń do pliku `historia.txt` w katalogu `szkolenie`.

## Prompt (lekcja 4)

**17.** Wyświetl obecny wzór znaku zachęty. Nazwij każdy element promptu `[anna@serwer ~]$` i powiedz, czym różni się zakończenie `$` od `#`.

**18.** Zmień prompt bieżącej sesji trzy razy: (a) z pełną ścieżką katalogu bieżącego, (b) dodatkowo z godziną, (c) w kolorze zielonym. Przetestuj, przechodząc do `/etc`, i zadbaj, żeby kolor nie „wyciekał” na wpisywane polecenia.

> **Wskazówka:** kody kolorów otaczaj sekwencjami `\[` i `\]`.

**19.** Spraw, żeby Twój ulubiony wariant promptu był ustawiany automatycznie w każdej nowej powłoce. Wczytaj zmiany bez wylogowywania i sprawdź w nowym oknie terminala.

## Konfiguracja powłoki, zmienne i aliasy (lekcje 5–6)

**20.** Utwórz zmienną `KURS` o wartości `Linux`, wyświetl ją, a następnie sprawdź, czy widzi ją powłoka potomna (`bash -c 'echo $KURS'`). Spraw, żeby ją widziała.

**21.** Wyświetl wartość zmiennej `PATH` i wyjaśnij: w jakiej kolejności powłoka przeszukuje katalogi i dlaczego własny skrypt w katalogu bieżącym trzeba uruchamiać jako `./skrypt.sh`.

**22.** Utwórz tymczasowe aliasy: `czas` (data i godzina), `dom` (przejście do katalogu domowego z wyświetleniem ścieżki) oraz `dysk` (zajętość dysków w czytelnym formacie). Przetestuj je i sprawdź ich definicje.

**23.** Alias `ll='ls -lah'` zapisz na stałe w odpowiednim pliku konfiguracyjnym, wczytaj zmiany bez wylogowania i sprawdź, że działa. Uzasadnij wybór pliku.

## Dowiązania (lekcja 7)

**24.** W katalogu domowym utwórz katalog `links`, przejdź do niego i utwórz plik `abc` z dowolną treścią. Sprawdź jego numer i-węzła, rozmiar i licznik dowiązań.

**25.** Utwórz dowiązanie twarde `def` do pliku `abc` i porównaj oba pliki poleceniem `ls -li`. Co się zgadza, a co się zmieniło? Następnie zmień uprawnienia pliku `def` na `400` i sprawdź uprawnienia `abc`. Wyjaśnij wynik.

**26.** Utwórz dowiązanie symboliczne `skrot` do pliku `abc` i obejrzyj je w `ls -li`. Potem usuń plik `abc` i sprawdź, co stało się z `def`, a co ze `skrot`. Wyjaśnij różnicę.

## Edytory vi/vim i nano (lekcje 8–9)

**27.** Utwórz plik `temp.txt` w edytorze `vim`: wpisz do niego wiersz `Szkolenie Linux`, zapisz i wyjdź. Następnie otwórz go ponownie i dopisz na końcu wiersza tekst ` jest proste`, używając polecenia trybu normalnego, które od razu przeskakuje na koniec wiersza i włącza wstawianie. Tym razem wyjdź **bez zapisywania**.

**28.** Pobierz „Pana Tadeusza” poleceniem `wget https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt`, otwórz plik w `vim` i: przejdź na koniec pliku, wróć na początek, wyszukaj słowo `Tadeusz` i przejdź przez trzy kolejne wystąpienia. Wyjdź z edytora.

**29.** Otwórz `pan-tadeusz.txt` w `nano`, wyszukaj frazę `Zosia` i przejdź do następnego wystąpienia, po czym wyjdź bez zapisywania. Następnie otwórz `temp.txt` w `nano`, usuń cały wiersz jednym skrótem, wpisz nowy tekst `Używam edytora nano`, zapisz i wyjdź. Sprawdź zawartość pliku.

**30.** Na koniec posprzątaj: usuń katalogi `szkolenie` i `links` oraz pliki `temp.txt` i `pan-tadeusz.txt`. Zanim naciśniesz Enter przy `rm -r`, wykonaj kontrolne `ls`.
