# Zadania – Instalacja i zarządzanie oprogramowaniem

Zadania wykonuj na maszynie szkoleniowej (Rocky/AlmaLinux 9 lub 10) jako zwykły użytkownik z `sudo`. Zanim coś zainstalujesz, czytaj podsumowanie transakcji, które pokazuje `dnf`.

**1.** Wyjaśnij własnymi słowami, czym różni się instalowanie oprogramowania przez menedżer pakietów od pobierania instalatorów ze stron WWW (jak na Windowsie). Wymień co najmniej trzy korzyści.

**2.** Sprawdź, dokąd prowadzi polecenie `yum` w Twoim systemie. Jakie polecenie faktycznie wykonuje się po wpisaniu `yum install`?

**3.** Wyszukaj w repozytoriach pakiety `wget` oraz `mc`. Następnie – bez instalowania – wyświetl informacje o pakiecie `mc`: wersję, rozmiar i repozytorium, z którego pochodzi.

**4.** Zainstaluj pakiety `wget` i `mc` jednym poleceniem.

**5.** Wyświetl listę zainstalowanych pakietów i przefiltruj ją tak, żeby zobaczyć tylko pakiety zawierające w nazwie „openssh”.

**6.** Sprawdź, z jakiego pakietu pochodzi plik `/etc/ssh/sshd_config`.

**7.** Wyświetl listę wszystkich plików, które instaluje pakiet znaleziony w zadaniu 6, a następnie samą listę jego plików konfiguracyjnych.

> **Wskazówka:** do zadań 6–7 służy narzędzie `rpm` z opcjami z grupy `-q`.

**8.** Wyświetl listę włączonych repozytoriów. Czy repozytorium `crb` jest włączone?

**9.** Dodaj do systemu repozytorium EPEL i włącz na stałe repozytorium CRB. Sprawdź, że oba pojawiły się na liście.

**10.** Zainstaluj pakiet `htop` i sprawdź, z którego repozytorium został pobrany.

**11.** Obejrzyj plik konfiguracyjny repozytorium EPEL w `/etc/yum.repos.d/`. Znajdź w nim: identyfikator repozytorium, pole decydujące o tym, czy jest włączone, oraz informację o kluczu GPG. Co oznaczają zmienne `$releasever` i `$basearch`?

**12.** Pobierz pakiet `tree` do katalogu domowego **bez instalowania go**. Następnie – pracując na pobranym pliku – wyświetl jego metadane i listę plików, które by zainstalował.

**13.** Zainstaluj pobrany w zadaniu 12 plik `.rpm` tak, żeby ewentualne zależności dociągnęły się automatycznie. Dlaczego nie używamy do tego `rpm -ivh`?

**14.** Sprawdź, jakie aktualizacje są dostępne dla Twojego systemu (bez instalowania ich), a następnie zaktualizuj sam pakiet `bash` (jeśli ma dostępną aktualizację).

**15.** Wyświetl historię transakcji menedżera pakietów. Odszukaj numer transakcji, w której instalowałeś `htop`, i obejrzyj jej szczegóły.

**16.** Cofnij transakcję z zadania 15 (instalację `htop`). Sprawdź, że pakiet zniknął z systemu, a w historii pojawiła się nowa transakcja.

**17.** Wyczyść pamięć podręczną metadanych i zbuduj ją na nowo. Kiedy takie czyszczenie się przydaje?

**18.** Usuń pakiety `wget`, `mc` i `tree`, a następnie uruchom sprzątanie nieużywanych zależności. Przeczytaj uważnie, co `dnf` proponuje usunąć, zanim potwierdzisz.

**19.** Korzystając z `dnf repoquery`, sprawdź, jakich zależności wymaga pakiet `htop`.

**20.** Wyjaśnij, czym jest „piekło zależności”, podaj dwie typowe przyczyny jego powstania na RHEL 9/10 i wyjaśnij, dlaczego użycie `rpm --nodeps` pogarsza sytuację zamiast ją naprawiać.
