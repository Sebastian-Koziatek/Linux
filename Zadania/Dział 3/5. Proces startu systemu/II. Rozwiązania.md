![](../../../grafiki/3-5-rozwiazania.png)

# Rozwiązania – Proces startu systemu

## 1. Czas startu

```bash
systemd-analyze
systemd-analyze blame | head -3
```

Pierwsze polecenie dzieli czas na jądro, initrd i przestrzeń użytkownika; `blame` pokazuje czas poszczególnych usług.

---

## 2. BIOS czy UEFI

```bash
ls /sys/firmware/efi && echo UEFI || echo BIOS
```

Katalog `/sys/firmware/efi` istnieje tylko przy starcie przez UEFI.

---

## 3. Zawartość /boot i jądro

```bash
ls /boot
uname -r
rpm -qa kernel\* | sort -V
```

Jądro to `vmlinuz-<wersja>`, initramfs to `initramfs-<wersja>.img`, konfiguracja GRUB-a w `/boot/grub2/`. `uname -r` powinno odpowiadać najnowszemu zainstalowanemu pakietowi `kernel`, chyba że po aktualizacji nie było restartu.

---

## 4. /etc/default/grub

```bash
cat /etc/default/grub
```

`GRUB_TIMEOUT` – ile sekund menu czeka na wybór; `GRUB_CMDLINE_LINUX` – parametry dopisywane do wiersza poleceń jądra w każdym wpisie (np. `crashkernel`, `rhgb quiet`).

---

## 5. Zmiana GRUB_TIMEOUT

```bash
sudo sed -i 's/^GRUB_TIMEOUT=.*/GRUB_TIMEOUT=8/' /etc/default/grub
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Na RHEL 9 generuje się zawsze do `/boot/grub2/grub.cfg` (na BIOS i UEFI). Pliku nie edytuje się ręcznie, bo jest w całości generowany – nadpisze go każda aktualizacja jądra.

---

## 6. grubby

```bash
sudo grubby --default-kernel
sudo grubby --info=ALL
```

`grubby` operuje na wpisach BLS w `/boot/loader/entries/` – po jego użyciu nie trzeba przebudowywać grub.cfg.

---

## 7. Moduły jądra

```bash
lsmod | head
lsmod | grep -i -e e1000 -e virtio
modinfo virtio_net        # lub modinfo e1000e
```

`lsmod` czyta `/proc/modules`; `modinfo` pokazuje opis, autora i parametry modułu.

---

## 8. Cel domyślny i jego skład

```bash
systemctl get-default
systemctl list-dependencies multi-user.target | head -20
```

---

## 9. set-default a isolate

`set-default` zmienia dowiązanie `default.target` – działa **od następnego startu**, trwale. `isolate` przełącza system **natychmiast** – zatrzymuje wszystko, czego nowy cel nie wymaga – ale po restarcie wraca cel domyślny.

---

## 10. Tryb ratunkowy poleceniem

```bash
sudo systemctl rescue          # z konsoli VM! przez SSH stracisz dostęp
# po podaniu hasła roota:
ip a                           # interfejsy są, ale sieć nieskonfigurowana / usług brak
ps aux | wc -l                 # garść procesów zamiast setek
systemctl default              # powrót do normalnej pracy
```

W trybie ratunkowym systemy plików z fstab są zamontowane, ale usługi i sieć nie działają.

---

## 11. Tryb ratunkowy z GRUB-a

Restart → w menu GRUB klawisz `e` → na końcu wiersza `linux` dopisać `systemd.unit=rescue.target` → Ctrl+x. Różnica: działa, zanim system w ogóle wstanie (przydatne przy zepsutym starcie) i nie wymaga działającego logowania — nadal jednak trzeba podać hasło roota. Zmiana jest jednorazowa, nic nie zapisuje się na dysku.

---

## 12. Instalacja i stan nginx

```bash
sudo dnf install nginx
sudo systemctl start nginx
systemctl status nginx
systemctl is-active nginx
ps aux | grep [n]ginx
```

---

## 13. Stop, start, autostart

```bash
sudo systemctl stop nginx
systemctl is-active nginx          # inactive
curl -s localhost || echo "nie odpowiada"
sudo systemctl enable --now nginx  # start + autostart jednym poleceniem
ls -l /etc/systemd/system/multi-user.target.wants/ | grep nginx
```

`enable` tworzy dowiązanie `nginx.service → /usr/lib/systemd/system/nginx.service` w katalogu `wants` celu multi-user.

---

## 14. Przeglądy usług

```bash
systemctl list-units --type=service
systemctl list-units --type=service --state=failed    # albo: systemctl --failed
systemctl list-unit-files --type=service
```

---

## 15. Maskowanie

```bash
sudo systemctl stop nginx
sudo systemctl mask nginx
sudo systemctl start nginx
```

```text
Failed to start nginx.service: Unit nginx.service is masked.
```

```bash
sudo systemctl unmask nginx
sudo systemctl start nginx
```

`disable` wyłącza tylko autostart – usługę nadal można uruchomić ręcznie lub przez zależność. Maska (dowiązanie do `/dev/null`) blokuje każdy start.

---

## 16. Logi nginx

```bash
journalctl -u nginx -b
journalctl -u nginx -f        # drugi terminal: curl localhost
sudo tail -f /var/log/nginx/access.log
```

Do dziennika systemd trafiają komunikaty procesu (start, błędy); log dostępu nginx pisze do własnego pliku w `/var/log/nginx/`.

---

## 17. firewalld i reguła HTTP

```bash
systemctl is-active firewalld && systemctl is-enabled firewalld
sudo systemctl stop firewalld
curl -s http://ADRES_IP_SERWERA >/dev/null && echo działa
sudo systemctl start firewalld            # przywracamy zaporę!
# zamiast wyłączania zapory – trwała reguła:
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

Wyłączanie zapory to test, nie rozwiązanie – otwiera się konkretną usługę.

---

## 18. Usługa puls

```bash
sudo tee /usr/local/bin/puls.sh > /dev/null <<'EOF'
#!/bin/bash
while true; do
echo "$(date '+%F %T') zalogowanych: $(who | wc -l)"
sleep 30
done
EOF
sudo chmod +x /usr/local/bin/puls.sh

sudo tee /etc/systemd/system/puls.service > /dev/null <<'EOF'
[Unit]
Description=Puls systemu - data i liczba zalogowanych

[Service]
Type=simple
ExecStart=/usr/local/bin/puls.sh
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now puls
journalctl -u puls -f
```

---

## 19. Test automatycznego restartu

```bash
sudo pkill -f puls.sh
sleep 7
systemctl status puls --no-pager | head -4     # Active: active (running) since … (kilka sekund)
journalctl -u puls -n 10                       # widać wpis o restarcie i nowe komunikaty
```

`Restart=on-failure` zadziałał: proces zabity sygnałem został uznany za awarię i podniesiony po `RestartSec=5`.

---

## 20. Sprzątanie i pytanie historyczne

```bash
sudo systemctl disable --now puls
sudo rm /etc/systemd/system/puls.service /usr/local/bin/puls.sh
sudo systemctl daemon-reload
```

Przed systemd autostart włączało się poleceniem `chkconfig nazwa on` (Debian: `update-rc.d`), a usługami sterowało `service nazwa start`. Dziś zastępują je `systemctl enable` i `systemctl start`.
