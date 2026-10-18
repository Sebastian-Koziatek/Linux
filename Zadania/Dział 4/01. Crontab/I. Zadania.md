# Zadania – Crontab

1. Sprawdź, czy demon crona działa na Twojej maszynie i czy jest włączony na stałe (autostart).
2. Zrób kopię zapasową swojego obecnego harmonogramu do pliku `~/crontab.kopia` (nawet jeśli jest pusty). Dlaczego warto to robić przed każdą edycją?
3. Dodaj do swojego crontaba wpis, który co minutę wysyła do wszystkich zalogowanych użytkowników komunikat „Crontab pozdrawia” (polecenie `wall`). Odczekaj dwie minuty i potwierdź, że komunikat przychodzi.
4. Nie wylogowując się, sprawdź w dzienniku systemowym, że cron faktycznie uruchamia Twoje zadanie co minutę. Jakiego wpisu szukasz?
5. Wyświetl swój harmonogram oraz — jako administrator — harmonogram użytkownika `szkolenie`. Co oznacza komunikat `no crontab for szkolenie`?
6. Przetłumacz na polski następujące wpisy czasu:
   a) `*/5 * * * *`  b) `0 22 * * 1-5`  c) `30 6 1,15 * *`  d) `0 */4 * * 0`  e) `@reboot`
7. Zapisz w składni crona: a) codziennie o 23:45; b) co pół godziny w godzinach 8–16 w dni robocze; c) w każdą sobotę o 5:00; d) pierwszego dnia każdego kwartału (styczeń, kwiecień, lipiec, październik) o 1:00.
8. Dodaj wpis uruchamiający o 2:30 w nocy skrypt `/usr/local/bin/kopia.sh` tak, aby całe jego wyjście (również błędy) dopisywało się do pliku `/tmp/kopia.log`.
9. Wyjaśnij, dlaczego wpis `* * * * * moj-skrypt.sh` zwykle nie zadziała, mimo że `moj-skrypt.sh` uruchamia się z Twojego terminala bez problemu. Podaj dwie przyczyny i sposoby ich usunięcia.
10. Jakimi znakami rozdzielisz kilka poleceń w jednym wpisie crona? Pokaż różnicę między `;`, `&&` i `||` na przykładzie zadania, które tworzy archiwum i dopisuje do logu informację o sukcesie albo porażce.
11. Wyświetl zawartość systemowego pliku `/etc/crontab` i katalogu `/etc/cron.d/`. Czym różni się format tych wpisów od wpisów z `crontab -e`?
12. Sprawdź, jakie katalogi `cron.daily`, `cron.weekly` i `cron.monthly` istnieją w `/etc` i co zawierają. Kto pilnuje ich wykonania na maszynie, która nocą bywa wyłączona?
13. Usuń z crontaba wpis z zadania 3 (żeby komunikaty przestały przychodzić), ale zachowaj pozostałe wpisy. Jakiego polecenia NIE należy do tego używać i dlaczego?
14. Wyświetl listę timerów systemd aktywnych na Twojej maszynie. Znajdź timer odpowiadający za codzienne zadania i powiedz, kiedy nastąpi jego najbliższe uruchomienie.

> **Wskazówka:** do zadań 6–7 przyda się czytanie pól na głos od lewej: minuta, godzina, dzień miesiąca, miesiąc, dzień tygodnia.
