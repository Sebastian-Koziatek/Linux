![](../../../grafiki/4-03-rozwiazania.png)

# Rozwiązania – Samba

## 1. Instalacja i konfiguracja domyślna

```bash
sudo dnf install samba samba-common samba-client
grep '^\[' /etc/samba/smb.conf
```

Główna konfiguracja to `/etc/samba/smb.conf`; domyślnie zawiera sekcje `[global]`, `[homes]` (katalogi domowe) i `[printers]` (drukarki).

---

## 2. Udział publiczny

```bash
sudo mkdir -p /srv/publiczny
```

Dopisujemy do `/etc/samba/smb.conf`:

```text
[publiczny]
    path = /srv/publiczny
    comment = Udzial cwiczeniowy
    browsable = yes
    writable = yes
    valid users = anna
```

```bash
testparm
```

`testparm` sprawdza składnię i przy poprawnym pliku wypisuje m.in. `Loaded services file OK.`, a po naciśnięciu Enter — zinterpretowaną konfigurację.

---

## 3. Użytkownik Samby

```bash
sudo useradd -s /sbin/nologin anna
sudo smbpasswd -a anna
```

Samba trzyma własną bazę haseł w innym formacie niż `/etc/shadow` — konto systemowe daje tożsamość i uprawnienia plikowe, ale logowanie SMB weryfikuje się hasłem z bazy Samby, które trzeba założyć `smbpasswd -a`.

---

## 4. Uruchomienie usługi

```bash
sudo systemctl enable --now smb
sudo ss -tlnp | grep smbd
```

`smbd` nasłuchuje na porcie `445/tcp` (oraz historycznym 139, jeśli włączony jest NetBIOS).

---

## 5. Zapora

```bash
sudo firewall-cmd --permanent --add-service=samba
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
cat /usr/lib/firewalld/services/samba.xml
```

Usługa `samba` otwiera porty 445/tcp i 139/tcp oraz 137-138/udp (NetBIOS).

---

## 6. SELinux

```bash
sudo semanage fcontext -a -t samba_share_t "/srv/publiczny(/.*)?"
sudo restorecon -Rv /srv/publiczny
ls -Zd /srv/publiczny
```

Bez typu `samba_share_t` polityka SELinux zabroni demonowi `smbd` czytać i zapisywać pliki — udział byłby widoczny, ale każda operacja kończyłaby się odmową dostępu (i wpisem AVC w dzienniku audytu).

---

## 7. Test z klienta

```bash
# uprawnienia plikowe: anna musi móc pisać w katalogu
sudo chown anna /srv/publiczny

smbclient -L //localhost -U anna
smbclient //localhost/publiczny -U anna
```

```text
smb: \> put /etc/hostname hostname.txt
smb: \> ls
smb: \> quit
```

```bash
ls -l /srv/publiczny/hostname.txt
```

Plik należy do użytkownika `anna` — Samba wykonuje operacje plikowe z tożsamością zalogowanego konta systemowego.

---

## 8. Diagnoza „odmowy dostępu” przy zapisie

Kolejność od najczęstszej przyczyny:

```bash
# 1. uprawnienia plikowe - czy anna ma prawo zapisu w katalogu?
ls -ld /srv/publiczny

# 2. SELinux - czy katalog ma typ samba_share_t i czy są świeże odmowy?
ls -Zd /srv/publiczny
sudo ausearch -m AVC -ts recent

# 3. konfiguracja udziału - czy nie ma read only / braku w valid users?
testparm -s | sed -n '/\[publiczny\]/,/^$/p'
```

Skoro udział widać, zapora i usługa działają — zapis blokują niemal zawsze uprawnienia `rwx`, etykieta SELinux albo ustawienia samego udziału; `writable = yes` nigdy nie da więcej praw, niż pozwala system plików.
