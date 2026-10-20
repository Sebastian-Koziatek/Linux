# Administracja systemem Linux I — materiały szkoleniowe

Materiały do pięciodniowego szkolenia **„Administracja systemem Linux I”** prowadzonego w formie
warsztatowej. Napisane z myślą o osobach, które **dopiero zaczynają pracę z Linuksem** — administratorach
Windows, testerach, programistach, analitykach. Nie zakładamy żadnej wcześniejszej znajomości systemu:
zaczynamy od instalacji, kończymy na samodzielnej konfiguracji dysków, sieci, kont i zapory.

Systemem referencyjnym jest rodzina **Red Hat Enterprise Linux 9/10** (Rocky Linux, AlmaLinux,
CentOS Stream). Tam, gdzie Ubuntu/Debian robi coś inaczej, znajdziesz ramkę *Na Ubuntu/Debianie*.

## Jak czytać

Każda lekcja ma ten sam układ: wyjaśnienie, **jak to działa** → **W praktyce** (polecenia
krok po kroku z przykładowym wynikiem) → **Najczęstsze błędy i pułapki** → **Podsumowanie** ze ściągą.
W katalogu [Zadania](Zadania/) czekają
ćwiczenia z rozwiązaniami.

Materiały czyta się wprost na GitHubie. Do pracy offline polecamy [Obsidian](https://obsidian.md/) —
otwórz katalog repozytorium jako skarbiec (vault).

## Program

### Dział 1 — Wprowadzenie do systemu

| Moduł | Zakres |
|---|---|
| [01. Instalacja systemu](Dzia%C5%82%201%20-%20Wprowadzenie%20do%20systemu/1.%20Instalacja%20systemu/1.%20Czym%20jest%20Linux%20i%20sk%C4%85d%20si%C4%99%20wzi%C4%85%C5%82.md) | czym jest Linux (i dlaczego nie jest Uniksem), dystrybucje i ich rodziny, model wydań i cykl życia, rodzina Red Hat, nośniki, rodzaj i wersja systemu, maszyna wirtualna, instalacja krok po kroku |
| [02. Środowiska graficzne](Dzia%C5%82%201%20-%20Wprowadzenie%20do%20systemu/2.%20%C5%9Arodowiska%20graficzne/1.%20Czym%20jest%20%C5%9Brodowisko%20graficzne.md) | GNOME, KDE Plasma, Xfce, Cinnamon, MATE; instalacja pulpitu na serwerze i kiedy to ma sens |
| [03. Instalacja i zarządzanie oprogramowaniem](Dzia%C5%82%201%20-%20Wprowadzenie%20do%20systemu/3.%20Instalacja%20i%20zarz%C4%85dzanie%20oprogramowaniem/1.%20Jak%20dzia%C5%82a%20mened%C5%BCer%20pakiet%C3%B3w.md) | menedżer pakietów, `dnf`, repozytoria, pakiety RPM, możliwości zaawansowane `dnf`, inne dystrybucje, piekło zależności |
| [04. Dokumentacja i pomoc](Dzia%C5%82%201%20-%20Wprowadzenie%20do%20systemu/4.%20Dokumentacja%20i%20pomoc/1.%20Podr%C4%99cznik%20systemowy%20man.md) | `man`, `info`, pomoc wbudowana w programy, gdzie szukać odpowiedzi |

### Dział 2 — Podstawy pracy z systemem Linux

| Moduł | Zakres |
|---|---|
| [01. Praca z powłoką Bash](Dzia%C5%82%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/1.%20Praca%20z%20pow%C5%82ok%C4%85%20Bash/1.%20Czym%20jest%20pow%C5%82oka%20i%20terminal.md) | terminal i powłoka, poruszanie się po systemie, struktura katalogów (FHS), pliki i katalogi, vi/vim, nano, prompt, konfiguracja powłoki, zmienne i aliasy, dowiązania |
| [02. Zarządzanie plikami i katalogami](Dzia%C5%82%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/2.%20Zarz%C4%85dzanie%20plikami%20i%20katalogami/1.%20Uprawnienia%20do%20plik%C3%B3w%20i%20katalog%C3%B3w.md) | uprawnienia (`chmod`, `chown`), wyszukiwanie (`find`, `locate`), przeglądanie i potoki (`cat`, `less`, `tail`, `grep`) |
| [03. Użytkownicy i grupy](Dzia%C5%82%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/3.%20U%C5%BCytkownicy%20i%20grupy/1.%20Konto%20root%2C%20sudo%20i%20su.md) | root, `sudo`, `su`, konta i grupy lokalne, pliki konfiguracyjne kont |
| [04. Zdalna administracja](Dzia%C5%82%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/4.%20Zdalna%20administracja/1.%20Czym%20jest%20SSH.md) | SSH: serwer, klient, klucze, zdalne polecenia i kopiowanie plików, pulpit zdalny |

### Dział 3 — Zarządzanie systemem Linux

| Moduł | Zakres |
|---|---|
| [01. Zarządzanie dyskami](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/1.%20Zarz%C4%85dzanie%20dyskami/1.%20Dyski%20w%20Linuksie%20%E2%80%93%20katalog%20dev%20i%20nazwy%20urz%C4%85dze%C5%84.md) | urządzenia w `/dev`, wykrywanie dysków, MBR i GPT, typy partycji, `fdisk`, `cfdisk`, `parted`, `gparted` |
| [02. RAID](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/2.%20RAID/1.%20RAID%20%E2%80%93%20po%20co%20%C5%82%C4%85czy%C4%87%20dyski.md) | po co łączyć dyski, RAID 0, 1, 2, 3, 4, 5, 6, RAID 0+1 i 1+0, RAID programowy (`mdadm`) |
| [03. Woluminy logiczne LVM](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/3.%20Woluminy%20logiczne%20LVM/1.%20Idea%20wolumin%C3%B3w%20logicznych.md) | idea LVM, tworzenie i powiększanie woluminów, LVM a RAID |
| [04. System plików](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/4.%20System%20plik%C3%B3w/1.%20Czym%20jest%20system%20plik%C3%B3w.md) | budowa systemu plików, ext2/3/4, XFS, Btrfs i ZFS, montowanie i naprawa, `fstab` |
| [05. Konfiguracja sieci](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/5.%20Konfiguracja%20sieci/1.%20Podstawy%20sieci%20dla%20administratora.md) | podstawy sieci, `ip`/`ifconfig`/`route`, NetworkManager (`nmcli`, `nmtui`, GUI), pliki konfiguracyjne, diagnostyka |
| [06. Proces startu systemu](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/6.%20Proces%20startu%20systemu/1.%20Etapy%20startu%20systemu.md) | etapy startu, GRUB2, poziomy startowe i targety, demony i `systemctl`, własna usługa, init a systemd |
| [07. Zabezpieczenia sieciowe](Dzia%C5%82%203%20-%20Zarz%C4%85dzanie%20systemem%20Linux/7.%20Zabezpieczenia%20sieciowe/1.%20Czym%20jest%20zapora%20sieciowa.md) | zapora sieciowa, `iptables`, `firewalld`, zabezpieczenia na poziomie jądra (`sysctl`) |

### Dział 4 — Tematy dodatkowe

Materiał poza programem podstawowym — dla chętnych i na pytania z sali.

| Moduł | Zakres |
|---|---|
| [01. Crontab](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/1.%20Crontab/1.%20Harmonogram%20zada%C5%84%20%E2%80%93%20cron%20i%20crontab.md) | harmonogram zadań, składnia czasu, timery systemd |
| [02. SELinux](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/2.%20SELinux/1.%20Czym%20jest%20SELinux.md) | czym jest SELinux, tryby pracy, diagnoza i naprawa typowych blokad |
| [03. Samba](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/3.%20Samba/1.%20Udost%C4%99pnianie%20plik%C3%B3w%20dla%20Windows%20%E2%80%93%20Samba.md) | udostępnianie plików dla Windows |
| [04. Logi systemowe](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/4.%20Logi%20systemowe/1.%20Gdzie%20szuka%C4%87%20log%C3%B3w.md) | `journalctl`, rsyslog, czytanie logów w praktyce |
| [05. Screen i tmux](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/5.%20Screen%20i%20tmux/1.%20Sesje%20terminala%20%E2%80%93%20screen%20i%20tmux.md) | sesje terminala odporne na zerwane połączenie |
| [06. Lynis](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/6.%20Lynis/1.%20Audyt%20bezpiecze%C5%84stwa%20z%20Lynis.md) | audyt bezpieczeństwa i utwardzanie systemu |
| [07. nmap](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/7.%20nmap/1.%20nmap%20%E2%80%93%20wprowadzenie%20i%20etyka.md) | skanowanie własnych systemów, czytanie wyników |
| [08. Docker](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/8.%20Docker/1.%20Czym%20s%C4%85%20kontenery.md) | kontenery, Podman/Docker, podstawowe polecenia, praktyczne przykłady |
| [09. Certyfikat SSL w Apache](Dzia%C5%82%204%20-%20Tematy%20dodatkowe/9.%20Certyfikat%20SSL%20w%20Apache/1.%20HTTPS%20i%20certyfikaty%20%E2%80%93%20podstawy.md) | HTTPS, certyfikat self-signed, podmiana certyfikatu, Let's Encrypt |

## Zadania

Katalog [Zadania](Zadania/) zawiera ćwiczenia pogrupowane tematycznie (`I. Zadania.md`
i `II. Rozwiązania.md` w każdym folderze) — od pracy na powłoce i edytorów, przez konta
i uprawnienia, po sieć, LVM i rozruch systemu. Zadania wykonuje się na maszynie szkoleniowej,
w razie potrzeby z dodatkowym dyskiem do ćwiczeń z partycjonowania i LVM.

## Dla autorów

Zasady pisania lekcji, szablon, konwencje nazw oraz system grafik opisuje
[narzedzia/PRZEWODNIK-AUTORA.md](narzedzia/PRZEWODNIK-AUTORA.md). Grafiki powstają z plików HTML
w [grafiki/zrodla](grafiki/zrodla/) i są renderowane poleceniem `node narzedzia/render-grafiki.mjs`.
Spójność odnośników i grafik sprawdza `python3 narzedzia/sprawdz.py`.

## Licencja

Materiały szkoleniowe — wszelkie prawa zastrzeżone. © Sebastian Koziatek.
