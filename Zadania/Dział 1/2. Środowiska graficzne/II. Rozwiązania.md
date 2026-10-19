![](../../../grafiki/1-2-rozwiazania.png)

# Rozwiązania – Środowiska graficzne

## 1. Serwer wyświetlania, menedżer okien, środowisko pulpitu

Serwer wyświetlania (np. Wayland, X11) rysuje obraz i odbiera klawiaturę oraz mysz. Menedżer okien (np. Mutter, KWin, Xfwm) zarządza samymi oknami: ramki, przesuwanie, fokus. Środowisko pulpitu (np. GNOME, KDE Plasma, Xfce) to pełny zestaw: menedżer okien + panel, menu, ustawienia i aplikacje.

---

## 2. Domyślny cel systemd

```bash
systemctl get-default
```

Po instalacji Minimal/Server wynik to `multi-user.target` (tryb tekstowy).

---

## 3. Typ sesji

```bash
echo $XDG_SESSION_TYPE
```

W konsoli tekstowej i przez SSH wynik to `tty` – sesja nie jest graficzna. `wayland` albo `x11` zobaczysz dopiero w terminalu uruchomionym wewnątrz pulpitu.

---

## 4. Grupy pakietów

```bash
dnf group list
dnf group info "Server with GUI"
```

Środowiska znajdziesz w sekcji „Available Environment Groups” (m.in. Server with GUI, Workstation). `group info` wypisuje grupy obowiązkowe (Mandatory) i opcjonalne – liczba zależy od wersji systemu; istotne jest odczytanie sekcji „Mandatory Groups”.

---

## 5. Instalacja środowiska

```bash
sudo dnf group install "Server with GUI"
```

Nazwę grupy podajemy w cudzysłowach, bo zawiera spacje; instalacja obejmuje ponad tysiąc pakietów.

---

## 6. Przełączenie do grafiki bez restartu

```bash
sudo systemctl isolate graphical.target
```

Na konsoli maszyny pojawia się ekran logowania GDM; `isolate` nie zmienia ustawienia domyślnego.

---

## 7. Grafika na stałe

```bash
sudo systemctl set-default graphical.target
sudo reboot
```

Po restarcie maszyna startuje wprost do ekranu logowania; `systemctl get-default` zwraca `graphical.target`.

---

## 8. Sesja wewnątrz GNOME

```bash
echo $XDG_SESSION_TYPE
echo $XDG_CURRENT_DESKTOP
```

W terminalu GNOME na RHEL 9/10 wyniki to `wayland` i `GNOME` – w przeciwieństwie do `tty` z zadania 3, bo tym razem zmienne opisują sesję graficzną.

---

## 9. Stan GDM

```bash
systemctl status gdm
```

Usługa powinna być `active (running)`; to właśnie ona wyświetla ekran logowania.

---

## 10. Powrót do trybu tekstowego

```bash
sudo systemctl set-default multi-user.target
sudo systemctl isolate multi-user.target
```

`set-default` zapisuje wybór na kolejne starty, `isolate` zamyka sesję graficzną natychmiast. Kolejność jest dowolna, potrzebne są oba.

---

## 11. EPEL i dodatkowe środowiska

```bash
sudo dnf install epel-release
dnf group list
```

Po włączeniu EPEL na liście pojawiają się dodatkowe środowiska, m.in. Xfce, KDE Plasma Workspaces, Cinnamon i MATE (dokładny zestaw zależy od wersji EPEL).

---

## 12. Usunięcie środowiska

```bash
df -h /
sudo systemctl set-default multi-user.target
sudo dnf group remove "Server with GUI"
df -h /
```

Przed usunięciem wracamy do celu tekstowego, żeby nie wyłączyć pulpitu „pod sobą”. Porównanie wyników `df -h /` pokaże odzyskane kilka GB.
