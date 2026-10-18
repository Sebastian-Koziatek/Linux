# Rozwiązania – Certyfikat SSL w Apache

1. Instalacja i strona:
```bash
sudo dnf install httpd mod_ssl
sudo systemctl enable --now httpd
httpd -M | grep ssl
echo "<h1>Serwer szkoleniowy</h1>" | sudo tee /var/www/html/index.html
```

2. Certyfikat samopodpisany:
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/pki/tls/private/serwer.key \
  -out    /etc/pki/tls/certs/serwer.crt \
  -subj "/C=PL/O=Szkolenie/CN=serwer.example.com"
sudo chmod 600 /etc/pki/tls/private/serwer.key
sudo chmod 644 /etc/pki/tls/certs/serwer.crt
```
`-nodes` zostawia klucz bez hasła – inaczej Apache pytałby o nie przy każdym starcie.

3. Oględziny certyfikatu:
```bash
sudo openssl x509 -in /etc/pki/tls/certs/serwer.crt -noout -subject -issuer -dates
```
Subject i issuer są **identyczne** – to definicja certyfikatu samopodpisanego: wystawca
poświadcza sam siebie.

4. Konfiguracja:
```bash
sudo vi /etc/httpd/conf.d/ssl.conf
# SSLCertificateFile    /etc/pki/tls/certs/serwer.crt
# SSLCertificateKeyFile /etc/pki/tls/private/serwer.key
sudo apachectl configtest
sudo systemctl restart httpd
```

5. Firewall:
```bash
sudo firewall-cmd --permanent --add-service=http --add-service=https
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

6. Test:
```bash
curl https://localhost        # błąd: self-signed certificate
curl -k https://localhost     # działa
```
curl odmawia, bo certyfikatu nie podpisał żaden zaufany urząd – nie da się potwierdzić
tożsamości serwera. To cecha self-signed, nie usterka; `-k` świadomie pomija weryfikację
(tylko do testów!).

7. Przekierowanie:
```bash
sudo tee /etc/httpd/conf.d/przekierowanie.conf <<'EOF'
<VirtualHost *:80>
    ServerName serwer.example.com
    Redirect permanent / https://serwer.example.com/
</VirtualHost>
EOF
sudo apachectl configtest && sudo systemctl reload httpd
curl -I http://localhost
```
Nagłówki pokażą `HTTP/1.1 301 Moved Permanently` i `Location: https://serwer.example.com/`.

8. Zgodność pary klucz–certyfikat:
```bash
sudo openssl x509 -in /etc/pki/tls/certs/serwer.crt -noout -pubkey | openssl sha256
sudo openssl pkey -in /etc/pki/tls/private/serwer.key -pubout | openssl sha256
```
Oba skróty muszą być identyczne – wtedy klucz prywatny pasuje do certyfikatu.

9. Podmiana:
```bash
sudo openssl req -x509 -nodes -days 30 -newkey rsa:2048 \
  -keyout /tmp/nowy.key -out /tmp/nowy.crt -subj "/C=PL/O=Szkolenie/CN=serwer.example.com"
sudo cp /etc/pki/tls/certs/serwer.crt /etc/pki/tls/certs/serwer.crt.bak
sudo cp /etc/pki/tls/private/serwer.key /etc/pki/tls/private/serwer.key.bak
sudo cp /tmp/nowy.crt /etc/pki/tls/certs/serwer.crt
sudo cp /tmp/nowy.key /etc/pki/tls/private/serwer.key
sudo chmod 600 /etc/pki/tls/private/serwer.key
sudo restorecon -v /etc/pki/tls/certs/serwer.crt /etc/pki/tls/private/serwer.key
sudo apachectl configtest && sudo systemctl reload httpd
echo | openssl s_client -connect localhost:443 2>/dev/null | openssl x509 -noout -dates
```
`notAfter` jest teraz ok. 30 dni w przód – serwer podaje nowy certyfikat.

10. Awaria kontrolowana:
```bash
sudo sed -i 's|/etc/pki/tls/private/serwer.key|/etc/pki/tls/private/brak.key|' /etc/httpd/conf.d/ssl.conf
sudo apachectl configtest
```
Wynik: `SSLCertificateKeyFile: file '/etc/pki/tls/private/brak.key' does not exist or is empty` –
i właśnie dlatego `configtest` robi się **przed** restartem. Przywrócenie:
```bash
sudo sed -i 's|/etc/pki/tls/private/brak.key|/etc/pki/tls/private/serwer.key|' /etc/httpd/conf.d/ssl.conf
sudo apachectl configtest && sudo systemctl reload httpd
```

11. SELinux:
```bash
ls -Z /etc/pki/tls/certs/serwer.crt /etc/pki/tls/private/serwer.key
cp /etc/pki/tls/certs/serwer.crt /tmp/ && ls -Z /tmp/serwer.crt
```
W `/etc/pki/tls/...` pliki mają kontekst `cert_t`; kopia w `/tmp` dostaje `user_tmp_t`.
Gdyby Apache miał czytać certyfikat spoza właściwych katalogów, SELinux może zablokować dostęp –
trzymając pliki na swoich miejscach (lub naprawiając kontekst `restorecon`), unikasz całej klasy
błędów „Permission denied”.
