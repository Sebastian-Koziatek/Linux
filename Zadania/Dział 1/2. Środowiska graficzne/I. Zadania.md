![](../../../grafiki/1-2-zadania.png)

# Zadania – Środowiska graficzne

> Zadania wykonuj na maszynie wirtualnej z modułu 01 (Minimal Install lub Server). Instalacja środowiska w zadaniu 5 pobiera kilka GB – uruchom ją przy dobrym łączu.

**1.** Wyjaśnij różnicę między serwerem wyświetlania, menedżerem okien i środowiskiem pulpitu. Podaj po jednym przykładzie każdego z nich.

**2.** Sprawdź, jaki cel (target) systemd jest ustawiony jako domyślny na Twojej maszynie.

**3.** Sprawdź, w jakim typie sesji pracujesz (`wayland`, `x11` czy `tty`). Wyjaśnij otrzymany wynik.

**4.** Wyświetl listę dostępnych grup pakietów i odszukaj wśród nich środowiska graficzne. Następnie wyświetl informacje o grupie „Server with GUI” – ile pakietów obowiązkowych zawiera?

**5.** Zainstaluj środowisko graficzne grupą „Server with GUI”.

**6.** Przełącz system do trybu graficznego bez restartu i zaloguj się na pulpicie GNOME.

**7.** Ustaw tryb graficzny jako domyślny przy starcie systemu, zrestartuj maszynę i sprawdź, że pojawia się ekran logowania GDM.

**8.** Po zalogowaniu w GNOME otwórz terminal i ponownie sprawdź typ sesji oraz nazwę środowiska. Porównaj z wynikiem z zadania 3.

**9.** Sprawdź stan usługi menedżera wyświetlania `gdm`.

**10.** Przywróć domyślny start w trybie tekstowym i przełącz się do niego od razu, bez restartu.

> **Wskazówka:** potrzebne będą dwa polecenia – jedno zapisuje wybór na przyszłość, drugie przełącza natychmiast.

**11.** (Dla chętnych) Włącz repozytorium EPEL i sprawdź, jakie nowe grupy środowisk graficznych stały się dostępne. Nie musisz niczego instalować.

**12.** (Dla chętnych) Odinstaluj środowisko graficzne grupą `dnf group remove` i sprawdź, ile miejsca na dysku odzyskałeś (`df -h /` przed i po).
