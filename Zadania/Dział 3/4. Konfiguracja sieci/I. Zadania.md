![](../../../grafiki/3-4-zadania.png)

# Zadania – Konfiguracja sieci

> Zadania wykonuj na maszynie szkoleniowej. Tam, gdzie pojawia się nazwa interfejsu `ens192`, podstaw nazwę swojej karty (sprawdzisz ją w zadaniu 1). Adresy dopasuj do swojej sieci – chyba że zadanie wyraźnie każe użyć konkretnego adresu.

> **Wskazówka:** jeśli pracujesz przez SSH, zadania zmieniające adres lub wyłączające interfejs (6, 10) wykonuj na konsoli maszyny – inaczej zerwiesz sobie połączenie.

**1.** Wyświetl skrócony przegląd wszystkich interfejsów sieciowych. Zapisz: jak nazywa się Twój interfejs, jaki ma stan i jaki adres IP z maską.

**2.** Na podstawie wyniku z zadania 1 odpowiedz: jaki jest adres **sieci**, w której pracuje Twoja maszyna, a jaka część adresu to „numer domu” (część hosta)? Ile maszyn zmieści się w tej sieci przy masce /24?

**3.** Wyświetl tablicę tras i wskaż adres bramy domyślnej. Wyjaśnij jednym zdaniem, do czego ta brama służy.

**4.** Sprawdź adres MAC swojego interfejsu dwoma różnymi poleceniami z rodziny `ip`.

**5.** Wyświetl tablicę sąsiadów (ARP). Co oznacza wpis łączący adres IP z adresem MAC?

**6.** Dodaj do swojego interfejsu **tymczasowy** drugi adres `192.168.77.5/24`, sprawdź, że się pojawił, a następnie go usuń. Dlaczego taka zmiana nie przetrwa restartu systemu?

**7.** Sprawdź, czy w systemie dostępne jest polecenie `ifconfig`. Jeśli nie – z jakiego pakietu można je doinstalować i jakie nowe polecenia zastępują `ifconfig -a`, `route -n` i `netstat -tulpn`?

**8.** Wyświetl listę urządzeń widzianych przez NetworkManager oraz listę profili połączeń. Czym różni się „urządzenie” od „połączenia (profilu)”?

**9.** Odczytaj z profilu swojego połączenia metodę przydzielania adresu IPv4 (`auto` czy `manual`) jednym poleceniem z `grep`.

**10.** Ustaw na swoim interfejsie **statyczną** konfigurację przez `nmcli`: obecny adres IP z maską, obecną bramę i serwery DNS `192.168.10.1` oraz `8.8.8.8` (adresy IP/bramy odczytaj wcześniej z systemu, żeby ich nie zmienić). Zastosuj profil i sprawdź wynik. Na koniec – jeśli maszyna wcześniej używała DHCP – przywróć metodę automatyczną.

**11.** Obejrzyj plik profilu swojego połączenia w `/etc/NetworkManager/system-connections/`. Wskaż sekcję i klucz, w którym zapisały się serwery DNS. Jakie uprawnienia ma ten plik i dlaczego?

**12.** Wyjaśnij, dlaczego ręczna edycja `/etc/resolv.conf` to zły pomysł, i podaj poprawny sposób zmiany serwerów DNS. Jakie polecenia trzeba wykonać po **ręcznej** edycji pliku `.nmconnection`, żeby NetworkManager ją zastosował?

**13.** Dodaj do `/etc/hosts` wpis `127.0.0.1 mojserwer` i sprawdź pingiem, że nazwa działa. Dlaczego działa, mimo że żaden serwer DNS o niej nie słyszał? Na koniec usuń wpis.

**14.** Sprawdź bieżącą nazwę komputera, zmień ją trwale na `stacja1.szkolenie.local`, zweryfikuj zmianę, a następnie przywróć poprzednią nazwę.

**15.** Przeprowadź pełną diagnostykę „od dołu do góry” swojej maszyny: (1) adres, (2) ping do bramy, (3) ping do `8.8.8.8`, (4) ping do `onet.pl`, (5) `curl -I` do dowolnej strony. Przy każdym kroku zapisz, co by oznaczało jego niepowodzenie.

**16.** Ustal adres IP domeny `www.example.com` trzema różnymi narzędziami. Następnie zapytaj o tę samą nazwę bezpośrednio serwer `8.8.8.8` i sprawdź w wyjściu, który serwer DNS odpowiedział.

**17.** Wyświetl wszystkie porty TCP i UDP, na których nasłuchuje Twoja maszyna, razem z nazwami procesów. Który proces nasłuchuje na porcie 22? Potwierdź otwartość portu 22 osobnym testem pojedynczego portu (`nc`).

**18.** Przeskanuj **własną** maszynę nmapem (`localhost`) i porównaj listę otwartych portów z wynikiem zadania 17. Dlaczego nie wolno skanować adresów, które do Ciebie nie należą?
