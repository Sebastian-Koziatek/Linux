![](../../../grafiki/4-04-rozwiazania.png)

# Rozwiązania – Logi systemowe

## Część A – logi

---

**1.** Ostatnie 30 wpisów od najnowszego:
```bash
sudo journalctl -n 30 -r
``` `-n` ogranicza liczbę wpisów, `-r` odwraca kolejność.

---

**2.** Komunikaty `sshd` z bieżącego rozruchu:
```bash
sudo journalctl -u sshd -b
```

---

**3.** Błędy z ostatniej doby:
```bash
sudo journalctl -p err --since "24 hours ago"
sudo journalctl -p warning --since "24 hours ago"
``` `-p err` obejmuje `err`, `crit`, `alert` i `emerg`.

---

**4.** Śledzenie na żywo i test:
```bash
# okno 1
sudo journalctl -fu sshd
# okno 2
ssh tester@localhost
``` W oknie 1 pojawi się wpis `Failed password for invalid user tester from 127.0.0.1 port … ssh2` (adres będzie inny, gdy łączysz się z innego komputera).

---

**5.** Liczba nieudanych prób:
```bash
sudo grep -c "Failed password" /var/log/secure
``` `-c` zlicza pasujące linie zamiast je wypisywać.

---

**6.** Polecenia wykonane przez `sudo`:
```bash
sudo grep "COMMAND" /var/log/secure | tail -n 20
``` Każdy wpis zawiera użytkownika, katalog roboczy i pełne polecenie.

---

**7.** Log menedżera pakietów:
```bash
sudo tail -n 20 /var/log/dnf.log
sudo dnf install tree
sudo grep -i "tree" /var/log/dnf.log | tail -n 5
``` Czas instalacji stoi na początku linii; historię transakcji pokaże też `sudo dnf history`.

---

**8.** Komunikaty jądra o dyskach:
```bash
sudo journalctl -k -b --grep "sd|vd"
``` Na maszynach wirtualnych dyski bywają `vda`, na fizycznych `sda`.

---

**9.** Rozmiar i trwałość dziennika:
```bash
sudo journalctl --disk-usage
ls -d /var/log/journal
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
``` Po restarcie journald pisze do `/var/log/journal` i historia przetrwa ponowne uruchomienie.

---

**10.** Logowania:
```bash
last -n 5
sudo lastb
``` `last` czyta `/var/log/wtmp`, `lastb` – `/var/log/btmp` (wymaga `sudo`).

---

**11.** Rotacja:
```bash
systemctl status logrotate.timer
ls -l /var/log/messages*
``` Zrotowane pliki mają w nazwie datę, np. `messages-20261012`.

---

## Część B – szybka diagnostyka

---

**12.** Czas pracy i obciążenie:
```bash
uptime
``` Trzy liczby na końcu to średnie obciążenie z 1, 5 i 15 minut.

---

**13.** Procesy wg pamięci i procesora:
```bash
ps aux --sort=-%mem | head -n 6
ps aux --sort=-%cpu | head -n 6
``` Pierwsza linia to nagłówek, dlatego `head -n 6`.

---

**14.** Pamięć i swap:
```bash
free -h
```

---

**15.** Miejsce i i-węzły na `/`:
```bash
df -h /
df -i /
``` Gdy `df -i` pokazuje 100%, nie da się tworzyć plików mimo wolnego miejsca.

---

**16.** Nasłuchujące porty:
```bash
sudo ss -tulnp
``` `-t` TCP, `-u` UDP, `-l` nasłuchujące, `-n` bez tłumaczenia nazw, `-p` proces.

---

**17.** Usługi uruchomione i z błędem:
```bash
systemctl list-units --type=service --state=running
systemctl list-units --type=service --state=failed
``` Dla usługi z błędem następny krok to `sudo journalctl -u nazwa -b`.

---

**18.** Otwarte pliki w `/var/log`:
```bash
sudo dnf install lsof
sudo lsof +D /var/log
``` Zobaczysz m.in. `rsyslogd`, `systemd-journald` i `auditd` – to one piszą do logów na bieżąco.
