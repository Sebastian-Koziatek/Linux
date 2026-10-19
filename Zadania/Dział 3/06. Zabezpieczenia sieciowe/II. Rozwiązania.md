![](../../../grafiki/3-06-rozwiazania.png)

# Rozwiązania – Zabezpieczenia sieciowe

## 1. Stan i konfiguracja aktywnej strefy

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
```

Na świeżym RHEL/Rocky/AlmaLinux aktywna jest strefa `public` z usługami `cockpit dhcpv6-client ssh`.

---

## 2. Porty nasłuchujące kontra zapora

```bash
sudo ss -tlnp
sudo firewall-cmd --list-services
sudo firewall-cmd --list-ports
```

`ss -tlnp` pokazuje realnie nasłuchujące usługi; porównanie z listą zapory ujawnia nadmiarowe otwarcia (dozwolone w zaporze, ale nic tam nie słucha) — warto je usuwać.

---

## 3. Serwer WWW z otwartą zaporą

```bash
sudo dnf install nginx
sudo systemctl enable --now nginx
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
curl -I http://localhost
sudo firewall-cmd --list-services
```

`--permanent` zapisuje zmianę na stałe, a `--reload` aktywuje ją natychmiast.

---

## 4. Port tylko w konfiguracji bieżącej

```bash
sudo firewall-cmd --add-port=8080/tcp
sudo firewall-cmd --list-ports      # 8080/tcp jest
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports      # pusto!
```

`--reload` odtwarza konfigurację bieżącą z trwałej — zmiana zrobiona bez `--permanent` ginie, bo w konfiguracji trwałej nigdy jej nie było.

---

## 5. Port na stałe

```bash
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

Tym razem wpis trafił do `/etc/firewalld/`, więc przetrwa i `--reload`, i restart serwera.

---

## 6. Usługa PostgreSQL

```bash
sudo firewall-cmd --get-services | tr ' ' '\n' | grep postgres
cat /usr/lib/firewalld/services/postgresql.xml
```

Usługa `postgresql` otwiera port `5432/tcp`.

---

## 7. Własna usługa

```bash
sudo tee /etc/firewalld/services/aplikacja.xml > /dev/null <<'EOF'
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>aplikacja</short>
  <description>Firmowa aplikacja na porcie 9000.</description>
  <port protocol="tcp" port="9000"/>
</service>
EOF
sudo firewall-cmd --reload
sudo firewall-cmd --permanent --add-service=aplikacja
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

Pierwszy `--reload` jest po to, by firewalld w ogóle zobaczył nowy plik usługi; dopiero potem można ją dodać do strefy.

---

## 8. Rich rule dla cockpita

```bash
sudo firewall-cmd --permanent --remove-service=cockpit
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="cockpit" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-rich-rules
```

Reguła rozszerzona łączy warunek adresu źródłowego z usługą — zwykłe `--add-service` tego nie potrafi.

---

## 9. Sprzątanie

```bash
sudo firewall-cmd --permanent --remove-service=http
sudo firewall-cmd --permanent --remove-service=https
sudo firewall-cmd --permanent --remove-service=aplikacja
sudo firewall-cmd --permanent --remove-port=8080/tcp
sudo firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="cockpit" accept'
sudo firewall-cmd --permanent --add-service=cockpit
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
sudo rm /etc/firewalld/services/aplikacja.xml
```

Usuwanie działa lustrzanie do dodawania; na końcu kasujemy też plik własnej usługi.

---

## 10. DROP a REJECT

`DROP` wyrzuca pakiet bez żadnej odpowiedzi — nadawca czeka aż do przekroczenia limitu czasu i nie wie nawet, czy serwer istnieje; stosujemy go wobec internetu. `REJECT` odsyła komunikat odmowy — nadawca natychmiast widzi „connection refused”; wygodniejszy wewnątrz własnej sieci, bo użytkownik i administrator od razu wiedzą, że to zapora.

---

## 11. Reguły iptables na maszynie z firewalld

```bash
sudo iptables -L -n -v --line-numbers
```

Na RHEL 9/10 polecenie pokaże niewiele lub nic, bo firewalld tworzy reguły bezpośrednio w nftables — pełny obraz daje `sudo nft list ruleset`.

---

## 12. Blokada adresu i usunięcie po numerze

```bash
sudo iptables -A INPUT -s 192.168.10.240 -j DROP
sudo iptables -L INPUT -n --line-numbers
sudo iptables -D INPUT <numer>
```

`--line-numbers` pokazuje pozycję reguły; `-D ŁAŃCUCH numer` usuwa dokładnie tę pozycję.

---

## 13. Zapora serwera WWW w bezpiecznej kolejności

```bash
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -P INPUT DROP
```

Reguła dla `lo` musi być pierwsza, bo z pętli lokalnej korzysta mnóstwo usług systemowych; reguła `ESTABLISHED,RELATED` chroni trwającą sesję SSH — dzięki nim polityka `DROP` ustawiona na końcu nikogo nie odcina.

---

## 14. ip_forward

```bash
sysctl net.ipv4.ip_forward
```

Na zwykłym serwerze wartość to `0` — maszyna nie przekazuje cudzych pakietów. `1` jest uzasadnione na routerze, bramie VPN albo hoście wirtualizacji/kontenerów, gdzie ruch gości musi przechodzić przez maszynę.

---

## 15. Plik sysctl

```bash
sudo tee /etc/sysctl.d/99-cwiczenie.conf > /dev/null <<'EOF'
net.ipv4.conf.all.log_martians = 1
net.ipv4.tcp_syncookies = 1
EOF
sudo sysctl -p /etc/sysctl.d/99-cwiczenie.conf
sysctl net.ipv4.conf.all.log_martians net.ipv4.tcp_syncookies
sudo rm /etc/sysctl.d/99-cwiczenie.conf
sudo sysctl --system
```

`sysctl -p <plik>` wczytuje wskazany plik bez restartu; `sysctl --system` przelicza całość konfiguracji po usunięciu pliku (uwaga: wartość ustawiona wcześniej pozostanie w jądrze do restartu, bo nic jej nie nadpisuje).

---

## 16. Scenariusz z brakującym poleceniem

Zabrakło `sudo firewall-cmd --reload`. Opcja `--permanent` zapisała usługę tylko w konfiguracji trwałej (pliki w `/etc/firewalld/`), nie zmieniając bieżącego filtrowania. Restart serwera „pomógł”, bo przy starcie firewalld wczytuje konfigurację trwałą — czyli zrobił to, co zrobiłby `--reload` od razu.
