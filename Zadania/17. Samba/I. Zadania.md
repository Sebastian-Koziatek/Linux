# Zadania – Samba

1. Zainstaluj pakiety serwera i klienta Samby, a następnie sprawdź, w jakim pliku znajduje się główna konfiguracja i jakie sekcje zawiera on domyślnie.
2. Utwórz katalog `/srv/publiczny` i skonfiguruj w `smb.conf` udział `[publiczny]`: widoczny na liście, z prawem zapisu, dostępny dla użytkownika `anna`. Sprawdź składnię konfiguracji przed uruchomieniem usługi. Jakie polecenie to robi i co wypisuje przy poprawnym pliku?
3. Utwórz użytkownika systemowego `anna` bez prawa logowania do powłoki i dodaj go do bazy haseł Samby. Dlaczego samo konto systemowe nie wystarcza do zalogowania się do udziału?
4. Uruchom usługę serwera plików Samby i włącz ją na stałe. Sprawdź, na jakim porcie nasłuchuje.
5. Otwórz zaporę dla Samby na stałe i zweryfikuj listę usług. Jakie porty kryją się pod usługą `samba`?
6. Nadaj katalogowi `/srv/publiczny` właściwy kontekst SELinux w sposób trwały i zweryfikuj etykietę. Co by się stało, gdybyś pominął ten krok?
7. Z tego samego serwera wylistuj udziały jako `anna`, a następnie połącz się z udziałem `publiczny`, wgraj dowolny plik (`put`) i wylistuj zawartość. Sprawdź w systemie plików, jakiego właściciela ma wgrany plik.
8. Scenariusz diagnostyczny: użytkownik z Windows widzi udział, ale przy próbie zapisania pliku dostaje „odmowę dostępu”. `writable = yes` jest ustawione. Wymień w kolejności trzy miejsca, które sprawdzisz, i polecenia, których użyjesz.

> **Wskazówka:** jeśli nie masz pod ręką komputera z Windows, wszystkie testy klienta wykonasz poleceniem `smbclient` z samego serwera lub drugiej maszyny z Linuksem.
