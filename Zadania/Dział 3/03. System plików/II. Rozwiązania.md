![](../../../grafiki/3-03-rozwiazania.png)

# Rozwiązania – System plików

## 1. Przegląd urządzeń

```bash
lsblk -f
```

Partycje bez wartości w kolumnie `FSTYPE` nie mają systemu plików – powinny to być `sdb1` i `sdb2`.

---

## 2. XFS na /dev/sdb1

```bash
sudo mkfs.xfs -L dane /dev/sdb1
```

Opcja `-L` nadaje etykietę; jeśli partycja miała już system plików, trzeba dodać `-f`.

---

## 3. ext4 na /dev/sdb2

```bash
sudo mkfs.ext4 -L archiwum /dev/sdb2
```

---

## 4. Odczyt UUID

```bash
sudo blkid /dev/sdb1 /dev/sdb2
lsblk -f /dev/sdb
```

Oba polecenia pokazują UUID; `blkid` dodatkowo PARTUUID i typ.

---

## 5. Montowanie po etykiecie i UUID

```bash
sudo mkdir -p /mnt/dane /mnt/archiwum
sudo mount LABEL=dane /mnt/dane
sudo mount UUID=$(sudo blkid -s UUID -o value /dev/sdb2) /mnt/archiwum
findmnt /mnt/dane /mnt/archiwum
```

Etykieta i UUID są odporne na zmianę nazwy urządzenia (`sdb` → `sdc`).

---

## 6. Miejsce i i-węzły

```bash
df -h /mnt/dane
df -i /mnt/dane
```

`df -h` pokazuje bloki, `df -i` i-węzły – oba zasoby mogą się skończyć niezależnie.

---

## 7. Rozmiar katalogu

```bash
mkdir -p /mnt/dane/projekty    # jeśli brak praw: sudo i chown
dd if=/dev/zero of=/mnt/dane/projekty/plik1 bs=1M count=50
sudo du -sh /mnt/dane/projekty
```

`du -s` sumuje, `-h` podaje czytelne jednostki.

---

## 8. „Target is busy”

```bash
cd /mnt/archiwum
sudo umount /mnt/archiwum          # błąd: target is busy
sudo fuser -vm /mnt/archiwum       # pokaże nasz proces bash (dostęp „..c..” = bieżący katalog)
cd ~                               # wychodzimy z katalogu
sudo umount /mnt/archiwum          # teraz się uda
```

Odmontowanie wymaga, by żaden proces nie używał systemu plików – także jako bieżącego katalogu.

---

## 9. e2fsck na ext4

```bash
sudo umount /mnt/archiwum 2>/dev/null
sudo e2fsck -f /dev/sdb2
```

Na zamontowanym systemie plików `fsck` mógłby naprawiać struktury, które jądro właśnie zmienia – to prosta droga do uszkodzenia danych.

---

## 10. Sprawdzenie XFS bez zmian

```bash
sudo umount /mnt/dane 2>/dev/null
sudo xfs_repair -n /dev/sdb1
```

`-n` (no modify) tylko raportuje problemy. Pamiętaj: `fsck.xfs` nic nie robi – dla XFS zawsze `xfs_repair`.

---

## 11. Zmiana etykiet

```bash
# ext4 – można nawet na zamontowanym
sudo tune2fs -L kopie /dev/sdb2        # albo: sudo e2label /dev/sdb2 kopie
# XFS – wyłącznie na ODMONTOWANYM systemie plików
sudo umount /mnt/dane 2>/dev/null
sudo xfs_admin -L kopie-xfs /dev/sdb1
sudo xfs_admin -l /dev/sdb1            # kontrola
```

---

## 12. Remount w tryb tylko do odczytu

```bash
sudo mount LABEL=kopie-xfs /mnt/dane 2>/dev/null || sudo mount /dev/sdb1 /mnt/dane
sudo mount -o remount,ro /mnt/dane
sudo touch /mnt/dane/test              # błąd: Read-only file system
sudo mount -o remount,rw /mnt/dane
```

`remount` zmienia opcje bez przerywania montowania.

---

## 13. Parametry systemów plików

```bash
sudo tune2fs -l /dev/sdb2 | grep -E "Block size|Inode count|Filesystem state"
xfs_info /mnt/dane
```

W `tune2fs -l`: `Block size: 4096`, `Inode count`, `Filesystem state: clean`. W `xfs_info` wielkość bloku to `bsize`, liczba bloków `blocks`; XFS tworzy i-węzły dynamicznie.

---

## 14. Wpis w fstab

```bash
sudo cp /etc/fstab /etc/fstab.bak
echo "UUID=$(sudo blkid -s UUID -o value /dev/sdb1) /mnt/dane xfs defaults,nofail 0 0" | sudo tee -a /etc/fstab
sudo mount -a
sudo findmnt --verify
sudo systemctl daemon-reload
```

`mount -a` montuje wpisy z fstab bez restartu, `findmnt --verify` sprawdza składnię. `nofail` sprawia, że brak dysku nie zatrzyma startu systemu w trybie awaryjnym.

---

## 15. Symulacja literówki

```bash
sudo vim /etc/fstab        # zmień jedną cyfrę UUID w swoim wpisie
sudo findmnt --verify
```

```text
/mnt/dane
   [E] unreachable source: UUID=3f1c7a2e-…: No such file or directory
```

Weryfikator wskazuje nieistniejące źródło. Przywróć poprawny UUID i ponownie uruchom `findmnt --verify` aż do `Success`.

---

## 16. Montowanie ISO

```bash
sudo mkdir -p /mnt/iso
sudo mount -o loop,ro /root/obraz.iso /mnt/iso
ls /mnt/iso
sudo umount /mnt/iso
```

Opcja `loop` tworzy urządzenie pętli z pliku; ISO montuje się zawsze tylko do odczytu.

---

## 17. Drzewo katalogów

```bash
ls /etc/ssh/sshd_config        # a) konfiguracja: /etc
journalctl -u sshd -n 5        # b) logi: dziennik systemd (ewentualnie /var/log/secure)
which sshd || ls /usr/sbin/sshd  # c) program: /usr/sbin
```

d) Własne skrypty administracyjne: `/usr/local/bin` – katalog poza kontrolą menedżera pakietów, obecny w `PATH`.

---

## 18. Sprzątanie

```bash
sudo umount /mnt/dane /mnt/archiwum 2>/dev/null
sudo vim /etc/fstab            # usuń swój wiersz (albo: sudo cp /etc/fstab.bak /etc/fstab)
sudo findmnt --verify
sudo systemctl daemon-reload
```

Po usunięciu wpisu weryfikacja ma zgłosić `Success, no errors or warnings detected`.
