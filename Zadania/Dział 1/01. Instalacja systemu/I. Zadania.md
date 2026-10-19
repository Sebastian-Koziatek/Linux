![](../../../grafiki/1-01-zadania.png)

# Zadania – Instalacja systemu

> Zadania 1–5 to pytania sprawdzające teorię z modułu, zadania 6–16 wykonujesz na swojej maszynie wirtualnej zainstalowanej według lekcji 6 i 7.

**1.** Wyjaśnij własnymi słowami różnicę między jądrem Linux a dystrybucją Linuksa.

**2.** Przyporządkuj dystrybucje do rodzin (Red Hat / Debian / SUSE / Arch): Ubuntu, Rocky Linux, Fedora, Linux Mint, openSUSE Leap, AlmaLinux, Kali Linux, Manjaro.

**3.** Czym różnią się od siebie RHEL, CentOS Stream, Rocky Linux i AlmaLinux? Którą z nich wybrałbyś na serwer produkcyjny bez budżetu na subskrypcje i dlaczego?

**4.** Wymień cztery środowiska, w których może działać Linux (sprzęt, maszyna wirtualna, chmura, kontener), i wskaż, które z nich NIE ma własnego jądra.

**5.** Kiedy warto mieć przestrzeń SWAP, a kiedy można z niej zrezygnować? Jaki rozmiar SWAP zaleca się dla serwera z 4 GB RAM?

**6.** Sprawdź, jaką dystrybucję i wersję ma Twoja maszyna. Użyj dwóch różnych poleceń.

**7.** Sprawdź wersję uruchomionego jądra oraz – jednym poleceniem – pełne podsumowanie systemu (nazwa komputera, system, wirtualizacja, architektura).

**8.** Sprawdź, czy Twoja maszyna działa w środowisku wirtualnym i pod jakim hipernadzorcą.

**9.** Sprawdź, ile pamięci RAM i SWAP ma Twój system oraz skąd pochodzi SWAP (partycja, wolumin, plik).

**10.** Wyświetl układ dysków i partycji maszyny. Odszukaj partycję `/boot` i woluminy LVM utworzone przez instalator.

**11.** Nadaj swojemu użytkownikowi (jeśli jeszcze ich nie ma) uprawnienia do `sudo`, dodając go do grupy `wheel`, i zweryfikuj, że działają.

> **Wskazówka:** jeżeli przy instalacji zaznaczono „Ustawienie tego użytkownika jako administratora”, użytkownik już jest w grupie `wheel` – sprawdź to poleceniem `id`.

**12.** Zaktualizuj system menedżerem `dnf`, a następnie sprawdź, czy pozostały jakieś aktualizacje do wykonania.

**13.** Znajdź, który pakiet zawiera program `needs-restarting`, zainstaluj go i sprawdź, czy po aktualizacji system wymaga ponownego uruchomienia.

**14.** Zainstaluj pakiet `mc` (Midnight Commander), a następnie wyświetl jego stronę podręcznika `man` i odczytaj z niej, do czego służy opcja `-e`.

**15.** Sprawdź nazwę komputera i zmień ją na `serwer` poleceniem `hostnamectl`. Zweryfikuj zmianę.

**16.** (Tylko RHEL) Sprawdź stan rejestracji systemu i dostępne subskrypcje poleceniem `subscription-manager`. Na Rocky/AlmaLinux: wyjaśnij, dlaczego to polecenie nie jest tam potrzebne.
