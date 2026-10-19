![](../../../grafiki/4-5-zadania.png)

# Zadania – Screen i tmux

> Zadania wykonuj na swojej maszynie szkoleniowej. Najlepiej otwórz do niej **dwa** połączenia SSH – łatwiej zobaczysz, że sesja żyje niezależnie od terminala.

**1.** Zainstaluj `tmux` oraz `screen` (ten drugi wymaga repozytorium EPEL). Sprawdź wersje obu programów.

**2.** Utwórz sesję tmux o nazwie `cwiczenia`. Wewnątrz uruchom polecenie, które co sekundę dopisuje linię do pliku `/tmp/tmux-test.log`:
```bash
   for i in {1..300}; do echo "linia $i"; sleep 1; done >> /tmp/tmux-test.log
``` Odłącz się od sesji skrótem klawiszowym (nie poleceniem `exit`!).

**3.** Zamknij okno terminala (albo rozłącz SSH), zaloguj się ponownie i udowodnij, że pętla nadal działa – podejrzyj przyrastający plik. Następnie wróć do sesji `cwiczenia`.

**4.** W sesji tmux podziel okno na dwa panele obok siebie. W lewym uruchom `sudo journalctl -f`, w prawym wykonaj `logger "test z tmuksa"`. Sprawdź, czy wpis pojawił się w lewym panelu, po czym zamknij prawy panel.

**5.** Wypisz wszystkie sesje tmux. Utwórz drugą sesję o nazwie `druga`, odłącz się od niej i przełącz z powrotem do `cwiczenia`, podając nazwę.

**6.** Powtórz ćwiczenie 2–3 w programie `screen`: sesja o nazwie `klasyk`, odłączenie, wylistowanie sesji, powrót. Zwróć uwagę na inny prefiks skrótów.

**7.** Zasymuluj sytuację „sesja wisi jako Attached”: podłącz się do `klasyk` z dwóch terminali naraz (w drugim użyj odpowiedniej opcji wymuszającej przejęcie sesji).

**8.** Uruchom – tym razem **bez** multipleksera – kopiowanie w tle odporne na wylogowanie: spakuj katalog `/etc` do `/tmp/etc.tar.gz` przez `nohup … &`, wyloguj się, zaloguj ponownie i sprawdź, czy plik powstał w całości. Kiedy wybierzesz tę drogę zamiast tmuksa?

**9.** Posprzątaj: zakończ wszystkie sesje tmux i screen oraz usuń pliki testowe z `/tmp`. Upewnij się, że `tmux ls` i `screen -ls` nie pokazują już niczego.

> **Wskazówka:** w tmuksie prefiksem skrótów jest `Ctrl+b`, w screenie `Ctrl+a`. Najpierw prefiks

> (wciśnij i puść), potem litera.
