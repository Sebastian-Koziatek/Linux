# Administracja systemem Linux I — materiały szkoleniowe

Materiały do pięciodniowego szkolenia **„Administracja systemem Linux I”** prowadzonego w formie
warsztatowej. Napisane z myślą o osobach, które **dopiero zaczynają pracę z Linuksem** — administratorach
Windows, testerach, programistach, analitykach. Nie zakładamy żadnej wcześniejszej znajomości systemu:
zaczynamy od instalacji, kończymy na samodzielnej konfiguracji dysków, sieci, kont i zapory.

Systemem referencyjnym jest rodzina **Red Hat Enterprise Linux 9/10** (Rocky Linux, AlmaLinux,
CentOS Stream). Tam, gdzie Ubuntu/Debian robi coś inaczej, znajdziesz ramkę *Na Ubuntu/Debianie*.

## Jak czytać

Każda lekcja ma ten sam układ: **Po co mi to?** → **Jak to działa** → **W praktyce** (polecenia
krok po kroku z przykładowym wynikiem) → **Najczęstsze błędy i pułapki** → **Podsumowanie** ze ściągą.
Każdy moduł otwiera plik `0. O module.md` z listą lekcji, a w katalogu [Zadania](Zadania/) czekają
ćwiczenia z rozwiązaniami.

Materiały czyta się wprost na GitHubie. Do pracy offline polecamy [Obsidian](https://obsidian.md/) —
otwórz katalog repozytorium jako skarbiec (vault).

## Program

### Dział 1 — Wprowadzenie do systemu

| Moduł | Zakres |
|---|---|
| [01. Instalacja systemu](Dział%201%20-%20Wprowadzenie%20do%20systemu/01.%20Instalacja%20systemu/0.%20O%20module.md) | czym jest Linux, dystrybucje, nośniki, rodzaj i wersja systemu, maszyna wirtualna, instalacja krok po kroku |
| [02. Środowiska graficzne](Dział%201%20-%20Wprowadzenie%20do%20systemu/02.%20Środowiska%20graficzne/0.%20O%20module.md) | GNOME, KDE Plasma, Xfce, Cinnamon, MATE; instalacja pulpitu na serwerze i kiedy to ma sens |
| [03. Instalacja i zarządzanie oprogramowaniem](Dział%201%20-%20Wprowadzenie%20do%20systemu/03.%20Instalacja%20i%20zarządzanie%20oprogramowaniem/0.%20O%20module.md) | menedżer pakietów, YUM, repozytoria, pakiety RPM, DNF, inne dystrybucje, piekło zależności |
| [04. Dokumentacja i pomoc](Dział%201%20-%20Wprowadzenie%20do%20systemu/04.%20Dokumentacja%20i%20pomoc/0.%20O%20module.md) | `man`, `info`, pomoc wbudowana w programy, gdzie szukać odpowiedzi |

### Dział 2 — Podstawy pracy z systemem Linux

| Moduł | Zakres |
|---|---|
| [05. Praca z powłoką Bash](Dział%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/05.%20Praca%20z%20powłoką%20Bash/0.%20O%20module.md) | terminal i powłoka, poruszanie się po systemie, pliki i katalogi, prompt, konfiguracja powłoki, zmienne i aliasy, dowiązania, vi/vim, nano |
| [06. Zarządzanie plikami i katalogami](Dział%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/06.%20Zarządzanie%20plikami%20i%20katalogami/0.%20O%20module.md) | uprawnienia (`chmod`, `chown`), wyszukiwanie (`find`, `locate`), przeglądanie i potoki (`cat`, `less`, `tail`, `grep`), podstawy `sed` |
| [07. Użytkownicy i grupy](Dział%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/07.%20Użytkownicy%20i%20grupy/0.%20O%20module.md) | root, `sudo`, `su`, konta i grupy lokalne, pliki konfiguracyjne, uwierzytelnianie w LDAP/AD (sssd, PAM) |
| [08. Zdalna administracja](Dział%202%20-%20Podstawy%20pracy%20z%20systemem%20Linux/08.%20Zdalna%20administracja/0.%20O%20module.md) | SSH: serwer, klient, klucze, zdalne polecenia i kopiowanie plików, pulpit zdalny |

### Dział 3 — Zarządzanie systemem Linux

| Moduł | Zakres |
|---|---|
| [09. Zarządzanie dyskami](Dział%203%20-%20Zarządzanie%20systemem%20Linux/09.%20Zarządzanie%20dyskami/0.%20O%20module.md) | urządzenia w `/dev`, wykrywanie dysków, MBR i GPT, typy partycji, `fdisk`, `cfdisk`, `parted`, `gparted`, RAID i `mdadm` |
| [10. Woluminy logiczne LVM](Dział%203%20-%20Zarządzanie%20systemem%20Linux/10.%20Woluminy%20logiczne%20LVM/0.%20O%20module.md) | idea LVM, tworzenie i powiększanie woluminów, LVM a RAID |
| [11. System plików](Dział%203%20-%20Zarządzanie%20systemem%20Linux/11.%20System%20plików/0.%20O%20module.md) | budowa systemu plików, ext2/3/4, XFS, Btrfs i ZFS, montowanie i naprawa, drzewo katalogów, `fstab` |
| [12. Konfiguracja sieci](Dział%203%20-%20Zarządzanie%20systemem%20Linux/12.%20Konfiguracja%20sieci/0.%20O%20module.md) | podstawy sieci, `ip`/`ifconfig`/`route`, NetworkManager (`nmcli`, `nmtui`, GUI), pliki konfiguracyjne, diagnostyka |
| [13. Proces startu systemu](Dział%203%20-%20Zarządzanie%20systemem%20Linux/13.%20Proces%20startu%20systemu/0.%20O%20module.md) | etapy startu, GRUB2, poziomy startowe i targety, demony i `systemctl`, własna usługa, init a systemd |
| [14. Zabezpieczenia sieciowe](Dział%203%20-%20Zarządzanie%20systemem%20Linux/14.%20Zabezpieczenia%20sieciowe/0.%20O%20module.md) | zapora sieciowa, `iptables`, `firewalld`, zabezpieczenia na poziomie jądra (`sysctl`) |

### Dział 4 — Tematy dodatkowe

Materiał poza programem podstawowym — dla chętnych i na pytania z sali.

| Moduł | Zakres |
|---|---|
| [15. Crontab](Dział%204%20-%20Tematy%20dodatkowe/15.%20Crontab/0.%20O%20module.md) | harmonogram zadań, składnia czasu, timery systemd |
| [16. SELinux](Dział%204%20-%20Tematy%20dodatkowe/16.%20SELinux/0.%20O%20module.md) | czym jest SELinux, tryby pracy, diagnoza i naprawa typowych blokad |
| [17. Samba](Dział%204%20-%20Tematy%20dodatkowe/17.%20Samba/0.%20O%20module.md) | udostępnianie plików dla Windows |
| [18. Logi systemowe](Dział%204%20-%20Tematy%20dodatkowe/18.%20Logi%20systemowe/0.%20O%20module.md) | `journalctl`, rsyslog, czytanie logów w praktyce |
| [19. Screen i tmux](Dział%204%20-%20Tematy%20dodatkowe/19.%20Screen%20i%20tmux/0.%20O%20module.md) | sesje terminala odporne na zerwane połączenie |
| [20. Lynis](Dział%204%20-%20Tematy%20dodatkowe/20.%20Lynis/0.%20O%20module.md) | audyt bezpieczeństwa i utwardzanie systemu |
| [21. nmap](Dział%204%20-%20Tematy%20dodatkowe/21.%20nmap/0.%20O%20module.md) | skanowanie własnych systemów, czytanie wyników |
| [22. Docker](Dział%204%20-%20Tematy%20dodatkowe/22.%20Docker/0.%20O%20module.md) | kontenery, Podman/Docker, podstawowe polecenia, praktyczne przykłady |
| [23. Certyfikat SSL w Apache](Dział%204%20-%20Tematy%20dodatkowe/23.%20Certyfikat%20SSL%20w%20Apache/0.%20O%20module.md) | HTTPS, certyfikat self-signed, podmiana certyfikatu, Let's Encrypt |

## Zadania

Katalog [Zadania](Zadania/) zawiera dla każdego modułu plik `I. Zadania.md` oraz `II. Rozwiązania.md`.
Zadania wykonuje się na maszynie szkoleniowej — zwykle z dodatkowymi dyskami `/dev/sdb` i `/dev/sdc`
do ćwiczeń z partycjonowania, RAID i LVM.

## Dla autorów

Zasady pisania lekcji, szablon, konwencje nazw oraz system grafik opisuje
[narzedzia/PRZEWODNIK-AUTORA.md](narzedzia/PRZEWODNIK-AUTORA.md). Grafiki powstają z plików HTML
w [grafiki/zrodla](grafiki/zrodla/) i są renderowane poleceniem `node narzedzia/render-grafiki.mjs`.
Spójność odnośników i grafik sprawdza `python3 narzedzia/sprawdz.py`.

## Licencja

Materiały szkoleniowe — wszelkie prawa zastrzeżone. © Sebastian Koziatek.
