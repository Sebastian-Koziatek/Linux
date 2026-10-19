![](../../../grafiki/3-3-zadania.png)

# Zadania – System plików

> Ćwiczenia wykonuj na dodatkowym dysku `/dev/sdb` maszyny szkoleniowej. Jeśli nie ma na nim partycji, załóż `/dev/sdb1` (ok. 2 GB) i `/dev/sdb2` (ok. 1 GB) tak, jak w module o zarządzaniu dyskami.

> **Wskazówka:** przed każdym `mkfs` sprawdź `lsblk -f`, czy formatujesz właściwą partycję.

**1.** Wyświetl wszystkie urządzenia blokowe wraz z typem systemu plików, etykietą, UUID i punktem montowania. Które partycje nie mają jeszcze systemu plików?

**2.** Utwórz na `/dev/sdb1` system plików **XFS** z etykietą `dane`.

**3.** Utwórz na `/dev/sdb2` system plików **ext4** z etykietą `archiwum`.

**4.** Odczytaj UUID obu nowych systemów plików dwoma różnymi poleceniami.

**5.** Utwórz katalogi `/mnt/dane` i `/mnt/archiwum`, a następnie zamontuj `/dev/sdb1` w pierwszym z nich **po etykiecie**, a `/dev/sdb2` w drugim **po UUID**.

**6.** Sprawdź, ile wolnego miejsca i ile wolnych i-węzłów ma system plików zamontowany w `/mnt/dane`.

**7.** Utwórz w `/mnt/dane` katalog `projekty` z kilkoma plikami (np. `touch`, `dd`), po czym sprawdź poleceniem `du`, ile ten katalog zajmuje.

**8.** Przejdź do katalogu `/mnt/archiwum` w jednej sesji i spróbuj odmontować go w drugiej (albo w tej samej). Wyjaśnij komunikat błędu, znajdź winowajcę poleceniem `fuser` i skutecznie odmontuj.

**9.** Sprawdź spójność odmontowanego systemu plików ext4 na `/dev/sdb2` z wymuszeniem pełnego sprawdzenia. Dlaczego tego samego nie robi się na zamontowanej partycji?

**10.** Sprawdź system plików XFS na `/dev/sdb1` w trybie „tylko sprawdź, nic nie zmieniaj”.

**11.** Zmień etykietę systemu plików na `/dev/sdb2` z `archiwum` na `kopie` bez formatowania. Zrób to samo ćwiczenie dla `/dev/sdb1` (XFS) – jakie polecenie i jaki warunek musi być spełniony?

**12.** Przełącz zamontowany system plików `/mnt/dane` w tryb tylko do odczytu bez odmontowywania, spróbuj utworzyć w nim plik, po czym przywróć tryb zapisu.

**13.** Wyświetl parametry superbloku systemu plików ext4 (`/dev/sdb2`) i odczytaj z nich: wielkość bloku, liczbę i-węzłów i stan systemu plików. Dla XFS (`/dev/sdb1`) wyświetl analogiczne informacje, gdy jest zamontowany.

**14.** Dopisz do `/etc/fstab` trwałe montowanie `/dev/sdb1` w `/mnt/dane` po **UUID**, z opcjami `defaults,nofail`. Przetestuj wpis **bez restartu** dwoma poleceniami i wyjaśnij, po co jest `nofail`.

**15.** Zasymuluj literówkę: zmień w swoim nowym wpisie fstab jedną cyfrę UUID, uruchom polecenie weryfikujące fstab i odczytaj komunikat. Przywróć poprawny UUID. (Nie restartuj z błędnym wpisem!)

**16.** Pobierz lub wskaż dowolny obraz ISO (na maszynie szkoleniowej jest w `/root` lub pobierz mały obraz sieciowy) i zamontuj go w `/mnt/iso` w trybie tylko do odczytu. Wyświetl jego zawartość i odmontuj.

**17.** Korzystając z wiedzy o drzewie katalogów, odpowiedz (możesz sprawdzać w systemie): a) gdzie leży konfiguracja usługi `sshd`, b) gdzie jej logi, c) gdzie plik wykonywalny, d) w którym katalogu powinien wylądować Twój własny skrypt administracyjny?

**18.** Na końcu posprzątaj: odmontuj oba systemy plików, usuń swój wpis z `/etc/fstab` (zostaw plik w stanie sprzed ćwiczeń) i zweryfikuj plik poleceniem `findmnt --verify`.
