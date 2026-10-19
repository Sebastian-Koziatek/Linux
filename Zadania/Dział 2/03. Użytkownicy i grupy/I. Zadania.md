![](../../../grafiki/2-03-zadania.png)

# Zadania – Użytkownicy i grupy

> Pracuj jako zwykły użytkownik z dostępem do `sudo`. Zadania 1–5 dotyczą roota i sudo, 6–12 użytkowników, 13–16 grup, 17–19 plików konfiguracyjnych, 20 – kont centralnych.

## Root, sudo i su

**1.** Wyjaśnij własnymi słowami: czym konto root różni się od zwykłego konta i dlaczego nie pracujemy na nim na co dzień?

**2.** Sprawdź poleceniem, jakie uprawnienia `sudo` ma Twoje konto. Następnie wykonaj przez `sudo` jedno polecenie, którego zwykły użytkownik nie może wykonać (np. podejrzyj pierwsze wiersze `/etc/shadow`).

**3.** Wyjaśnij różnicę między `su`, `su -` i `sudo -i`: czyje hasło podajesz w każdym przypadku i czym różni się uzyskane środowisko?

**4.** Utwórz konto `tester` (z hasłem) i nadaj mu prawo do korzystania z `sudo`. Zaloguj się jako `tester` (`su - tester`) i udowodnij poleceniem, że sudo działa.

**5.** Przez `visudo -f` utwórz w `/etc/sudoers.d/` wpis, który pozwala użytkownikowi `tester` wykonywać **tylko** polecenie `systemctl status sshd` jako root bez podawania hasła. Przetestuj, że inne polecenia sudo nadal pytają o hasło lub są odrzucane. Na końcu znajdź w dzienniku ślad swoich wywołań sudo.

> **Wskazówka:** wpis ma postać `tester ALL=(root) NOPASSWD: /usr/bin/systemctl status sshd`.

## Użytkownicy

**6.** Utwórz konta `tux1` i `tux2` z opisami (imię i nazwisko) oraz nadaj im hasła. Sprawdź poleceniem `id`, że istnieją.

**7.** Obejrzyj katalog domowy `tux1` razem z plikami ukrytymi i porównaj jego zawartość z katalogiem `/etc/skel`. Skąd wzięły się te pliki?

**8.** W drugim terminalu (albo przez `su - tux1`) zaloguj się jako `tux1`. Następnie zablokuj to konto, spróbuj zalogować się ponownie i opisz, co się dzieje. Odblokuj konto.

**9.** Wymuś na koncie `tux1` zmianę hasła przy następnym logowaniu i sprawdź ustawienia starzenia się jego hasła.

**10.** Ustaw hasłu konta `tux2` maksymalną ważność 90 dni z ostrzeżeniem 7 dni przed wygaśnięciem.

**11.** Dopisz `tux1` do grupy `wheel` tak, aby **nie** utracił żadnej dotychczasowej grupy. Jakiej opcji trzeba użyć i co by się stało bez niej?

**12.** Sprawdź, kto jest aktualnie zalogowany w systemie i wyświetl historię ostatnich logowań.

## Grupy

**13.** Utwórz grupę `pingwiny` i dodaj do niej `tux1` oraz `tux2` (jednym poleceniem albo dwoma). Sprawdź skład grupy.

**14.** Wyjaśnij: czym różni się grupa główna użytkownika od grupy dodatkowej i gdzie każda z nich jest zapisana?

**15.** Utwórz katalog `/srv/pingwiny`, w którym `tux1` i `tux2` będą mogli wspólnie pracować: pełne prawa dla grupy `pingwiny`, brak dostępu dla innych, a nowe pliki mają automatycznie należeć do grupy. Przetestuj, tworząc plik jako `tux1`, i sprawdź grupę tego pliku.

**16.** Usuń `tux2` z grupy `pingwiny` i udowodnij poleceniem, że już do niej nie należy.

## Pliki konfiguracyjne

**17.** Wyświetl wpis konta `tux1` z `/etc/passwd` i omów wszystkie siedem pól. Dlaczego w drugim polu jest `x`?

**18.** Podejrzyj (przez `sudo`) wpis `tux1` w `/etc/shadow`. Po czym poznasz, że konto jest zablokowane? Jak wygląda początek pola z hasłem, gdy skrót wykonano algorytmem SHA-512?

**19.** Wyjaśnij, dlaczego do sprawdzenia istnienia konta lepiej używać `getent passwd nazwa` niż `grep nazwa /etc/passwd`, oraz jakim poleceniem bezpiecznie edytować `/etc/passwd`, gdy naprawdę trzeba to zrobić ręcznie.

## Konta centralne (koncepcyjne)

**20.** Firma ma 30 serwerów Linux i domenę Active Directory. Opisz w kilku zdaniach: (a) po co podłączać serwery do domeny zamiast zakładać konta lokalne, (b) jaką rolę pełnią w logowaniu PAM i sssd, (c) jakim poleceniem dołącza się serwer RHEL do domeny i (d) dzięki czemu logowanie działa także przy chwilowej awarii łącza do kontrolera domeny.

## Sprzątanie

**21.** Usuń konta `tux1`, `tux2` i `tester` wraz z katalogami domowymi oraz grupę `pingwiny` i katalog `/srv/pingwiny`. Sprawdź, że w `/home` nie zostały pliki bez właściciela.
