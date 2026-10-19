![](../../../grafiki/1-04-zadania.png)

# Zadania – Dokumentacja i pomoc

> Zadania wykonuj na maszynie szkoleniowej (Rocky/AlmaLinux 9 lub 10). Celem jest nabranie odruchu sprawdzania dokumentacji w systemie, zanim sięgniesz do internetu.

> **1.** Otwórz `man man` i odpowiedz: z ilu sekcji składa się podręcznik systemowy i co zawierają sekcje 1, 5 i 8?

> **2.** Otwórz stronę podręcznika polecenia `ls`. - Do której sekcji należy `ls`? - Korzystając z wyszukiwania w otwartej stronie (`/`), znajdź co najmniej trzy opcje służące do sortowania wyników. - Jak z poziomu otwartej strony przejść na jej koniec, a jak wrócić na początek?

> **3.** Przeczytaj SYNOPSIS strony `man cp`. Wyjaśnij, co w zapisie `cp [OPTION]... SOURCE DEST` oznaczają nawiasy kwadratowe i wielokropek. Czy `cp plik1` (bez celu) jest zgodne z tym wzorem?

> **4.** Nazwa `passwd` występuje w podręczniku więcej niż raz. - Sprawdź jednym poleceniem, w których sekcjach występuje. - Otwórz stronę o **pliku** `/etc/passwd` i odczytaj z niej, co zawiera trzecie pole wiersza.

> **5.** Nie znasz nazwy polecenia do zmiany nazwy plików. Znajdź kandydatów, przeszukując opisy stron podręcznika słowem „rename”.

> **6.** Polecenie `apropos` zwraca „nothing appropriate” na świeżym systemie. Jakim poleceniem zbudujesz indeks, żeby zaczęło działać?

> **7.** Sprawdź, gdzie fizycznie na dysku leży plik strony podręcznika `passwd` z sekcji 5.

> **8.** Otwórz dokumentację `info coreutils`, przejdź do rozdziału o poleceniu `ls` i wróć do spisu treści. - Których klawiszy użyjesz do: wejścia w odnośnik, powrotu o poziom wyżej, wyjścia z programu? - Czym różni się układ dokumentacji info od strony man?

> **9.** Sprawdź, czy polecenie `pwd` ma dokument info, i porównaj jego objętość ze stroną `man pwd`. Dlaczego narzędzia GNU mają często bogatszą dokumentację w info niż w man?

> **10.** Zainstaluj `pinfo` i otwórz w nim `pinfo coreutils`. Czym nawigacja różni się od standardowego `info`?

> **11.** Sprawdź poleceniem `type`, czym są: `cd`, `ls`, `pwd` i `history`. Dla tych, które są wbudowane w powłokę, wyświetl pomoc właściwym poleceniem.

> **12.** Wyświetl skróconą pomoc polecenia `tar` (bez otwierania strony man). Znajdź w niej opcję odpowiadającą za rozpakowanie archiwum.

> **13.** Zainstaluj pakiet `mc` (jeśli go nie masz) i sprawdź: - czy ma stronę man, - czy ma dokumentację w `/usr/share/doc/`, - jak uruchomić pomoc wewnątrz samego programu `mc`.

> **14.** Korzystając z `dnf repoquery -l`, sprawdź – bez instalowania – jakie strony podręcznika (`/usr/share/man/...`) instaluje pakiet `tree`.

> **15.** Zainstaluj klienta tldr (pakiet `tealdeer` z EPEL), zaktualizuj bazę ściąg i wyświetl ściągę dla `tar`. Czym różni się ona od `man tar` i kiedy która forma jest wygodniejsza?

> **16.** Wskaż adresy oficjalnej dokumentacji: Red Hat, Rocky Linux i AlmaLinux. Dlaczego dokumentacja Red Hat jest użyteczna także dla Rocky/Alma?

> **17.** Kolega przysłał Ci zdjęcie ekranu z błędem i pyta „co robić?”. Wymień cztery informacje, które powinien dostarczyć, żeby dało się sensownie pomóc – i wyjaśnij, czemu zdjęcie ekranu to zły format.
