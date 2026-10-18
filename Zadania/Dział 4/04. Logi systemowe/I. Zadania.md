# Zadania – Logi systemowe

Zadania wykonuj na swojej maszynie szkoleniowej jako zwykły użytkownik z `sudo`.
Część A dotyczy dziennika systemd i plików w `/var/log`, część B to krótka diagnostyka
systemu – polecenia, po które sięgasz razem z logami, gdy „coś jest nie tak”.

## Część A – logi

1. Wyświetl 30 ostatnich wpisów dziennika systemd, od najnowszego.
2. Pokaż wszystkie komunikaty usługi `sshd` z bieżącego uruchomienia systemu.
3. Wypisz z dziennika tylko wpisy o priorytecie `err` i wyższym z ostatnich 24 godzin.
   Jeśli nic nie ma – to dobra wiadomość; sprawdź wtedy priorytet `warning`.
4. W jednym oknie terminala włącz śledzenie logu `sshd` na żywo. W drugim oknie (lub z innego
   komputera) spróbuj zalogować się przez SSH na nieistniejące konto `tester` i podaj dowolne
   hasło. Znajdź w pierwszym oknie wpis o tej próbie i odczytaj z niego adres IP.
5. Policz, ile nieudanych prób logowania (`Failed password`) zapisano w `/var/log/secure`.
6. Sprawdź, które polecenia były ostatnio wykonywane przez `sudo` (podpowiedź: `/var/log/secure`,
   słowo `COMMAND`).
7. Odczytaj z `/var/log/dnf.log` ostatnie wpisy, a następnie zainstaluj dowolny mały pakiet
   (np. `tree`). Znajdź w logu wpis o tej instalacji i podaj, o której godzinie się odbyła.
8. Pokaż komunikaty jądra z bieżącego rozruchu dotyczące dysków (podpowiedź: słowo `sd`
   lub `vd` w zależności od typu maszyny).
9. Sprawdź, ile miejsca zajmuje dziennik systemd i czy jest trwały (czy istnieje katalog
   `/var/log/journal`). Jeśli nie jest – włącz trwały dziennik.
10. Wypisz 5 ostatnich logowań do systemu oraz nieudane próby logowania na konsoli.
11. Sprawdź, czy rotacja logów jest aktywna (timer `logrotate`), i wypisz, jakie pliki
    `messages-*` zostały już zrotowane.

> **Wskazówka:** gdy nie wiesz, jak nazywa się jednostka systemd, wpisz `systemctl list-units --type=service | grep nazwa`.

## Część B – szybka diagnostyka

12. Sprawdź, jak długo system jest uruchomiony i jakie jest jego obciążenie.
13. Wypisz 5 procesów zużywających najwięcej pamięci RAM oraz 5 zużywających najwięcej procesora.
14. Sprawdź ilość wolnej pamięci RAM i użycie swapu.
15. Sprawdź, ile wolnego miejsca ma system plików `/` oraz czy nie kończą się i-węzły.
16. Wypisz, na jakich portach TCP i UDP nasłuchują usługi.
17. Wypisz usługi systemd, które są uruchomione, a osobno te, które zakończyły się błędem.
18. Zainstaluj `lsof` i sprawdź, które procesy mają otwarte pliki w katalogu `/var/log`.
