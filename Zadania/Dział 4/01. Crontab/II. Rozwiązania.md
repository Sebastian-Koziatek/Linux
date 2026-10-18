# Rozwiązania – Crontab

## 1. Stan demona

```bash
systemctl status crond
systemctl is-enabled crond
```

Na RHEL/Rocky/AlmaLinux usługa nazywa się `crond` (na Ubuntu/Debianie: `cron`); `is-enabled` potwierdza autostart.

## 2. Kopia harmonogramu

```bash
crontab -l > ~/crontab.kopia
```

Jedno pomyłkowe `crontab -r` kasuje cały harmonogram bez potwierdzenia — z kopią przywrócisz go poleceniem `crontab ~/crontab.kopia`.

## 3. Komunikat co minutę

```bash
crontab -e
```

```text
* * * * * /usr/bin/wall "Crontab pozdrawia"
```

Pięć gwiazdek oznacza „co minutę”; `wall` wypisuje komunikat na terminalach wszystkich zalogowanych.

## 4. Dowód w dzienniku

```bash
sudo journalctl -u crond --since "5 min ago"
```

Szukamy wpisów `CROND[…]: (twoj_login) CMD (/usr/bin/wall "Crontab pozdrawia")` — pojawiają się co minutę i potwierdzają, że cron zadanie uruchamia.

## 5. Harmonogramy użytkowników

```bash
crontab -l
sudo crontab -u szkolenie -l
```

`no crontab for szkolenie` oznacza po prostu, że ten użytkownik nigdy nie utworzył harmonogramu — to nie błąd.

## 6. Tłumaczenia wpisów

a) co 5 minut; b) w dni robocze (pon–pt) o 22:00; c) pierwszego i piętnastego dnia każdego miesiąca o 6:30; d) w każdą niedzielę co 4 godziny, o pełnych godzinach (0:00, 4:00, 8:00, …); e) jednorazowo po każdym starcie systemu.

## 7. Zapis w składni crona

```text
45 23 * * *        # a) codziennie o 23:45
*/30 8-16 * * 1-5  # b) co pół godziny, 8:00-16:30, pon-pt
0 5 * * 6          # c) w każdą sobotę o 5:00
0 1 1 1,4,7,10 *   # d) 1 stycznia/kwietnia/lipca/października o 1:00
```

## 8. Zadanie z przekierowaniem wyjścia

```text
30 2 * * * /usr/local/bin/kopia.sh >> /tmp/kopia.log 2>&1
```

`>>` dopisuje do pliku, a `2>&1` kieruje tam także strumień błędów — bez tego komunikaty o problemach przepadną.

## 9. Dlaczego skrypt nie działa w cronie

Po pierwsze: brak pełnej ścieżki — cron ma krótki `PATH` (zwykle `/usr/bin:/bin`) i nie zagląda do katalogu bieżącego; rozwiązanie: `/pełna/ścieżka/moj-skrypt.sh` albo linia `PATH=…` na początku crontaba. Po drugie: skrypt może polegać na środowisku z `~/.bashrc` (zmienne, aliasy), którego cron nie wczytuje; rozwiązanie: ustawić potrzebne zmienne w samym skrypcie. (Częsty trzeci powód: brak bitu wykonywalności — `chmod +x`.)

## 10. Łączenie poleceń

```text
# ';' - wykonaj po kolei niezależnie od wyniku
# '&&' - drugie tylko gdy pierwsze się powiodło
# '||' - drugie tylko gdy pierwsze zawiodło
0 3 * * * tar -czf /tmp/kopia.tar.gz /home/anna && echo "$(date) OK" >> /tmp/kopia.log || echo "$(date) BLAD" >> /tmp/kopia.log
```

Działa też potok `|` (przekazanie wyjścia dalej). Uwaga na `%` w cronie — np. w `date +\%F` wymaga ukośnika.

## 11. Crontab systemowy

```bash
cat /etc/crontab
ls -l /etc/cron.d/
cat /etc/cron.d/*
```

Wpisy systemowe mają **sześć** pól przed poleceniem — dodatkowe (szóste z kolei) to nazwa użytkownika, jako który zadanie się wykona, np. `30 2 * * * root /usr/local/sbin/kopia.sh`.

## 12. Katalogi okresowe i anacron

```bash
ls -l /etc/cron.daily /etc/cron.weekly /etc/cron.monthly
cat /etc/anacrontab
```

W katalogach leżą zwykłe skrypty wykonywalne (m.in. rotacja logów). Ich wykonania pilnuje **anacron** — jeśli maszyna była wyłączona w porze zadania, uruchomi je po starcie z opóźnieniem opisanym w `/etc/anacrontab`.

## 13. Usunięcie jednego wpisu

```bash
crontab -e     # kasujemy TYLKO linię z wall, zapisujemy
crontab -l     # kontrola
```

Nie używamy `crontab -r` — usuwa cały harmonogram, a nie jeden wpis. Alternatywa skryptowa: `crontab -l | grep -v 'wall' | crontab -`.

## 14. Timery systemd

```bash
systemctl list-timers
```

W kolumnach `NEXT`/`LEFT` widać najbliższe uruchomienie. Za zadania okresowe crona odpowiadają np. `logrotate.timer` czy `dnf-makecache.timer`; jeśli w systemie nie ma osobnego timera „daily”, codzienne skrypty obsługuje para crond + anacron.
