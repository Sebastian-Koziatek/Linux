![](../../grafiki/rozwiazania-16-firewalld.png)

# Rozwiązania – Firewalld

## Rozeznanie

**1. Stan usługi, aktywna strefa i jej zawartość:**

```bash
sudo firewall-cmd --state
sudo systemctl is-enabled firewalld
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
```

```text
running
enabled
public
  interfaces: enp1s0
public (active)
  target: default
  interfaces: enp1s0
  services: dhcpv6-client ssh
  ports:
```

`--state` odpowiada `running` albo `not running`, `--get-active-zones` pokazuje strefę wraz z przypisaną kartą, a `--list-all` wypisuje całą zawartość strefy: usługi, porty i reguły rozszerzone. Świeży RHEL ma w strefie `public` tylko `ssh` i `dhcpv6-client`.

---

## Otwieranie usług

**2. HTTP i HTTPS na stałe:**

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https

# lista jeszcze sprzed przeładowania - pokazuje konfigurację bieżącą
sudo firewall-cmd --list-services
```

```text
dhcpv6-client ssh
```

```bash
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

```text
dhcpv6-client http https ssh
```

Firewalld trzyma dwie konfiguracje: **bieżącą** (w pamięci, działa od razu) i **trwałą** (na dysku, przeżywa restart). Opcja `--permanent` zapisuje regułę tylko do tej drugiej, dlatego do czasu `--reload` polecenia bez `--permanent` pokazują stary stan. Stąd zasada: `--permanent` + `--reload`.

---

## Porty i usługi własne

**3. Port 8080/tcp i sprawdzenie gotowych usług:**

```bash
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

```text
8080/tcp
```

```bash
# czy firewalld zna gotową usługę "mysql"
sudo firewall-cmd --get-services | tr ' ' '\n' | grep -x mysql
```

```text
mysql
```

Usługa to nazwany zestaw portów opisany w pliku XML (`/usr/lib/firewalld/services/`). Jeśli taka usługa istnieje, lepiej użyć `--add-service=mysql` niż numeru portu — reguła jest czytelniejsza. Port otwieramy wtedy, gdy gotowej usługi nie ma.

---

## Dostęp z wybranej sieci

**4. SSH tylko z sieci 192.168.10.0/24:**

```bash
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="ssh" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```

```text
public (active)
  services: dhcpv6-client http https
  ports: 8080/tcp
  rich rules:
	rule family="ipv4" source address="192.168.10.0/24" service name="ssh" accept
```

Najpierw znika ogólne zezwolenie na ssh (bez tego reguła rozszerzona niczego by nie zawężała — ruch i tak byłby wpuszczany), a potem wchodzi reguła dopuszczająca ssh wyłącznie ze wskazanej sieci. **Wykonuj to z konsoli maszyny albo z adresu należącego do tej sieci**, inaczej odetniesz sobie własne połączenie.

---

## Sprzątanie i sytuacja awaryjna

**5. Cofnięcie zmian i tryb paniki:**

```bash
sudo firewall-cmd --permanent --remove-service=http
sudo firewall-cmd --permanent --remove-service=https
sudo firewall-cmd --permanent --remove-port=8080/tcp
sudo firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="ssh" accept'
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```

```text
public (active)
  services: dhcpv6-client ssh
  ports:
  rich rules:
```

```bash
sudo firewall-cmd --panic-on      # odcina cały ruch sieciowy
sudo firewall-cmd --query-panic
sudo firewall-cmd --panic-off     # powrót do normalnej pracy
```

```text
yes
```

Każde usunięcie jest odwrotnością dodania (`--remove-*` zamiast `--add-*`) i również wymaga `--reload`. Tryb paniki blokuje **cały** ruch, łącznie z Twoją sesją SSH — używa się go przy podejrzeniu włamania i tylko z dostępem do konsoli maszyny.
