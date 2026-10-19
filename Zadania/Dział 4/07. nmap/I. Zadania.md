![](../../../grafiki/4-07-zadania.png)

# Zadania – nmap

> **Wszystkie zadania wykonujesz wyłącznie na własnej maszynie szkoleniowej i w sieci szkoleniowej.** Skanowanie innych adresów jest zabronione – to nie tylko zasada kursu, ale też prawa. Tam, gdzie zadanie mówi o „drugiej maszynie”, użyj maszyny sąsiada **za jego zgodą** albo drugiej własnej maszyny.

**1.** Zainstaluj nmap i sprawdź jego wersję.

**2.** Przeskanuj własną maszynę (`localhost`). Zanotuj, które porty są otwarte, a następnie porównaj wynik z listą usług nasłuchujących według `ss`. Czy listy się pokrywają?

**3.** Sprawdź, które hosty w sieci szkoleniowej odpowiadają – bez skanowania ich portów.

**4.** Przeskanuj drugą maszynę (za zgodą!) i porównaj wynik ze skanem jej `localhost` wykonanym przez właściciela. Jeśli wyniki się różnią – wyjaśnij, co je różni i dlaczego.

**5.** Na drugiej maszynie uruchom serwer WWW (`sudo dnf install httpd && sudo systemctl start httpd`), ale **nie otwieraj** portu na firewallu. Przeskanuj port 80 z zewnątrz – jaki stan zobaczysz? Następnie otwórz usługę http na firewallu i przeskanuj ponownie.

**6.** Sprawdź wersje usług na otwartych portach drugiej maszyny. Jaka dokładnie wersja serwera SSH tam działa?

**7.** Przeskanuj wszystkie 65535 portów TCP własnej maszyny z przyspieszeniem i bez zapytań DNS. Zmierz, ile trwał skan (podpowiedź: nmap sam to wypisuje).

**8.** Wykonaj na własnej maszynie skan z zapisem wyników we wszystkich formatach do plików o nazwie zaczynającej się od dzisiejszej daty. Obejrzyj różnice między plikami `.nmap` i `.gnmap`.

**9.** Sprawdź, czy nmap potrafi odgadnąć system operacyjny drugiej maszyny. Porównaj wynik z zawartością `/etc/os-release` na niej.

**10.** (Dla dociekliwych) Podczas gdy kolega skanuje Twoją maszynę skanem `-sT` na port 22, obserwuj logi `sshd` na żywo. Czy widzisz ślad skanowania? A przy skanie `-sS`?

> **Wskazówka:** jeśli skan „nie widzi” maszyny, która na pewno działa, jej firewall może blokować

> pakiety rozpoznawcze – przypomnij sobie, która opcja każe skanować mimo to.
