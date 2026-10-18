# Rozwiązania – Screen i tmux

1. Instalacja i wersje:
```bash
sudo dnf install tmux
sudo dnf install epel-release
sudo dnf install screen
tmux -V
screen --version
```
`tmux` jest w standardowych repozytoriach RHEL, `screen` dopiero w EPEL.

2. Sesja i odłączenie:
```bash
tmux new -s cwiczenia
for i in {1..300}; do echo "linia $i"; sleep 1; done >> /tmp/tmux-test.log
```
Odłączenie: `Ctrl+b`, puść, potem `d` – na ekranie pojawi się `[detached (from session cwiczenia)]`.

3. Dowód życia i powrót:
```bash
tail -f /tmp/tmux-test.log    # liczby przyrastają, Ctrl+C kończy podgląd
tmux attach -t cwiczenia
```
Pętla działała cały czas, bo jej powłoka żyje pod serwerem tmux, nie pod SSH.

4. Panele:
```bash
# Ctrl+b %  – podział pionowy; przejście między panelami: Ctrl+b + strzałka
sudo journalctl -f            # lewy panel
logger "test z tmuksa"        # prawy panel
```
Wpis `test z tmuksa` pojawia się w lewym panelu. Prawy panel zamkniesz przez `exit`
albo `Ctrl+b x` (z potwierdzeniem).

5. Wiele sesji:
```bash
tmux ls
tmux new -s druga             # Ctrl+b d, żeby się odłączyć
tmux attach -t cwiczenia
```
Wewnątrz tmuksa nową sesję tworzy się też bez zagnieżdżania: `Ctrl+b :` i polecenie `new -s druga`.

6. To samo w screen:
```bash
screen -S klasyk
for i in {1..300}; do echo "linia $i"; sleep 1; done >> /tmp/screen-test.log
# odłączenie: Ctrl+a d
screen -ls
screen -r klasyk
```

7. Przejęcie sesji podłączonej gdzie indziej:
```bash
screen -dr klasyk
```
`-d` odłącza poprzednie podłączenie, `-r` podłącza Ciebie. W tmuksie: `tmux attach -d -t nazwa`.

8. `nohup` w tle:
```bash
nohup tar czf /tmp/etc.tar.gz /etc > /tmp/etc-tar.log 2>&1 &
# po ponownym zalogowaniu:
ls -lh /tmp/etc.tar.gz
tar tzf /tmp/etc.tar.gz > /dev/null && echo "archiwum OK"
```
Tę drogę wybierasz, gdy polecenie nie zadaje pytań i nie musisz wracać do jego terminala –
wystarczy log w pliku. Do pracy interaktywnej lepszy jest tmux.

9. Sprzątanie:
```bash
tmux kill-session -t cwiczenia
tmux kill-session -t druga
screen -S klasyk -X quit
rm -f /tmp/tmux-test.log /tmp/screen-test.log /tmp/etc.tar.gz /tmp/etc-tar.log
tmux ls
screen -ls
```
Oba listowania powinny zgłosić brak sesji (`no server running`, `No Sockets found`).
Zamiast `kill-session` możesz też wejść do sesji i zamknąć wszystkie powłoki poleceniem `exit`.
