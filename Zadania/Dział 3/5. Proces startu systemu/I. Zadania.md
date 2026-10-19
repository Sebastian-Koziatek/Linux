![](../../../grafiki/3-5-zadania.png)

# Zadania – Proces startu systemu

> Zadania 10–13 wykonuj na maszynie szkoleniowej (restartowanie i tryby naprawcze wymagają dostępu do konsoli maszyny wirtualnej, nie tylko SSH).

## Proces startu i GRUB

**1.** Sprawdź, ile trwał ostatni start systemu i które trzy usługi startowały najdłużej.

**2.** Sprawdź, czy Twoja maszyna startuje w trybie BIOS, czy UEFI.

**3.** Wyświetl zawartość katalogu `/boot` i wskaż: plik jądra, initramfs oraz katalog konfiguracji GRUB-a. Sprawdź też wersję aktualnie uruchomionego jądra i porównaj z listą zainstalowanych pakietów jądra.

**4.** Przejrzyj plik `/etc/default/grub`. Co oznaczają zmienne `GRUB_TIMEOUT` i `GRUB_CMDLINE_LINUX`?

**5.** Zmień czas oczekiwania menu GRUB na 8 sekund i przebuduj konfigurację właściwym poleceniem. Do którego pliku się ją generuje na RHEL 9 i dlaczego nie edytuje się go ręcznie?

**6.** Poleceniem `grubby` wyświetl: domyślne jądro oraz pełne informacje o wszystkich wpisach menu.

**7.** Wyświetl listę aktualnie załadowanych modułów jądra i pokaż szczegóły jednego z nich (np. sterownika karty sieciowej).

## Targety

**8.** Sprawdź domyślny cel (target) systemu, a potem wypisz, jakie jednostki wchodzą w jego skład.

**9.** Wyjaśnij różnicę między `systemctl set-default` a `systemctl isolate`. Które z nich przeżyje restart?

**10.** (Konsola VM) Przełącz działający system w tryb ratunkowy poleceniem `systemctl`, rozejrzyj się (czy działa sieć? jakie procesy działają?), po czym wróć do celu domyślnego.

**11.** (Konsola VM) Uruchom system w trybie ratunkowym **z menu GRUB-a**, dopisując odpowiedni parametr jądra klawiszem `e`. Czym różni się ten sposób od zadania 10?

## Usługi – systemctl

**12.** Zainstaluj serwer nginx i uruchom jego usługę. Sprawdź jej stan trzema sposobami: pełny status, `is-active`, lista procesów.

**13.** Zatrzymaj nginx, potwierdź, że nie działa (status + próba `curl localhost`), a następnie uruchom go ponownie i włącz autostart jednym poleceniem. Sprawdź, jaki symlink powstał po włączeniu autostartu.

**14.** Wyświetl: wszystkie usługi i ich stan, tylko usługi w stanie `failed` oraz ustawienia autostartu wszystkich plików jednostek usług.

**15.** Zamaskuj usługę nginx i spróbuj ją uruchomić. Odczytaj komunikat, po czym zdejmij maskę. Czym maskowanie różni się od `disable`?

**16.** Wyświetl logi usługi nginx: wszystkie od ostatniego startu systemu oraz w trybie śledzenia na żywo. W drugim terminalu wykonaj `curl localhost`, by zobaczyć nowe wpisy (jeśli ich nie widać, sprawdź `sudo tail -f /var/log/nginx/access.log` – nginx pisze dostęp do pliku).

**17.** Sprawdź, czy usługa `firewalld` działa i jest w autostarcie. Zatrzymaj ją, sprawdź dostęp do strony nginx z innej maszyny (albo `curl` na adres IP serwera), po czym **przywróć firewalld do działania** i zamiast wyłączania zapory dodaj trwałą regułę wpuszczającą HTTP.

## Własna usługa

**18.** Napisz skrypt `/usr/local/bin/puls.sh`, który co 30 sekund wypisuje datę i liczbę zalogowanych użytkowników. Stwórz dla niego jednostkę `puls.service` (opis, `Type=simple`, restart po awarii po 5 s), uruchom ją z autostartem i obejrzyj jej logi.

**19.** Zabij proces skryptu `puls.sh` i udowodnij (status, logi), że systemd podniósł usługę automatycznie.

**20.** Posprzątaj: zatrzymaj i wyłącz usługę `puls`, usuń jej plik jednostki i skrypt, przeładuj konfigurację systemd. Na koniec wyjaśnij: jakim starym poleceniem (sprzed systemd) włączało się autostart usługi i co je dziś zastępuje?
