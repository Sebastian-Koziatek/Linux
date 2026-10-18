# Rozwiązania – nmap

Adresy w rozwiązaniach są przykładowe (sieć szkoleniowa `192.168.10.0/24`, druga maszyna
`192.168.10.20`) – podstaw własne.

1. Instalacja:
```bash
sudo dnf install nmap
nmap --version
```

2. Skan lokalny i porównanie:
```bash
nmap localhost
sudo ss -tulnp
```
Listy mogą się różnić: `nmap localhost` domyślnie sprawdza 1000 najpopularniejszych portów TCP,
więc nie pokaże usług na nietypowych portach ani UDP; `ss` widzi wszystko od środka.

3. Odkrywanie hostów:
```bash
sudo nmap -sn 192.168.10.0/24
```
`-sn` pomija skanowanie portów – tylko sprawdza, kto odpowiada.

4. Skan z zewnątrz kontra lokalny:
```bash
sudo nmap 192.168.10.20
```
Typowa różnica: usługa widoczna lokalnie jest z zewnątrz `filtered`, bo firewalld nie przepuszcza
do niej ruchu, albo nasłuchuje tylko na `127.0.0.1` i z zewnątrz w ogóle jej nie widać.

5. Firewall w akcji:
```bash
# na drugiej maszynie
sudo dnf install httpd && sudo systemctl start httpd
# z Twojej maszyny
sudo nmap -p 80 192.168.10.20        # STATE: filtered
# na drugiej maszynie
sudo firewall-cmd --add-service=http --permanent && sudo firewall-cmd --reload
# z Twojej maszyny
sudo nmap -p 80 192.168.10.20        # STATE: open
```
Ten sam nasłuchujący serwer, dwa różne stany – różnicę robi wyłącznie zapora.

6. Wersje usług:
```bash
sudo nmap -sV 192.168.10.20
```
Wersja SSH stoi w kolumnie VERSION, np. `OpenSSH 8.7 (protocol 2.0)`.

7. Pełny zakres portów:
```bash
sudo nmap -p- -T4 -n localhost
```
Czas skanu podaje ostatnia linia: `Nmap done: … scanned in X seconds`.

8. Zapis wyników:
```bash
sudo nmap -sV -oA 20261018-moja-maszyna localhost
ls 20261018-moja-maszyna.*
```
Powstają trzy pliki: `.nmap` (czytelny dla człowieka), `.xml` (dla narzędzi) i `.gnmap`
(jedna linia na host – wygodny dla `grep`).

9. Wykrywanie systemu:
```bash
sudo nmap -O 192.168.10.20
# na drugiej maszynie:
cat /etc/os-release
```
`-O` wymaga sudo i zgaduje po zachowaniu stosu TCP/IP – zwykle trafia w rodzinę i przybliżoną
wersję jądra, rzadko w dokładną dystrybucję. Dlatego wynik traktujemy jak hipotezę.

10. Ślad w logach:
```bash
# na Twojej maszynie
sudo journalctl -fu sshd
# kolega wykonuje: sudo nmap -sT -p 22 twoj_adres, potem sudo nmap -sS -p 22 twoj_adres
```
Skan `-sT` nawiązuje pełne połączenie i natychmiast je zrywa – sshd zapisze wpis w stylu
`banner exchange: Connection from … invalid format` albo `Connection closed/reset by … [preauth]`.
Skan `-sS` zrywa połączenie przed jego pełnym nawiązaniem, więc sshd zwykle nie loguje nic –
dlatego nazywa się go „cichym”. Ślad `-sS` zostaje za to w logach firewalla, jeśli włączysz
rejestrowanie odrzuconych pakietów.
