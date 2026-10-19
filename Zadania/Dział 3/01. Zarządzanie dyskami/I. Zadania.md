![](../../../grafiki/3-01-zadania.png)

# Zadania – Zarządzanie dyskami

> Wszystkie zadania wykonuj na **dodatkowych dyskach** `/dev/sdb` i `/dev/sdc` maszyny szkoleniowej. Dysk `/dev/sda` to dysk systemowy – nie dotykamy go żadnym poleceniem zmieniającym.

> **Wskazówka:** przed każdym zadaniem zmieniającym dysk uruchom `lsblk` i upewnij się, że pracujesz na właściwym urządzeniu.

**1.** Wyświetl listę wszystkich dysków i partycji w formie drzewa. Które urządzenie jest dyskiem systemowym, a które dyskami ćwiczeniowymi?

**2.** Wyświetl tę samą listę razem z systemami plików i UUID. Dlaczego przy dyskach ćwiczeniowych kolumny FSTYPE i UUID są puste?

**3.** Sprawdź, jakim plikom w `/dev` odpowiadają dyski ćwiczeniowe według trwałych nazw w `/dev/disk/by-id/`.

**4.** Sprawdź, czy Twoja maszyna wystartowała w trybie UEFI czy BIOS, oraz jaki typ tablicy partycji (GPT czy MBR) ma dysk systemowy.

**5.** Jeśli Twoja maszyna wirtualna na to pozwala, dodaj w jej ustawieniach nowy dysk bez wyłączania systemu, a następnie spraw, by Linux go wykrył bez restartu. Udowodnij wykryciem wpisu w dzienniku jądra. (Jeśli nie możesz dodać dysku – wykonaj sam skan kontrolerów i sprawdź, że niczego nie ubyło.)

**6.** Na dysku `/dev/sdb` utwórz programem `fdisk` nową tablicę partycji GPT oraz dwie partycje: 2 GiB i 3 GiB. Przed zapisem wyświetl plan układu partycji.

**7.** Zmień typ drugiej partycji (`/dev/sdb2`) na **Linux LVM**. Sprawdź efekt poleceniem pokazującym nazwy typów partycji.

**8.** Usuń w `fdisk` obie partycje z `/dev/sdb` tak, by dysk znów był pusty (sama tablica GPT może zostać).

**9.** Na dysku `/dev/sdb` utwórz w programie `cfdisk` jedną partycję 1 GiB, a następnie usuń ją w tym samym programie. Zwróć uwagę, w którym momencie zmiany naprawdę trafiają na dysk.

**10.** Na dysku `/dev/sdc` utwórz programem `parted` tablicę GPT i partycję o nazwie `dane` zajmującą połowę dyska. Następnie usuń tę partycję. Czym różni się moment zapisu zmian w `parted` od `fdisk`?

**11.** Wykonaj zadanie 10 jeszcze raz, ale jednym poleceniem w trybie skryptowym `parted -s` (utworzenie tablicy i partycji; usuwanie osobno).

**12.** Wyjaśnij własnymi słowami: dlaczego na starym dysku MBR po partycjach `sda1` i `sda2` może od razu występować `sda5`? Co to mówi o rodzaju partycji `sda5`?

**13.** Wyczyść oba dyski ćwiczeniowe z partycji, a następnie zbuduj z `/dev/sdb` i `/dev/sdc` macierz **RAID 1** `/dev/md0`. Obserwuj postęp pierwszej synchronizacji.

**14.** Załóż na macierzy system plików XFS, zamontuj ją w katalogu `/dane` i utwórz tam plik `test.txt` z dowolną treścią.

**15.** Zasymuluj awarię dysku `/dev/sdc` w macierzy. Sprawdź stan macierzy i udowodnij, że plik `test.txt` jest nadal dostępny.

**16.** Usuń „uszkodzony” dysk z macierzy, dodaj go ponownie jako nowy i poczekaj na odbudowę. Sprawdź, że stan wrócił do `[UU]`.

**17.** Zapisz konfigurację macierzy tak, by po restarcie zachowała nazwę `md0`. Pokaż dopisany wiersz konfiguracji.

**18.** Posprzątaj: odmontuj `/dane`, zatrzymaj macierz i usuń z obu dysków wszystkie ślady po niej, tak by `lsblk` pokazywał dwa czyste dyski. Wyjaśnij, dlaczego samo zatrzymanie macierzy nie wystarczy.

> **Wskazówka do zadań 13–18:** stan macierzy na bieżąco śledzisz poleceniem `watch cat /proc/mdstat` (wyjście z podglądu: Ctrl+C).
