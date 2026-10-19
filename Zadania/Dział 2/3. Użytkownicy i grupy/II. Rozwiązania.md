![](../../../grafiki/2-3-rozwiazania.png)

# Rozwiązania – Użytkownicy i grupy

> Zestawy odpowiadają kolejnym tematom modułu; numeracja zaczyna się od nowa w każdym z nich.

## Root, sudo, su

### 1. Czym się różni konto root od konta użytkownika?

```
Konto root (superuser):

Uprawnienia:
- UID = 0 (User ID zero)
- Pełny dostęp do wszystkich plików i katalogów
- Może modyfikować dowolne pliki systemowe
- Może instalować/usuwać oprogramowanie
- Może zarządzać usługami systemowymi
- Może tworzyć/usuwać konta użytkowników
- Może montować/odmontowywać systemy plików

Możliwości:
- Obejście kontroli dostępu (permissions)
- Dostęp do wszystkich urządzeń (/dev)
- Modyfikacja jądra systemu
- Zarządzanie siecią i firewall
- Dostęp do wszystkich procesów

Katalog domowy: /root
Shell: zwykle /bin/bash
Prompt: # (hash/kratka)

Konto użytkownika:

Uprawnienia:
- UID > 0 (zwykle 1000+)
- Dostęp tylko do własnych plików
- Ograniczony dostęp do plików systemowych
- Nie może instalować oprogramowania systemowego
- Nie może modyfikować konfiguracji systemowej

Ograniczenia:
- Kontrola dostępu przez uprawnienia plików
- Brak dostępu do /etc, /boot, /root
- Nie może zabijać procesów innych użytkowników
- Nie może montować systemów plików

Katalog domowy: /home/username
Prompt: $ (dolar)

Bezpieczeństwo:
- Root: maksymalne ryzyko - jeden błąd może zniszczyć system
- User: ograniczone ryzyko - może uszkodzić tylko własne dane

Filozofia Linux:
- Principle of least privilege
- Używaj root tylko gdy niezbędne
- Codzienne zadania jako zwykły użytkownik
```

---

### 2. Czym jest sudo?

```
sudo (substitute user do / superuser do):

Definicja:
- Mechanizm delegacji uprawnień administratora
- Pozwala zwykłym użytkownikom wykonywać polecenia z uprawnieniami root
- Tymczasowe podniesienie uprawnień
- Kontrolowany dostęp do funkcji administratora

Główne cechy:

Bezpieczeństwo:
- Wymaga hasła użytkownika (nie root)
- Logowanie wszystkich działań
- Granularna kontrola uprawnień
- Timeout sesji (domyślnie 15 minut)

Konfiguracja:
- Plik /etc/sudoers
- Grupy użytkowników (wheel, sudo, admin)
- Reguły per-user i per-command
- Aliasy poleceń i użytkowników

Podstawowe użycie:
sudo polecenie                    # Wykonaj polecenie jako root
sudo -u username polecenie        # Wykonaj jako inny użytkownik
sudo -i                          # Interactive shell jako root
sudo -s                          # Shell jako root
sudo -l                          # Lista dostępnych poleceń

Zalety sudo:
- Auditowanie (logi w /var/log/auth.log)
- Brak potrzeby dzielenia hasła root
- Granularne uprawnienia
- Łatwiejsze zarządzanie dostępem
- Możliwość odwołania uprawnień

Logi sudo:
tail /var/log/auth.log | grep sudo
journalctl | grep sudo

Przykłady użycia:
sudo apt update                   # Aktualizacja pakietów
sudo systemctl restart apache2   # Restart usługi
sudo mount /dev/sdb1 /mnt        # Montowanie dysku
sudo useradd newuser             # Dodanie użytkownika

Konfiguracja sudoers:
visudo                           # Bezpieczna edycja /etc/sudoers
```

---

### 3. Jak z poziomu użytkownika zalogować się do konta root?

```
Metody logowania do root:

1. su (substitute user):
su -
# Wymaga hasła root
# - oznacza login shell (pełne środowisko root)

su
# Zmienia na root ale zachowuje środowisko użytkownika

2. sudo su:
sudo su -
# Używa hasła użytkownika (jeśli ma uprawnienia sudo)
# Bezpieczniejsze od dzielenia hasła root

3. sudo -i:
sudo -i
# Interactive login shell jako root
# Preferowany sposób

4. Bezpośrednie logowanie:
login root
# Na konsoli systemowej
# Wymaga hasła root

5. SSH (jeśli włączone):
ssh root@localhost
# Wymaga konfiguracji SSH dla root

Porównanie metod:

su -:
- Wymaga hasła root
- Pełne środowisko root
- Tradycyjna metoda

sudo su -:
- Wymaga hasła użytkownika
- Logowane przez sudo
- Bezpieczniejsze

sudo -i:
- Wymaga hasła użytkownika  
- Preferowane przez sudo
- Najlepsze practices

Weryfikacja tożsamości root:
whoami                    # Powinno pokazać 'root'
id                       # UID=0
echo $HOME               # /root
pwd                      # Lokalizacja

Wyjście z root:
exit
logout
Ctrl+D

Uwagi bezpieczeństwa:
- Używaj sudo zamiast su gdy możliwe
- Nigdy nie włączaj SSH dla root w produkcji
- Ogranicz czas przebywania jako root
- Używaj sudo -i zamiast sudo su -
```

---

### 4. Zaloguj się do konta root i korzystając z pakietu sudo dopisz konto swojego użytkownika do listy kont uprawnionych.

```
Kroki dodania użytkownika do sudo:

1. Zaloguj się jako root:
sudo -i
# lub: su -

2. Sprawdź istniejącą konfigurację:
cat /etc/sudoers | grep -E "^%|^[a-zA-Z]"

3. Metoda 1 - Dodanie do grupy wheel/sudo:

RHEL/CentOS/Fedora:
usermod -aG wheel username

Debian/Ubuntu:
usermod -aG sudo username

4. Metoda 2 - Edycja /etc/sudoers:
visudo

Dodaj linię:
username ALL=(ALL) ALL

5. Metoda 3 - Utworzenie pliku w sudoers.d:
echo "username ALL=(ALL) ALL" > /etc/sudoers.d/username
chmod 440 /etc/sudoers.d/username

Weryfikacja:
1. Wyjdź z root:
exit

2. Testuj sudo:
sudo whoami
# Powinno pokazać 'root'

3. Sprawdź uprawnienia:
sudo -l

Przykłady konfiguracji w sudoers:

Pełne uprawnienia:
username ALL=(ALL) ALL

Bez hasła:
username ALL=(ALL) NOPASSWD: ALL

Tylko konkretne polecenia:
username ALL=(ALL) /usr/bin/systemctl, /usr/bin/mount

Grupa z pełnymi uprawnieniami:
%wheel ALL=(ALL) ALL

Sprawdzenie członkostwa w grupach:
groups username
id username

Testowanie różnych poleceń sudo:
sudo ls /root
sudo systemctl status sshd
sudo cat /etc/shadow

Dodatkowe opcje sudoers:

Aliasy użytkowników:
User_Alias ADMINS = john, jane, bob
ADMINS ALL=(ALL) ALL

Aliasy hostów:
Host_Alias SERVERS = server1, server2
username SERVERS=(ALL) ALL

Aliasy poleceń:
Cmnd_Alias SERVICES = /usr/bin/systemctl
username ALL=(ALL) SERVICES

Domyślne ustawienia:
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Defaults timestamp_timeout=15
Defaults !visiblepw
```

---

### 5. Czym się różni sudo su - od su?

```
Różnice między 'sudo su -' a 'su':

sudo su -:

Mechanizm uwierzytelnienia:
- Wymaga hasła UŻYTKOWNIKA
- Sprawdza uprawnienia sudo użytkownika
- Loguje działanie w systemie audytu

Bezpieczeństwo:
- Nie wymaga znajomości hasła root
- Wszystkie działania są logowane
- Można ograniczyć kto może używać
- Timeout automatyczny

Audyt:
- Zapisuje w /var/log/auth.log
- Możliwość śledzenia kto i kiedy
- Integracja z systemami monitorowania

Konfiguracja:
- Kontrolowane przez /etc/sudoers
- Granularne uprawnienia
- Możliwość ograniczenia poleceń

su:

Mechanizm uwierzytelnienia:
- Wymaga hasła ROOT
- Bezpośredni dostęp do konta root
- Brak dodatkowego logowania

Bezpieczeństwo:
- Wymaga dzielenia hasła root
- Trudniejsze audytowanie
- Każdy kto zna hasło może się zalogować

Audyt:
- Minimalne logowanie
- Trudno śledzić działania
- Brak granularnej kontroli

Porównanie praktyczne:

sudo su -:
$ sudo su -
[sudo] password for user: <hasło_użytkownika>
# whoami
root

su:
$ su -
Password: <hasło_root>
# whoami  
root

Inne warianty:

sudo -i:
- Preferowany sposób
- Login shell jako root
- Pełne środowisko root
- Logowanie przez sudo

sudo -s:
- Shell jako root
- Zachowuje obecne środowisko
- Nie zmienia $HOME

sudo su:
- Bez -, nie zmienia środowiska
- Non-login shell
- Może nie załadować profilu root

Środowisko po zalogowaniu:

su -:
- $HOME = /root
- PATH = root's PATH
- Pełny profil root

sudo su -:
- $HOME = /root  
- PATH = root's PATH
- Pełny profil root
- + logowanie sudo

su (bez -):
- $HOME = user's home
- PATH = user's PATH
- Środowisko użytkownika

Best practices:
1. Używaj sudo -i zamiast sudo su -
2. Unikaj zwykłego su
3. Nigdy nie udostępniaj hasła root
4. Konfiguruj sudo dla konkretnych zadań
5. Regularnie przeglądaj logi sudo

Sprawdzenie środowiska:
echo $HOME
echo $PATH
echo $USER
pwd
env | grep -E "HOME|PATH|USER"
```

---

### 6. Przejrzyj plik konfiguracyjny sudo i utwórz wpis który pozwoli wywoływać polecenia sudo bez hasła.

```
Przegląd pliku konfiguracyjnego sudo:

1. Bezpieczne otwieranie sudoers:
sudo visudo

Uwaga: NIGDY nie edytuj /etc/sudoers bezpośrednio!
visudo sprawdza składnię przed zapisem.

2. Struktura pliku /etc/sudoers:

Główne sekcje:
# Defaults - domyślne ustawienia
# User privilege specification - uprawnienia użytkowników
# Group privilege specification - uprawnienia grup
# Include directive - dodatkowe pliki

Przykładowa zawartość:
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

root    ALL=(ALL:ALL) ALL
%admin  ALL=(ALL) ALL
%sudo   ALL=(ALL:ALL) ALL

3. Dodanie wpisu bez hasła:

Metoda 1 - Modyfikacja głównego pliku:
sudo visudo

Dodaj linię:
username ALL=(ALL) NOPASSWD: ALL

Metoda 2 - Utworzenie oddzielnego pliku:
sudo visudo -f /etc/sudoers.d/nopasswd-username

Zawartość pliku:
username ALL=(ALL) NOPASSWD: ALL

4. Różne warianty konfiguracji NOPASSWD:

Pełne uprawnienia bez hasła:
username ALL=(ALL) NOPASSWD: ALL

Tylko konkretne polecenia:
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl, /usr/bin/mount

Tylko restart usług:
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart *

Grupa bez hasła:
%wheel ALL=(ALL) NOPASSWD: ALL

Kombinacja z hasłem i bez:
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl
username ALL=(ALL) /usr/bin/vi /etc/hosts

5. Testowanie konfiguracji:

Sprawdź składnię:
sudo visudo -c

Lista uprawnień:
sudo -l

Test bez hasła:
sudo whoami
# Nie powinno pytać o hasło

Test konkretnego polecenia:
sudo systemctl status sshd

6. Zaawansowane opcje:

Ograniczenie czasowe:
Defaults:username timestamp_timeout=0

Bez logów dla NOPASSWD:
Defaults:username !syslog

Wymaganie TTY:
Defaults:username requiretty

Ustawienia środowiska:
Defaults:username env_keep += "DISPLAY HOME"

7. Przykład kompletnej konfiguracji:

sudo visudo -f /etc/sudoers.d/custom-user

Zawartość:
# User privilege specification for custom-user
custom-user ALL=(ALL) NOPASSWD: ALL

# Alternative: limited commands without password
# custom-user ALL=(ALL) NOPASSWD: /usr/bin/systemctl, /usr/bin/mount, /usr/bin/umount

# Optional: specific defaults for this user
Defaults:custom-user !authenticate
Defaults:custom-user timestamp_timeout=0

8. Weryfikacja i testowanie:

Sprawdź uprawnienia:
sudo -l -U username

Test różnych poleceń:
sudo ls /root
sudo systemctl status sshd
sudo cat /etc/shadow

Sprawdź logi:
sudo tail /var/log/auth.log | grep sudo

9. Bezpieczeństwo NOPASSWD:

Zagrożenia:
- Każdy kto przejmie sesję może wykonać sudo
- Screen lock nie chroni przed sudo
- Skrypty mogą automatycznie używać sudo

Mitygacja:
- Ogranicz NOPASSWD do konkretnych poleceń
- Używaj timestamp_timeout=0
- Regularnie przeglądaj logi
- Rozważ 2FA dla krytycznych systemów

10. Usuwanie konfiguracji NOPASSWD:

Usuń wpis z sudoers:
sudo visudo

Usuń plik w sudoers.d:
sudo rm /etc/sudoers.d/nopasswd-username

Sprawdź czy zmiany zadziałały:
sudo -l
sudo whoami  # Powinno pytać o hasło
```

## Zarządzanie użytkownikami

### 1. Utwórz dwa dodatkowe konta użytkownika „tux1" i „tux2". Nadaj tym użytkownikom hasło, aby móc się zalogować jako ci użytkownicy. Sprawdź, czy zostały utworzone konta użytkowników.

```
Tworzenie użytkowników:
sudo useradd tux1
sudo useradd tux2

Ustawianie haseł:
sudo passwd tux1
# Wprowadź hasło dla tux1

sudo passwd tux2
# Wprowadź hasło dla tux2

Weryfikacja utworzenia kont:
id tux1
id tux2

Sprawdzenie w /etc/passwd:
grep "tux[12]" /etc/passwd

Sprawdzenie katalogów domowych:
ls -la /home/ | grep tux

Alternatywne tworzenie z dodatkowym informacjami:
sudo useradd -c "Tux User 1" -m -s /bin/bash tux1
sudo useradd -c "Tux User 2" -m -s /bin/bash tux2

Opcje useradd:
-c = komentarz (pełna nazwa)
-m = utwórz katalog domowy
-s = domyślny shell
-G = dodatkowe grupy
-u = konkretny UID

Sprawdzenie szczegółów:
getent passwd tux1
getent passwd tux2

Lista wszystkich użytkowników:
cut -d: -f1 /etc/passwd | sort
```

---

### 2. Przyjrzyj się różnym plikom przechowującym informacje o użytkownikach (/etc/passwd, /etc/shadow, /etc/group, /etc/gshadow). Spójrz także na katalog domowy tych nowych użytkowników i porównaj to z zawartością /etc/skel.

```
Sprawdzenie /etc/passwd:
grep "tux[12]" /etc/passwd

Format /etc/passwd:
username:x:UID:GID:comment:home_directory:shell

Sprawdzenie /etc/shadow:
sudo grep "tux[12]" /etc/shadow

Format /etc/shadow:
username:password_hash:last_change:min_age:max_age:warn:inactive:expire:reserved

Sprawdzenie /etc/group:
grep "tux[12]" /etc/group

Format /etc/group:
group_name:x:GID:member_list

Sprawdzenie /etc/gshadow:
sudo grep "tux[12]" /etc/gshadow

Format /etc/gshadow:
group_name:password:administrators:members

Sprawdzenie katalogów domowych:
ls -la /home/tux1/
ls -la /home/tux2/

Sprawdzenie szablonu /etc/skel:
ls -la /etc/skel/

Porównanie zawartości:
diff -r /etc/skel /home/tux1
diff -r /etc/skel /home/tux2

Szczegółowa analiza plików:
# /etc/passwd - podstawowe informacje o użytkownikach
cat /etc/passwd | grep -E "tux1|tux2"

# /etc/shadow - zaszyfrowane hasła i polityki
sudo cat /etc/shadow | grep -E "tux1|tux2"

# /etc/group - informacje o grupach
cat /etc/group | grep -E "tux1|tux2"

# /etc/gshadow - hasła grup (rzadko używane)
sudo cat /etc/gshadow | grep -E "tux1|tux2"

Sprawdzenie uprawnień plików:
ls -la /etc/passwd /etc/shadow /etc/group /etc/gshadow

Uprawnienia:
/etc/passwd: 644 (r--r--r--)
/etc/shadow: 000 lub 640 (tylko root może czytać)
/etc/group: 644 (r--r--r--)
/etc/gshadow: 000 lub 640 (tylko root może czytać)
```

---

### 3. W innym oknie terminala spróbuj zalogować się jako tux1 i tux2. czy to działa?

```
Logowanie jako tux1:
su - tux1
# Wprowadź hasło dla tux1

Sprawdzenie tożsamości:
whoami
id
pwd

Wyjście z sesji tux1:
exit

Logowanie jako tux2:
su - tux2
# Wprowadź hasło dla tux2

Sprawdzenie tożsamości:
whoami
id
pwd

Alternative metody logowania:
ssh tux1@localhost          # Przez SSH (jeśli włączone)
login tux1                  # Na konsoli

Test w nowym terminalu:
# Otwórz nowy terminal i wykonaj:
su - tux1

Sprawdzenie środowiska po zalogowaniu:
echo $HOME
echo $USER
echo $SHELL
env | grep USER

Sprawdzenie czy można wykonywać polecenia:
ls -la
ps
df -h

Sprawdzenie historii:
history

Test logowania z różnych lokalizacji:
# Terminal 1:
su - tux1

# Terminal 2:
su - tux2

Sprawdzenie aktywnych sesji:
who
w
users

Logi logowania:
sudo tail /var/log/secure        # RHEL/CentOS
sudo tail /var/log/auth.log      # Debian/Ubuntu
journalctl | grep "su:"
```

---

### 4. Zablokuj konto użytkownika tux1.

```
Blokowanie konta tux1:
sudo usermod -L tux1

Alternatywne metody blokowania:
sudo passwd -l tux1             # Lock password
sudo chage -E 0 tux1           # Expire account immediately

Sprawdzenie czy konto jest zablokowane:
sudo passwd -S tux1
# Powinno pokazać "L" (Locked)

Sprawdzenie w /etc/shadow:
sudo grep tux1 /etc/shadow
# Hasło powinno być poprzedzone "!" lub "*"

Weryfikacja statusu konta:
chage -l tux1

Sprawdzenie przez getent:
getent shadow tux1

Różnice między metodami blokowania:
usermod -L: dodaje "!" przed hashem hasła
passwd -l: dodaje "!" przed hashem hasła
chage -E 0: ustawia datę wygaśnięcia na 1970-01-01

Sprawdzenie daty wygaśnięcia:
chage -l tux1 | grep "Account expires"

Test różnych metod:
# Metoda 1: usermod
sudo usermod -L tux1
sudo grep tux1 /etc/shadow

# Metoda 2: passwd
sudo passwd -l tux1
sudo passwd -S tux1

# Metoda 3: chage
sudo chage -E 0 tux1
chage -l tux1
```

---

### 5. W innym oknie terminala spróbuj zalogować się jako tux1. Czy możesz się teraz zalogwać?

```
Test logowania zablokowanego konta:
su - tux1
# Powinno pokazać: Authentication failure

Sprawdzenie różnych metod logowania:
ssh tux1@localhost             # Przez SSH
login tux1                     # Na konsoli

Wszystkie powinny zwrócić błąd uwierzytelnienia.

Sprawdzenie w logach:
sudo tail /var/log/secure | grep tux1        # RHEL/CentOS
sudo tail /var/log/auth.log | grep tux1      # Debian/Ubuntu
journalctl | grep tux1

Typowe komunikaty błędów:
"Authentication failure"
"Account locked"
"Login incorrect"

Test z nieprawidłowym hasłem vs zablokowane konto:
# Zablokowane konto: błąd nawet z prawidłowym hasłem
# Nieprawidłowe hasło: błąd tylko z nieprawidłowym hasłem

Sprawdzenie statusu w różny sposób:
sudo passwd -S tux1            # Status hasła
id tux1                        # Sprawdź czy konto istnieje
getent passwd tux1             # Informacje o koncie

Weryfikacja że inne konto działa:
su - tux2                      # Powinno działać normalnie

Monitor prób logowania:
sudo tail -f /var/log/secure &  # Monitor w tle
# Spróbuj zalogować się jako tux1
# Sprawdź logi

Sprawdzenie PAM (Pluggable Authentication Modules):
grep tux1 /var/log/secure | grep pam
```

---

### 6. Odblokuj konto użytkownika tux1.

```
Odblokowanie konta tux1:
sudo usermod -U tux1

Alternatywne metody odblokowania:
sudo passwd -u tux1            # Unlock password

Jeśli użyto chage -E 0:
sudo chage -E -1 tux1          # Usuń datę wygaśnięcia

Sprawdzenie czy konto jest odblokowane:
sudo passwd -S tux1
# Powinno pokazać "P" (Password set)

Sprawdzenie w /etc/shadow:
sudo grep tux1 /etc/shadow
# "!" na początku hasła powinno być usunięte

Weryfikacja statusu:
chage -l tux1

Test logowania po odblokowaniu:
su - tux1
# Powinno działać z oryginalnym hasłem

Sprawdzenie historii zmian:
sudo grep tux1 /var/log/secure | tail -5

Pełna weryfikacja:
# 1. Status hasła
sudo passwd -S tux1

# 2. Informacje o koncie  
chage -l tux1

# 3. Test logowania
echo "Testowanie logowania..."
su - tux1 -c "whoami"

# 4. Sprawdzenie w shadow
sudo grep tux1 /etc/shadow | cut -d: -f2

Różne metody odblokowania w zależności od metody blokowania:
# Po usermod -L lub passwd -l:
sudo usermod -U tux1
# lub
sudo passwd -u tux1

# Po chage -E 0:
sudo chage -E -1 tux1
# lub ustaw konkretną datę w przyszłości
sudo chage -E 2025-12-31 tux1
```

---

### 7. Zmodyfikuj parametry starzenia się hasła dla tux1 tak, aby przy następnym logowaniu tux1 był zmuszony zresetować swoje hasło.

```
Wymuszenie zmiany hasła przy następnym logowaniu:
sudo chage -d 0 tux1

Alternatywna metoda:
sudo passwd -e tux1            # Expire password

Sprawdzenie ustawień starzenia hasła:
chage -l tux1

Ustawienie innych parametrów starzenia hasła:
sudo chage -M 90 tux1          # Maksymalny wiek hasła: 90 dni
sudo chage -m 1 tux1           # Minimalny wiek hasła: 1 dzień
sudo chage -W 7 tux1           # Ostrzeżenie 7 dni przed wygaśnięciem
sudo chage -I 30 tux1          # Nieaktywność: 30 dni po wygaśnięciu

Sprawdzenie wszystkich ustawień:
chage -l tux1

Przykładowe wyjście:
Last password change: Jan 01, 1970
Password expires: never
Password inactive: never
Account expires: never
Minimum number of days between password change: 0
Maximum number of days between password change: 99999
Number of days of warning before password expires: 7

Po ustawieniu chage -d 0:
Last password change: password must be changed

Sprawdzenie w /etc/shadow:
sudo grep tux1 /etc/shadow
# Trzecie pole (data ostatniej zmiany) powinno być 0

Interaktywne ustawienie wszystkich parametrów:
sudo chage tux1

Test ustawień:
# Sprawdź czy hasło wymaga zmiany
sudo passwd -S tux1 | grep "must change"

Domyślne ustawienia dla nowych użytkowników:
cat /etc/login.defs | grep -E "PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_WARN_AGE"
```

---

### 8. Ponownie, w innym terminalu, zaloguj się jako tux1. czy to działa? Czy poproszono Cię o zmianę hasła?

```
Test logowania z wymuszeniem zmiany hasła:
su - tux1

Oczekiwany przebieg:
1. Zostaniesz poproszony o aktualne hasło
2. System poprosi o nowe hasło
3. Zostaniesz poproszony o potwierdzenie nowego hasła

Przykładowy przebieg:
Password: <wprowadź_stare_hasło>
You are required to change your password immediately (password aged)
New password: <wprowadź_nowe_hasło>
Retype new password: <potwierdź_nowe_hasło>

Po pomyślnej zmianie:
passwd: password updated successfully

Sprawdzenie czy zmiana się udała:
whoami
id
chage -l tux1

Test z SSH:
ssh tux1@localhost
# Powinno również wymusić zmianę hasła

Sprawdzenie logów:
sudo tail /var/log/secure | grep tux1

Sprawdzenie daty ostatniej zmiany hasła:
chage -l tux1 | grep "Last password change"
# Powinno pokazać aktualną datę

Weryfikacja w /etc/shadow:
sudo grep tux1 /etc/shadow
# Trzecie pole powinno pokazywać liczbę dni od 1970-01-01

Obliczenie daty zmiany hasła:
# Jeśli w shadow jest np. 19358, to:
date -d "1970-01-01 + 19358 days"

Test logowania po zmianie:
exit                           # Wyjdź z sesji tux1
su - tux1                      # Zaloguj się ponownie
# Nie powinno już prosić o zmianę hasła

Sprawdzenie polityki haseł:
# Sprawdź czy nowe hasło spełnia wymagania
grep -E "^password.*pam_cracklib|^password.*pam_pwquality" /etc/pam.d/passwd
```

---

### 9. Utwórz dodatkową grupę „pingwiny". Uczyń użytkowników „tux1" i „tux2" członkami tej grupy.

```
Utworzenie grupy pingwiny:
sudo groupadd pingwiny

Dodanie użytkowników do grupy:
sudo usermod -aG pingwiny tux1
sudo usermod -aG pingwiny tux2

Sprawdzenie utworzenia grupy:
getent group pingwiny
grep pingwiny /etc/group

Sprawdzenie członkostwa w grupie:
groups tux1
groups tux2
id tux1
id tux2

Alternatywne metody dodawania do grupy:
sudo gpasswd -a tux1 pingwiny
sudo gpasswd -a tux2 pingwiny

Sprawdzenie wszystkich grup użytkownika:
id -Gn tux1                    # Nazwy grup
id -G tux1                     # GID grup

Lista wszystkich członków grupy:
getent group pingwiny | cut -d: -f4
grep pingwiny /etc/group | cut -d: -f4

Sprawdzenie GID grupy:
getent group pingwiny | cut -d: -f3

Test zmian (wymaga ponownego zalogowania):
su - tux1
groups                         # Sprawdź czy pingwiny jest na liście
id                            # Sprawdź GID

Tworzenie grupy z konkretnym GID:
sudo groupadd -g 1500 pingwiny # Gdyby grupa nie istniała

Sprawdzenie czy grupa została dodana jako dodatkowa:
# Podstawowa grupa użytkownika nie powinna się zmienić
id tux1 | grep -o "gid=[0-9]*([^)]*)"
# Dodatkowe grupy:
id tux1 | grep -o "groups=.*"
```

---

### 10. Przyjrzyj się różnym plikom przechowującym informacje o użytkownikach, aby zobaczyć, jak administrowana jest ta grupa pomocnicza.

```
Sprawdzenie w /etc/group:
grep pingwiny /etc/group

Format linii w /etc/group:
group_name:password:GID:member_list

Analiza wpisu:
pingwiny:x:1001:tux1,tux2

Sprawdzenie w /etc/gshadow:
sudo grep pingwiny /etc/gshadow

Format /etc/gshadow:
group_name:password:administrators:members

Sprawdzenie podstawowych grup użytkowników:
# Podstawowa grupa tux1:
id tux1 | grep -o "gid=[0-9]*([^)]*)"

# Podstawowa grupa tux2:
id tux2 | grep -o "gid=[0-9]*([^)]*)"

Sprawdzenie wszystkich grup każdego użytkownika:
getent group | grep tux1
getent group | grep tux2

Lista wszystkich grup w systemie:
cat /etc/group | cut -d: -f1 | sort

Sprawdzenie członkostwa odwrotnie (kto należy do jakiej grupy):
for group in $(cut -d: -f1 /etc/group); do
    members=$(getent group $group | cut -d: -f4)
    if [[ -n $members ]]; then
        echo "$group: $members"
    fi
done

Sprawdzenie uprawnień plików grupowych:
ls -la /etc/group /etc/gshadow

Analiza różnic w reprezentacji grupy:
# W /etc/passwd użytkownicy mają podstawową grupę (GID)
grep "tux[12]" /etc/passwd | cut -d: -f1,4

# W /etc/group dodatkowe grupy są w liście członków
grep pingwiny /etc/group

Administracja grupy:
# Dodawanie/usuwanie członków:
sudo gpasswd -a username pingwiny      # Dodaj
sudo gpasswd -d username pingwiny      # Usuń

# Ustawianie administratora grupy:
sudo gpasswd -A tux1 pingwiny

# Ustawianie hasła grupy (rzadko używane):
sudo gpasswd pingwiny

Sprawdzenie efektywnych grup po zalogowaniu:
su - tux1 -c "groups"
su - tux2 -c "groups"

Sprawdzenie z newgrp:
su - tux1 -c "newgrp pingwiny && id"
```

---

### 11. Utwórz katalog grupy, /home/pingwiny. Ustaw odpowiednie uprawnienia w tym katalogu, aby użytkownicy tux1 i tux2 mogli pracować razem nad projektem w tym katalogu.

```
Utworzenie katalogu grupy:
sudo mkdir /home/pingwiny

Ustawienie właściciela i grupy:
sudo chown :pingwiny /home/pingwiny

Ustawienie uprawnień dla współpracy grupowej:
sudo chmod 2775 /home/pingwiny

Wyjaśnienie uprawnień 2775:
2 = SGID (Set Group ID) - nowe pliki dziedziczą grupę katalogu
7 = rwx dla właściciela (root)
7 = rwx dla grupy (pingwiny)
5 = r-x dla innych

Sprawdzenie uprawnień:
ls -ld /home/pingwiny

Powinno pokazać:
drwxrwsr-x 2 root pingwiny 4096 Oct 23 10:30 /home/pingwiny
#    ^
#    s = SGID bit

Test działania:
# Jako tux1:
su - tux1
cd /home/pingwiny
touch plik_tux1.txt
echo "Treść od tux1" > plik_tux1.txt
ls -la

# Jako tux2:
su - tux2
cd /home/pingwiny
echo "Dodane przez tux2" >> plik_tux1.txt
touch plik_tux2.txt
ls -la

Sprawdzenie dziedziczenia grupy:
ls -la /home/pingwiny/
# Wszystkie pliki powinny mieć grupę 'pingwiny'

Dodatkowe ustawienia dla lepszej współpracy:
# Ustaw umask dla członków grupy
echo "umask 002" >> /home/tux1/.bashrc
echo "umask 002" >> /home/tux2/.bashrc

Alternatywne podejście z ACL (Access Control Lists):
# Jeśli system obsługuje ACL:
sudo setfacl -d -m g:pingwiny:rwx /home/pingwiny
sudo setfacl -m g:pingwiny:rwx /home/pingwiny

Sprawdzenie ACL:
getfacl /home/pingwiny

Test uprawnień:
# Sprawdź czy obaj użytkownicy mogą:
# 1. Tworzyć pliki
# 2. Czytać pliki innych
# 3. Modyfikować pliki innych
# 4. Tworzyć podkatalogi

Przykład struktury projektu:
sudo mkdir -p /home/pingwiny/{docs,src,tests}
sudo chown -R :pingwiny /home/pingwiny
sudo chmod -R 2775 /home/pingwiny

Weryfikacja pełnych uprawnień:
find /home/pingwiny -exec ls -ld {} \;
```

---

### 12. Przejrzyj na informacje o starzeniu się hasła dla tux1.

```
Sprawdzenie informacji o starzeniu hasła:
chage -l tux1

Szczegółowa analiza każdego pola:

Last password change (Data ostatniej zmiany):
# Pokazuje kiedy hasło było ostatnio zmieniane

Password expires (Hasło wygasa):
# Data wygaśnięcia hasła

Password inactive (Hasło nieaktywne):
# Ile dni po wygaśnięciu konto zostanie zablokowane

Account expires (Konto wygasa):
# Data wygaśnięcia całego konta

Minimum number of days between password change:
# Minimalna liczba dni między zmianami hasła

Maximum number of days between password change:
# Maksymalna liczba dni między zmianami hasła

Number of days of warning before password expires:
# Ostrzeżenia przed wygaśnięciem

Sprawdzenie w pliku shadow:
sudo grep tux1 /etc/shadow

Format pól w /etc/shadow:
username:password:lastchange:min:max:warn:inactive:expire:reserved

Obliczenie dat z /etc/shadow:
# Pole 3 (lastchange) to dni od 1970-01-01
lastchange=$(sudo grep tux1 /etc/shadow | cut -d: -f3)
date -d "1970-01-01 + $lastchange days"

Sprawdzenie statusu hasła:
sudo passwd -S tux1

Interpretacja statusu:
# P = Password set (hasło ustawione)
# L = Locked (zablokowane)
# N = No password (brak hasła)

Sprawdzenie domyślnych ustawień systemu:
grep -E "PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_WARN_AGE|PASS_MIN_LEN" /etc/login.defs

Interaktywna zmiana ustawień:
sudo chage tux1

Sprawdzenie czy hasło wymaga zmiany:
sudo passwd -S tux1 | grep "must change"

Przykład ustawienia wszystkich parametrów:
sudo chage -m 7 -M 90 -W 14 -I 30 -E 2024-12-31 tux1

Wyjaśnienie parametrów:
-m 7: minimum 7 dni między zmianami
-M 90: maksimum 90 dni ważności hasła
-W 14: ostrzeżenie 14 dni przed wygaśnięciem
-I 30: 30 dni nieaktywności po wygaśnięciu
-E 2024-12-31: konto wygasa 31 grudnia 2024

Sprawdzenie po zmianach:
chage -l tux1
```

---

### 13. Zobacz, ile procesów ma już twój użytkownik uruchomionych.

```
Sprawdzenie procesów bieżącego użytkownika:
ps -u $(whoami)

Sprawdzenie liczby procesów:
ps -u $(whoami) | wc -l

Sprawdzenie procesów tux1:
ps -u tux1
ps -U tux1                     # Alternative

Liczba procesów dla tux1:
ps -u tux1 --no-headers | wc -l

Szczegółowe informacje o procesach:
ps -f -u tux1                  # Full format
ps aux | grep "^tux1"         # Z wszystkimi informacjami

Drzewo procesów:
pstree -u tux1
ps -f --forest -u tux1

Sprawdzenie dla wszystkich użytkowników:
ps aux | awk '{print $1}' | sort | uniq -c | sort -nr

Sprawdzenie aktywnych sesji:
who
w
users

Procesy według PID:
ps -e -o pid,user,comm | grep tux1

Sprawdzenie zasobów używanych przez procesy:
top -u tux1
htop -u tux1                   # Jeśli zainstalowane

Statystyki procesów:
ps -eo user,pid,pcpu,pmem,comm | grep tux1

Sprawdzenie procesów wszystkich użytkowników tux:
ps aux | grep "^tux[12]"

Monitorowanie procesów w czasie rzeczywistym:
watch "ps -u tux1 --no-headers | wc -l"

Sprawdzenie limitów procesów:
ulimit -u                      # Limit procesów dla bieżącego użytkownika
cat /etc/security/limits.conf | grep nproc

Sprawdzenie procesów zombie:
ps aux | awk '$8 ~ /^Z/ { print $2, $11 }'

Sprawdzenie procesów uruchomionych przez konkretnego użytkownika:
sudo lsof -u tux1              # Otwarte pliki i procesy

Sprawdzenie sesji systemd:
loginctl list-sessions
loginctl show-user tux1

Historia procesów:
last tux1                      # Historia logowań
```

---

### Dodatkowe polecenia zarządzania użytkownikami

```
Zarządzanie użytkownikami:
sudo useradd username          # Dodaj użytkownika
sudo userdel username          # Usuń użytkownika
sudo userdel -r username       # Usuń z katalogiem domowym
sudo usermod options username  # Modyfikuj użytkownika

Zarządzanie grupami:
sudo groupadd groupname        # Dodaj grupę
sudo groupdel groupname        # Usuń grupę
sudo groupmod options groupname # Modyfikuj grupę

Zarządzanie hasłami:
sudo passwd username           # Zmień hasło
sudo passwd -e username        # Wymuś zmianę hasła
sudo passwd -l username        # Zablokuj hasło
sudo passwd -u username        # Odblokuj hasło

Informacje o użytkownikach:
id username                    # UID, GID, grupy
groups username                # Grupy użytkownika
finger username                # Szczegółowe informacje
getent passwd username         # Informacje z bazy użytkowników

Monitoring:
who                           # Zalogowani użytkownicy
w                            # Aktywność użytkowników
last                         # Historia logowań
lastlog                      # Ostatnie logowanie każdego użytkownika

Bezpieczeństwo:
sudo chage -l username        # Informacje o starzeniu hasła
sudo faillog -u username     # Nieudane próby logowania
sudo passwd -S username      # Status hasła
```
