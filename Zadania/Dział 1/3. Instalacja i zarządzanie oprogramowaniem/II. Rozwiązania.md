![](../../../grafiki/1-3-rozwiazania.png)

# Rozwiązania – Instalacja i zarządzanie oprogramowaniem

## 1. Menedżer pakietów a instalatory ze stron WWW

Menedżer pakietów pobiera oprogramowanie z zaufanych, podpisanych cyfrowo repozytoriów. Korzyści: (1) automatyczne rozwiązywanie zależności, (2) weryfikacja podpisu GPG – pewność, że pakiet nie został podmieniony, (3) jedno polecenie aktualizuje cały system, (4) czyste usuwanie i historia transakcji z możliwością cofnięcia.

---

## 2. Czym jest polecenie yum

```bash
ls -l /usr/bin/yum
```

`/usr/bin/yum` to dowiązanie symboliczne do `dnf-3` – każde polecenie `yum` wykonuje w rzeczywistości DNF, więc `yum install` = `dnf install`.

---

## 3. Wyszukanie i informacje

```bash
dnf search wget
dnf search mc
dnf info mc
```

`dnf info` pokazuje wersję, rozmiar, repozytorium (pole „Repozytorium”/„Repository”) i opis – bez instalowania.

---

## 4. Instalacja dwóch pakietów

```bash
sudo dnf install wget mc
```

Kilka pakietów podaje się po prostu po spacji; `dnf` policzy wspólną transakcję.

---

## 5. Lista zainstalowanych z filtrem

```bash
dnf list --installed | grep openssh
```

Działa też `rpm -qa | grep openssh`.

---

## 6. Skąd pochodzi plik

```bash
rpm -qf /etc/ssh/sshd_config
```

Plik należy do pakietu `openssh-server`.

---

## 7. Pliki pakietu

```bash
rpm -ql openssh-server
rpm -qc openssh-server
```

`-ql` wypisuje wszystkie pliki pakietu, `-qc` tylko pliki konfiguracyjne.

---

## 8. Lista repozytoriów

```bash
dnf repolist
dnf repolist --all | grep crb
```

Po świeżej instalacji `crb` jest wyłączone (widać je dopiero w `--all` ze statusem „disabled”).

---

## 9. EPEL i CRB

```bash
sudo dnf install epel-release
sudo dnf config-manager --set-enabled crb
dnf repolist
```

`epel-release` (z repozytorium Extras) instaluje plik `.repo` i klucz GPG EPEL; CRB włączamy, bo wiele pakietów EPEL ma tam zależności.

---

## 10. Instalacja htop

```bash
sudo dnf install htop
dnf list --installed htop
```

W kolumnie po prawej widać `@epel` – pakiet pochodzi z EPEL (dlatego bez zadania 9 nie dało się go znaleźć).

---

## 11. Plik .repo EPEL

```bash
cat /etc/yum.repos.d/epel.repo
```

Identyfikator to nazwa w nawiasach `[epel]`; o aktywności decyduje `enabled=1`; klucz wskazuje `gpgkey=` (a `gpgcheck=1` włącza weryfikację). `$releasever` to wersja systemu (np. 9), `$basearch` – architektura (np. x86_64); DNF podstawia je automatycznie, dzięki czemu jeden plik działa na różnych systemach.

---

## 12. Pobranie bez instalacji i obejrzenie pliku

```bash
cd ~
dnf download tree
rpm -qip tree-*.rpm
rpm -qlp tree-*.rpm
```

Opcja `-p` każe `rpm` pytać plik lokalny, a nie bazę zainstalowanych pakietów.

---

## 13. Instalacja pliku lokalnego

```bash
sudo dnf install ./tree-*.rpm
```

`dnf` zainstaluje plik lokalny i w razie potrzeby dociągnie zależności z repozytoriów; `rpm -ivh` nie zna repozytoriów, więc przy brakujących zależnościach kończy się błędem. Ścieżka musi zawierać `/` (np. `./`), żeby `dnf` wiedział, że to plik.

---

## 14. Dostępne aktualizacje i aktualizacja jednego pakietu

```bash
dnf check-update
sudo dnf update bash
```

`check-update` niczego nie zmienia (kod wyjścia 100 oznacza „są aktualizacje”); `update`/`upgrade` z nazwą pakietu aktualizuje tylko ten pakiet.

---

## 15. Historia transakcji

```bash
dnf history
dnf history info <ID>
```

W kolumnie „Wiersz poleceń” znajdź `install htop` i użyj jego ID.

---

## 16. Cofnięcie transakcji

```bash
sudo dnf history undo <ID>
rpm -q htop
dnf history
```

`undo` wykonuje operację odwrotną (tu: usuwa htop); `rpm -q htop` odpowie „nie jest zainstalowany”, a w historii przybędzie nowa transakcja.

---

## 17. Czyszczenie pamięci podręcznej

```bash
sudo dnf clean all
sudo dnf makecache
```

Przydaje się, gdy `dnf` widzi nieaktualne wersje, zgłasza błędy sum kontrolnych metadanych albo nie widzi pakietu świeżo dodanego do repozytorium.

---

## 18. Usunięcie i sprzątanie

```bash
sudo dnf remove wget mc tree
sudo dnf autoremove
```

`autoremove` usuwa tylko pakiety zainstalowane automatycznie jako zależności, których nic już nie wymaga – ale listę zawsze czytamy przed potwierdzeniem.

---

## 19. Zależności pakietu

```bash
dnf repoquery --requires htop
```

Zobaczysz m.in. biblioteki (`libncursesw…`), których htop potrzebuje do działania.

---

## 20. Piekło zależności

Piekło zależności to sytuacja, w której wymagania pakietów są sprzeczne (np. dwa programy wymagają różnych, niewspółistniejących wersji tej samej biblioteki) i nie istnieje rozwiązanie zadowalające wszystkich. Typowe przyczyny na RHEL 9/10: mieszanie repozytoriów przeznaczonych dla innych wersji systemu (np. `el8` na `el9`) oraz instalowanie pakietów spoza dystrybucji (np. zbudowanych pod Fedorę). `rpm --nodeps` nie rozwiązuje konfliktu – instaluje pakiet mimo braku zależności, więc program i tak nie działa, a baza RPM przestaje odzwierciedlać rzeczywisty stan systemu, przez co każda kolejna transakcja może się zachowywać nieprzewidywalnie.
