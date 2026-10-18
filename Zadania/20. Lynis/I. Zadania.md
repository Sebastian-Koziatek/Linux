# Zadania – Lynis

Zadania wykonuj na swojej maszynie szkoleniowej. Pracujesz na żywym systemie – zmieniaj jedną
rzecz naraz i trzymaj otwartą zapasową sesję SSH, zanim dotkniesz konfiguracji `sshd`.

1. Zainstaluj Lynis z repozytorium EPEL i sprawdź jego wersję.
2. Uruchom pełny audyt systemu. Zapisz z podsumowania: liczbę ostrzeżeń (warnings), liczbę
   sugestii (suggestions) i wartość hardening index.
3. Odczytaj hardening index bez przewijania terminala – wprost z pliku raportu Lynisa.
4. Wybierz z raportu jedną sugestię dotyczącą SSH (test `SSH-7408`) i wyświetl jej szczegóły
   poleceniem Lynisa. Co dokładnie narzędzie proponuje zmienić?
5. Wdróż zalecenie dotyczące starzenia haseł: w `/etc/login.defs` ustaw maksymalny wiek hasła
   na 180 dni, minimalny na 1 dzień i ostrzeżenie na 7 dni przed wygaśnięciem. Następnie ustaw
   te same limity istniejącemu kontu użytkownika i zweryfikuj je.
6. Ustaw wymagania jakości hasła: minimum 12 znaków i co najmniej 3 klasy znaków. Sprawdź,
   że system odrzuca hasło `kot` przy próbie zmiany.
7. Skonfiguruj baner logowania: do `/etc/issue` i `/etc/issue.net` wpisz komunikat o dostępie
   wyłącznie dla uprawnionych. Sprawdź, które testy banerów (`BANN-…`) przestały zgłaszać sugestię.
8. Upewnij się, że usługa `auditd` jest zainstalowana, włączona i wystartowana, a jej dziennik
   przyrasta w `/var/log/audit/audit.log`.
9. Utwardź SSH zgodnie z lekcją: osobnym plikiem w `/etc/ssh/sshd_config.d/` zablokuj logowanie
   roota i ogranicz liczbę prób uwierzytelnienia do 3. **Przetestuj składnię przed restartem**
   i zaloguj się testowo z drugiego okna.
10. Uruchom audyt ponownie (bez pauz) i porównaj hardening index z wynikiem z zadania 2.
    O ile punktów wzrósł?
11. (Dla dociekliwych) Zainstaluj drugą kopię Lynisa prosto z GitHuba do `/usr/local/lynis`
    i uruchom z niej audyt. Porównaj wersje obu instalacji.

> **Wskazówka:** identyfikatory testów (np. `AUTH-9286`) znajdziesz w nawiasach kwadratowych
> w sekcji Suggestions – to po nich pytasz `lynis show details`.
