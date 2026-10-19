![](../../../grafiki/4-09-zadania.png)

# Zadania – Certyfikat SSL w Apache

> Zadania wykonuj na swojej maszynie szkoleniowej. Pracujemy na certyfikacie samopodpisanym, bo maszyny nie mają publicznej domeny – procedury są identyczne jak przy certyfikacie od CA.

**1.** Zainstaluj Apache z modułem SSL, włącz i uruchom usługę. Sprawdź, że moduł `ssl` jest załadowany, i umieść w katalogu strony prosty plik `index.html`.

**2.** Wygeneruj certyfikat samopodpisany ważny 365 dni dla nazwy `serwer.example.com`: klucz do `/etc/pki/tls/private/serwer.key`, certyfikat do `/etc/pki/tls/certs/serwer.crt`. Ustaw właściwe uprawnienia obu plików.

**3.** Obejrzyj wystawiony certyfikat: dla kogo jest, kto go wystawił i do kiedy jest ważny. Co ciekawego widać w polach subject i issuer certyfikatu samopodpisanego?

**4.** Wskaż oba pliki w konfiguracji SSL Apache'a, przetestuj składnię konfiguracji i zrestartuj usługę.

**5.** Otwórz na firewallu usługi `http` i `https` na stałe. Sprawdź listę przepuszczanych usług.

**6.** Przetestuj stronę: najpierw `curl https://localhost` bez dodatkowych opcji, potem tak, żeby test się powiódł. Wyjaśnij, czemu pierwsza próba kończy się błędem i dlaczego to prawidłowe zachowanie.

**7.** Skonfiguruj przekierowanie całego ruchu z portu 80 na HTTPS i udowodnij poleceniem `curl`, że serwer odpowiada kodem 301 ze wskazaniem adresu `https://…`.

**8.** Sprawdź, czy klucz prywatny pasuje do certyfikatu, porównując skróty kluczy publicznych z obu plików.

**9.** Przećwicz podmianę certyfikatu: wygeneruj drugi certyfikat (ważny np. 30 dni), zrób kopię zapasową obecnych plików, wgraj nowe, przetestuj konfigurację, przeładuj Apache'a i potwierdź przez `openssl s_client`, że serwer podaje już nową datę ważności.

**10.** Zasymuluj awarię: ustaw w konfiguracji ścieżkę do nieistniejącego pliku klucza i uruchom test składni. Jak Apache zgłasza problem? Przywróć poprawną konfigurację.

**11.** (Dla dociekliwych) Sprawdź kontekst SELinux plików certyfikatu i klucza. Skopiuj certyfikat do `/tmp`, porównaj kontekst kopii i wyjaśnij, czemu trzymanie certyfikatów we właściwych katalogach oszczędza kłopotów.

> **Wskazówka:** przy każdej zmianie konfiguracji obowiązuje rytuał

> `apachectl configtest && systemctl reload httpd` – w tej kolejności.
