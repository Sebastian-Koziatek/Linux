# Rozwiązania: Zarządzanie dyskami

> **OSTRZEŻENIE:** wszystkie polecenia zmieniające wykonujemy wyłącznie na dyskach ćwiczeniowych `/dev/sdb` i `/dev/sdc`. **Nigdy nie uruchamiaj tych poleceń na `/dev/sda`** – to dysk systemowy; utworzenie na nim tablicy partycji, macierzy albo systemu plików zniszczy system. Przed każdym poleceniem sprawdź urządzenie w `lsblk`.

### 1.

```bash
lsblk
```

Dysk systemowy to `sda` (ma partycje i punkty montowania `/`, `/boot`), dyski ćwiczeniowe to `sdb` i `sdc` (bez partycji i punktów montowania).

### 2.

```bash
lsblk -f
```

Kolumny są puste, bo na dyskach ćwiczeniowych nie ma jeszcze systemów plików – UUID powstaje dopiero przy formatowaniu (`mkfs`).

### 3.

```bash
ls -l /dev/disk/by-id/ | grep -E 'sdb|sdc'
```

Dowiązania symboliczne (model + numer seryjny dysku) wskazują na `../../sdb` i `../../sdc`.

### 4.

```bash
ls /sys/firmware/efi && echo "UEFI" || echo "BIOS"
sudo fdisk -l /dev/sda | grep -i disklabel
```

Istniejący katalog `/sys/firmware/efi` oznacza rozruch UEFI; `Disklabel type: gpt` – tablicę GPT na dysku systemowym.

### 5.

```bash
lsblk                                            # stan przed
echo "- - -" | sudo tee /sys/class/scsi_host/host*/scan
sudo dmesg | tail                                # wpis "[sdX] Attached SCSI disk"
lsblk                                            # stan po – nowy dysk na liście
```

`tee` jest konieczne, bo przekierowanie `>` wykonuje powłoka bez uprawnień sudo; alternatywą jest `sudo rescan-scsi-bus.sh` z pakietu `sg3_utils`.

### 6.

```bash
sudo fdisk /dev/sdb
# g                 – nowa tablica GPT
# n ⏎ ⏎ +2G         – partycja 1: 2 GiB
# n ⏎ ⏎ +3G         – partycja 2: 3 GiB
# p                 – plan układu (przed zapisem!)
# w                 – zapis i wyjście
lsblk /dev/sdb
```

Do chwili wpisania `w` wszystkie zmiany istnieją tylko w pamięci.

### 7.

```bash
sudo fdisk /dev/sdb
# t  →  2  →  lvm  →  w
lsblk -o NAME,SIZE,PARTTYPENAME /dev/sdb
```

Alias `lvm` odpowiada typowi GPT „Linux LVM”; `PARTTYPENAME` pokazuje nowy typ.

### 8.

```bash
sudo fdisk /dev/sdb
# d → 2,  d → 1  (usunięcie obu partycji),  w
lsblk /dev/sdb
```

Kolejność usuwania partycji nie ma znaczenia; `w` zapisuje pustą tablicę.

### 9.

```bash
sudo cfdisk /dev/sdb
# [New] → 1G → [Write] → yes → [Quit]
sudo cfdisk /dev/sdb
# zaznacz sdb1 → [Delete] → [Write] → yes → [Quit]
```

Zmiany trafiają na dysk dopiero po wybraniu `Write` i wpisaniu `yes` – samo `Quit` porzuca niezapisane operacje.

### 10.

```bash
sudo parted /dev/sdc
# (parted) mklabel gpt
# (parted) mkpart dane xfs 1MiB 50%
# (parted) print
# (parted) rm 1
# (parted) quit
```

`parted` zapisuje każde polecenie **natychmiast** – nie ma odpowiednika `q` bez zapisu, jak w `fdisk`.

### 11.

```bash
sudo parted -s /dev/sdc -- mklabel gpt mkpart dane xfs 1MiB 50%
sudo parted -s /dev/sdc rm 1
```

Opcja `-s` wyłącza pytania (tryb skryptowy), `--` pozwala bezpiecznie użyć wartości `50%`.

### 12.

W tablicy MBR numery 1–4 są zarezerwowane dla partycji podstawowych i rozszerzonej, a partycje **logiczne** (wewnątrz rozszerzonej) numeruje się zawsze od 5. `sda5` jest więc partycją logiczną, a jedna z partycji 1–4 (tu np. `sda2`) musi być rozszerzoną, która ją zawiera.

### 13.

```bash
lsblk                                            # upewnij się, że sdb i sdc są czyste
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
watch cat /proc/mdstat                           # pasek resync; wyjście Ctrl+C
```

Po zakończeniu synchronizacji stan to `[2/2] [UU]`.

### 14.

```bash
sudo mkfs.xfs /dev/md0
sudo mkdir -p /dane
sudo mount /dev/md0 /dane
echo "test macierzy" | sudo tee /dane/test.txt
```

Macierz `md0` traktujemy jak zwykły dysk: system plików + montowanie.

### 15.

```bash
sudo mdadm /dev/md0 --fail /dev/sdc
cat /proc/mdstat                                 # sdc[1](F), stan [2/1] [U_]
cat /dane/test.txt                               # plik nadal dostępny
```

Macierz jest zdegradowana, ale dane są dostępne – to istota RAID 1.

### 16.

```bash
sudo mdadm /dev/md0 --remove /dev/sdc
sudo mdadm /dev/md0 --add /dev/sdc
watch cat /proc/mdstat                           # recovery … → [2/2] [UU]
```

Po `--add` odbudowa rusza automatycznie; kolejność to zawsze fail → remove → add.

### 17.

```bash
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm.conf
tail -1 /etc/mdadm.conf
```

Wiersz `ARRAY /dev/md0 metadata=1.2 name=… UUID=…` gwarantuje stałą nazwę `md0` po restarcie (bez wpisu macierz może wstać jako `md127`).

### 18.

```bash
sudo umount /dane
sudo mdadm --stop /dev/md0
sudo mdadm --zero-superblock /dev/sdb /dev/sdc
sudo sed -i '/^ARRAY \/dev\/md0/d' /etc/mdadm.conf
lsblk
```

Samo `--stop` tylko zatrzymuje macierz – superbloki na dyskach zostają i jądro złoży ją ponownie przy starcie. Dopiero `--zero-superblock` usuwa metadane; usuwamy też wpis z `/etc/mdadm.conf` (i ewentualny wpis z `/etc/fstab`, jeśli go dodałeś).
