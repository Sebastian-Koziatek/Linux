# Moduł 08. Zdalna administracja – zadania

Wszystkie zadania wykonasz na jednej maszynie szkoleniowej: serwer SSH działa lokalnie,
a „zdalne” połączenie nawiązujesz do samego siebie (`ssh anna@localhost`). Tam, gdzie w zadaniu
występuje użytkownik `anna`, użyj swojego konta szkoleniowego.

> **Wskazówka:** przy zadaniach zmieniających konfigurację serwera (10–14) miej zawsze otwarte
> drugie okno terminala z działającą sesją – tak jak prawdziwy administrator.

1. Sprawdź, czy serwer SSH jest uruchomiony i czy wstaje automatycznie po restarcie systemu.
   Zapisz, jakiej usługi dotyczy pytanie i jakim poleceniem to sprawdziłeś.

2. Połącz się przez SSH z własną maszyną jako Twój użytkownik (`ssh anna@localhost`).
   Przeczytaj uważnie pytanie o odcisk klucza serwera i odpowiedz na nie poprawnie.
   Po zalogowaniu sprawdź poleceniami `hostname` i `whoami`, gdzie jesteś i kim jesteś,
   a następnie zakończ sesję.

3. Obejrzyj zawartość pliku `~/.ssh/known_hosts`. Wyjaśnij własnymi słowami: co zawiera ten
   plik i przed czym Cię chroni?

4. Usuń z `known_hosts` zapamiętany odcisk hosta `localhost` jednym poleceniem (bez edytora),
   a potem połącz się ponownie i zaobserwuj, co się zmieniło.

5. Wykonaj na „zdalnej” maszynie pojedyncze polecenie bez otwierania powłoki: sprawdź przez SSH,
   ile jest wolnego miejsca na dysku (`df -h /`), tak aby wynik pojawił się w Twoim lokalnym
   terminalu, a sesja od razu się zakończyła.

6. Utwórz plik `~/.ssh/config` ze skrótem o nazwie `ja`, który łączy się z `localhost` jako Twój
   użytkownik. Nadaj plikowi poprawne uprawnienia i sprawdź, że `ssh ja` działa.

7. Uruchom połączenie w trybie diagnostycznym (`ssh -v ja`) i znajdź w wyjściu trzy informacje:
   z jakiego pliku konfiguracyjnego skorzystał klient, z jakim portem się łączył i jakie metody
   uwierzytelnienia zaproponował serwer.

8. Wygeneruj parę kluczy SSH typu Ed25519 z komentarzem zawierającym Twoje imię. Obejrzyj oba
   pliki w `~/.ssh/` i odpowiedz: który z nich wolno wysłać koledze, a którego nie wolno nikomu
   przekazywać?

9. Wgraj swój klucz publiczny na konto `anna@localhost` poleceniem `ssh-copy-id`, a następnie
   zaloguj się i upewnij, że serwer nie pyta już o hasło konta. Sprawdź też zawartość
   i uprawnienia pliku `~/.ssh/authorized_keys` oraz katalogu `~/.ssh`.

10. Celowo popsuj uprawnienia: nadaj plikowi `~/.ssh/authorized_keys` prawa `644`, a katalogowi
    `~/.ssh` prawa `755`. Czy logowanie kluczem nadal działa? Przywróć poprawne uprawnienia.
    (Uwaga: na maszynie szkoleniowej z domyślną konfiguracją `StrictModes` logowanie kluczem
    powinno przestać działać dopiero przy prawach zapisu dla grupy/innych, np. `775` na katalogu
    domowym – sprawdź i opisz, co zaobserwowałeś.)

11. Utwórz w katalogu `/etc/ssh/sshd_config.d/` plik konfiguracyjny, który: zabrania logowania
    na konto `root`, ogranicza liczbę prób uwierzytelnienia do 3 i pozwala logować się tylko
    Twojemu użytkownikowi. Sprawdź składnię konfiguracji i przeładuj usługę bez zrywania sesji.
    Zweryfikuj w drugim oknie, że nadal możesz się zalogować.

12. Sprawdź efektywną (działającą) wartość opcji `permitrootlogin` i `maxauthtries` jednym
    poleceniem po stronie serwera.

13. Dodaj baner logowania: utwórz plik `/etc/issue.net` z jednym zdaniem ostrzeżenia i włącz go
    w konfiguracji `sshd`. Sprawdź, że tekst pojawia się **przed** pytaniem o uwierzytelnienie.

14. Przenieś serwer SSH na port 2222: wykonaj wszystkie trzy wymagane kroki (zapora, SELinux,
    konfiguracja) we właściwej kolejności, połącz się na nowy port, a następnie przywróć port 22
    (cofnij wszystkie trzy zmiany).

15. Utwórz katalog `~/cwiczenia-scp` z trzema plikami tekstowymi. Skopiuj: (a) jeden plik do
    `/tmp` przez `scp` używając składni zdalnej (`anna@localhost:`), (b) cały katalog przez
    `scp -r`, (c) ten sam katalog przez `rsync -avz` do `~/kopia/`. Uruchom `rsync` drugi raz
    i wyjaśnij, dlaczego tym razem nic nie przesłał.

16. W sesji `sftp` z `localhost`: wyświetl zdalny i lokalny katalog roboczy, pobierz jeden plik
    poleceniem `get` i wyślij inny poleceniem `put`, po czym zakończ sesję.

17. Zmodyfikuj jeden plik w `~/cwiczenia-scp`, usuń inny, a następnie zsynchronizuj katalog do
    `~/kopia/` tak, aby kopia była wiernym lustrem źródła (plik usunięty ze źródła ma zniknąć
    także z kopii). Najpierw wykonaj próbę „na sucho” i przeczytaj, co zostanie zrobione.

18. (Dla chętnych) Wyjaśnij, w jakiej sytuacji zamiast SSH użyjesz xrdp, a w jakiej VNC, i dlaczego
    portu VNC (5901) nie należy wystawiać do internetu. Jakie polecenie tworzy bezpieczny tunel
    SSH dla VNC?
