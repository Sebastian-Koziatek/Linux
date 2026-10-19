![](../../../grafiki/3-6-zadania.png)

# Zadania – Zabezpieczenia sieciowe

> **Ważne:** jeśli pracujesz na maszynie zdalnie przez SSH, przed każdą zmianą w zaporze upewnij się, że reguła przepuszczająca SSH (usługa `ssh` / port 22) pozostaje aktywna. Dobry nawyk: trzymaj otwartą drugą, zapasową sesję SSH na czas ćwiczeń.

**1.** Sprawdź, czy firewalld na Twojej maszynie działa, i wyświetl pełną konfigurację aktywnej strefy. Która strefa jest aktywna i jakie usługi są w niej dozwolone?

**2.** Wyświetl listę wszystkich portów, na których Twój serwer faktycznie nasłuchuje (TCP). Porównaj ją z listą usług dozwolonych w zaporze — czy zapora przepuszcza coś, co nie nasłuchuje?

**3.** Zainstaluj serwer WWW nginx, uruchom go i dodaj **na stałe** usługi `http` i `https` do strefy domyślnej. Sprawdź przeglądarką lub poleceniem `curl http://localhost`, że strona działa, a `firewall-cmd --list-services` pokazuje obie usługi.

**4.** Dodaj do zapory port `8080/tcp` — ale tylko w konfiguracji bieżącej (bez `--permanent`). Sprawdź, że jest na liście, a następnie wykonaj `firewall-cmd --reload`. Co się stało z portem i dlaczego?

**5.** Dodaj port `8080/tcp` ponownie, tym razem tak, aby przetrwał restart serwera. Zweryfikuj listą portów.

**6.** Wyświetl listę wszystkich usług zdefiniowanych w firewalld i znajdź wśród nich usługę odpowiadającą PostgreSQL. Jakiego portu dotyczy? (Podpowiedź: definicje leżą w `/usr/lib/firewalld/services/`.)

**7.** Utwórz własną usługę firewalld o nazwie `aplikacja` dla portu `9000/tcp` (plik XML w `/etc/firewalld/services/`), a następnie dodaj ją na stałe do strefy domyślnej i zweryfikuj.

**8.** Za pomocą rich rule ogranicz dostęp do usługi `cockpit` tak, aby była osiągalna wyłącznie z sieci `192.168.10.0/24`. Usuń najpierw ogólną usługę `cockpit` ze strefy. Wyświetl rich rules po zmianie.

**9.** Usuń z zapory wszystko, co dodałeś w zadaniach 3–8 (usługi `http`, `https`, `aplikacja`, port `8080/tcp`, rich rule), i przywróć usługę `cockpit`. Zweryfikuj, że `--list-all` wygląda jak na początku ćwiczeń.

**10.** Wyjaśnij własnymi słowami różnicę między celami `DROP` i `REJECT`. Co zobaczy osoba łącząca się z zablokowanym portem w każdym z tych wariantów i kiedy który wybierzesz?

**11.** Wypisz bieżące reguły iptables z licznikami pakietów i numerami linii. Czy widzisz w nich ślad działania firewalld?

**12.** Korzystając z iptables, zablokuj cały ruch przychodzący z adresu `192.168.10.240`, a następnie wyświetl reguły, sprawdź numer dodanej reguły i usuń ją po numerze.

**13.** Ułóż (na kartce lub w pliku tekstowym) komplet poleceń iptables dla serwera WWW: pętla lokalna, połączenia nawiązane, SSH, HTTP, HTTPS, polityka domyślna DROP — w kolejności, która nie odetnie Ci zdalnego dostępu. Uzasadnij kolejność dwóch pierwszych reguł.

**14.** Sprawdź bieżącą wartość parametru jądra `net.ipv4.ip_forward`. Czy Twoja maszyna przekazuje pakiety? Kiedy wartość `1` byłaby uzasadniona?

**15.** Utwórz plik `/etc/sysctl.d/99-cwiczenie.conf` ustawiający `net.ipv4.conf.all.log_martians = 1` oraz `net.ipv4.tcp_syncookies = 1`, wczytaj go bez restartu systemu i zweryfikuj obie wartości. Na koniec usuń plik i wczytaj konfigurację ponownie.

**16.** Scenariusz do przemyślenia: administrator dodał usługę `http` poleceniem `firewall-cmd --permanent --add-service=http`, ale strona nadal nie działa. Po restarcie serwera strona zaczęła działać. Wyjaśnij, co się wydarzyło i jakiego polecenia zabrakło.
