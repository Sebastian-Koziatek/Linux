![](../../../grafiki/1-1-rozwiazania.png)

# Rozwiązania – Instalacja systemu

## 1. Jądro a dystrybucja

Jądro Linux to sam „silnik” systemu: zarządza procesorem, pamięcią, dyskami i siecią. Dystrybucja to kompletny produkt: jądro + narzędzia GNU + menedżer pakietów + repozytoria + instalator + model wsparcia. Dlatego różne dystrybucje (Rocky, Ubuntu, Fedora) mogą używać bardzo podobnego jądra, a mimo to różnić się sposobem instalowania oprogramowania.

---

## 2. Rodziny dystrybucji

| Rodzina | Dystrybucje z listy |
|---|---|
| Red Hat | Rocky Linux, Fedora, AlmaLinux |
| Debian | Ubuntu, Linux Mint, Kali Linux |
| SUSE | openSUSE Leap |
| Arch | Manjaro |

---

## 3. RHEL, CentOS Stream, Rocky, Alma

RHEL – komercyjny, subskrypcja, wsparcie producenta przez 10 lat. CentOS Stream – darmowa wersja rozwojowa, z której powstaje kolejne wydanie RHEL (zmienia się częściej). Rocky Linux i AlmaLinux – darmowe odtworzenia RHEL zgodne z nim na poziomie pakietów. Na serwer produkcyjny bez budżetu: Rocky Linux lub AlmaLinux – zachowują stabilność i cykl życia RHEL bez opłat.

---

## 4. Środowiska uruchomienia

Serwer fizyczny, maszyna wirtualna i maszyna w chmurze mają własne jądro. **Kontener własnego jądra nie ma** – korzysta z jądra systemu-gospodarza, dlatego jest lekki i startuje w sekundy.

---

## 5. SWAP

SWAP warto mieć na typowych serwerach i maszynach z małą ilością RAM – chroni przed OOM killerem, który zamyka procesy po wyczerpaniu pamięci. Rezygnuje się z niego świadomie w szczególnych konfiguracjach (np. wymagania producenta aplikacji). Dla 4 GB RAM (przedział 2–8 GB) zaleca się SWAP równy ilości RAM, czyli 4 GB.

---

## 6. Dystrybucja i wersja

```bash
cat /etc/os-release
cat /etc/redhat-release
```

Pierwsze polecenie działa na każdej dystrybucji, drugie tylko w rodzinie Red Hat.

---

## 7. Jądro i podsumowanie systemu

```bash
uname -r
hostnamectl
```

`uname -r` zwraca wersję jądra (np. `5.14.0-427.13.1.el9_4.x86_64`), `hostnamectl` – nazwę komputera, system, typ obudowy, wirtualizację i architekturę.

---

## 8. Wykrycie wirtualizacji

```bash
systemd-detect-virt
```

Wynik `oracle` oznacza VirtualBox, `kvm` – KVM/Proxmox, `none` – maszynę fizyczną. Te same informacje pokazuje pole „Virtualization” w `hostnamectl`.

---

## 9. RAM i SWAP

```bash
free -h
swapon --show
```

`free -h` pokazuje pamięć i SWAP w czytelnych jednostkach; `swapon --show` – urządzenie źródłowe SWAP (po instalacji automatycznej: wolumin LVM, typ `partition`).

---

## 10. Układ dysku

```bash
lsblk
```

Przykładowy wynik po partycjonowaniu automatycznym: partycja `sda1` zamontowana jako `/boot` oraz woluminy LVM `rl-root` (katalog `/`) i `rl-swap` (na RHEL grupa nazywa się `rhel`, na AlmaLinux – `almalinux`). Na maszynie UEFI dodatkowo mała partycja `/boot/efi`.

---

## 11. Uprawnienia sudo

```bash
# sprawdzenie, czy użytkownik już jest w grupie wheel
id admin

# dodanie do grupy (wykonaj jako root albo inny administrator)
sudo usermod -aG wheel admin

# weryfikacja — po PONOWNYM zalogowaniu użytkownika
sudo whoami
```

`usermod -aG` dopisuje użytkownika do grupy bez usuwania pozostałych; członkostwo zaczyna działać od nowego logowania, a `sudo whoami` powinno zwrócić `root`.

---

## 12. Aktualizacja systemu

```bash
sudo dnf update
dnf check-update
```

`dnf update` pobiera i instaluje aktualizacje (potwierdź `y`). `dnf check-update` po udanej aktualizacji nie wypisuje żadnych pakietów i kończy się kodem 0 (gdy są zaległe aktualizacje – kodem 100).

---

## 13. needs-restarting

```bash
dnf provides needs-restarting
sudo dnf install dnf-utils
needs-restarting -r
```

Program dostarcza pakiet narzędzi `dnf-utils` (instalowalny też pod historyczną nazwą `yum-utils`). Opcja `-r` odpowiada tylko na pytanie „czy wymagany jest restart systemu” – po aktualizacji jądra zwróci, że tak.

---

## 14. Pakiet mc i strona podręcznika

```bash
sudo dnf install mc
man mc
```

W podręczniku (sekcja OPTIONS) opcja `-e` uruchamia sam wbudowany edytor: `mc -e plik` działa jak `mcedit`. Podręcznik przewijasz spacją, szukasz `/tekst`, wychodzisz klawiszem `q`.

---

## 15. Zmiana nazwy komputera

```bash
hostnamectl
sudo hostnamectl set-hostname serwer
hostnamectl
```

Zmiana jest trwała (zapisywana w `/etc/hostname`); nowy prompt zobaczysz po ponownym zalogowaniu.

---

## 16. Subskrypcje RHEL

```bash
sudo subscription-manager status
sudo subscription-manager list --consumed
```

Na RHEL polecenia pokazują stan rejestracji i wykorzystywane subskrypcje – bez rejestracji system nie pobiera pakietów z oficjalnych repozytoriów. Rocky Linux i AlmaLinux nie używają subskrypcji: ich repozytoria są publiczne i darmowe, dlatego `subscription-manager` nie jest tam potrzebny.
