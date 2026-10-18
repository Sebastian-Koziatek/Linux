# Przewodnik autora materiałów

Materiały towarzyszą szkoleniu **„Administracja systemem Linux I”** (5 dni, program jsystems.pl).
Czyta je osoba, która **dopiero wchodzi w świat Linuksa** – często bez doświadczenia technicznego,
czasem administrator Windows, czasem analityk lub tester. Każda lekcja ma być zrozumiała bez
zaglądania do Google.

## 1. Struktura repozytorium

```
Dział 1 - Wprowadzenie do systemu/            moduły 01–04
Dział 2 - Podstawy pracy z systemem Linux/    moduły 05–08
Dział 3 - Zarządzanie systemem Linux/         moduły 09–14
Dział 4 - Tematy dodatkowe/                   moduły 15–23 (poza programem)
Zadania/NN. Nazwa modułu/                     I. Zadania.md + II. Rozwiązania.md
grafiki/                                      gotowe PNG
grafiki/zrodla/                               źródła HTML grafik + _styl.css
narzedzia/                                    ten przewodnik + render-grafiki.mjs
```

- Folder modułu: `NN. Nazwa modułu` (dwucyfrowy numer, kropka, spacja).
- Plik lekcji: `N. Tytuł lekcji.md` (numer bez zera wiodącego). Tytuł po polsku, bez skrótów,
  np. `3. Konfiguracja repozytoriów`, nie `3. Repo`.
- Każdy moduł ma plik `0. O module.md`: 3–5 zdań, czego uczestnik się nauczy, lista lekcji
  z linkami i czas orientacyjny.
- Podfolder `_stare/` zawiera dotychczasowe materiały do wykorzystania. Po przepisaniu modułu
  `_stare/` **usuwamy w całości** (`git rm -r`).

## 2. Szablon lekcji

Każda lekcja ma ten sam układ. Nagłówki zwykłe Markdown (`#`, `##`), **bez** `<h2 align="center">`.

```markdown
# Tytuł lekcji

> **W tej lekcji:** jedno–dwa zdania, co uczestnik będzie potrafił po jej przeczytaniu.

## Po co mi to?
Krótkie osadzenie w rzeczywistości administratora: jaki problem to rozwiązuje,
kiedy się z tym spotka. Porównanie do świata znanego uczestnikowi (Windows, biuro,
życie codzienne) mile widziane – jedno, trafne, nie wymuszone.

## Jak to działa
Wyjaśnienie pojęć od zera. Grafika, jeśli coś da się narysować.
![Opis grafiki](../../grafiki/1-03-jak-dziala-menedzer-pakietow.png)

## W praktyce
Polecenia krok po kroku. Każde polecenie w osobnym bloku ```bash``` z komentarzem,
co robi i co zobaczymy. Przykładowe wyjście w bloku ```text```.

## Najczęstsze błędy i pułapki
Lista 2–5 punktów: co początkujący robi źle i jak to rozpoznać.

## Podsumowanie
- 3–6 punktów do zapamiętania.
- Tabela „ściąga” z poleceniami, jeśli lekcja ich uczy.

## Zobacz też
Linki do powiązanych lekcji w repozytorium (ścieżka względna).
```

Długość: zwykle **3 000–8 000 znaków**. Lekcja czysto pojęciowa może być krótsza, lekcja
narzędziowa (fdisk, systemctl, firewalld) dłuższa. Nie rozbijamy jednego tematu na kilka
plików po 300 znaków – lepiej jedna pełna lekcja.

## 3. Ton i język

- Piszemy **po polsku**, zwracamy się do uczestnika na „Ty”. Zdania krótkie. Jedna myśl na akapit.
- Każdy skrót i termin angielski wyjaśniamy przy pierwszym użyciu: *repozytorium (ang. repository) –
  serwer z gotowymi pakietami…*. Potem używamy polskiego terminu konsekwentnie.
- Nazewnictwo: **menedżer pakietów** (nie manager), **demon** (nie deamon), **powłoka**,
  **jądro**, **katalog** (nie folder), **uprawnienia**, **dowiązanie symboliczne**.
- Bez memów, żartów obrazkowych, emoji w treści i w tytułach. Dopuszczalne są wypunktowania
  i tabele.
- Nie zakładamy wiedzy z innych modułów bez podlinkowania jej. Jeśli lekcja o LVM używa
  `fdisk`, link do lekcji o `fdisk`.
- Fakty techniczne muszą być prawdziwe dla **RHEL 9/10 i pochodnych (Rocky, AlmaLinux,
  CentOS Stream)** – to system szkoleniowy. Różnice dla Ubuntu/Debiana podajemy w ramce
  `> **Na Ubuntu/Debianie:** …` tylko tam, gdzie są istotne (apt, nazwy pakietów, ufw).
- Polecenia uruchamiamy jako zwykły użytkownik z `sudo`. Prompt w przykładach:
  `[admin@serwer ~]$`, a dla roota `[root@serwer ~]#`.
- Przykładowe nazwy: użytkownik `anna`, `jan`, grupa `ksiegowosc`, serwer `serwer`,
  dysk dodatkowy `/dev/sdb`, sieć `192.168.10.0/24`, brama `192.168.10.1`.

## 4. Bloki poleceń

```bash
# instalujemy serwer WWW (odpowiedź „y” na pytanie o potwierdzenie)
sudo dnf install nginx
```

```text
Zainstalowano:
  nginx-1:1.24.0-1.el9.x86_64
Zakończono!
```

- Komentarz `#` nad poleceniem mówi **po co**, nie powtarza nazwy polecenia.
- Nie wklejamy zrzutów ekranu z terminala – zawsze tekst (da się skopiować i przeszukać).
- Opcje poleceń tłumaczymy w tabeli lub liście po bloku, nie w komentarzu w jednej linii.

## 5. Grafiki

### Zasady
- Każda grafika powstaje z pliku HTML w `grafiki/zrodla/` i korzysta **wyłącznie** z klas
  z `_styl.css`. Dzięki temu wszystkie wyglądają tak samo. Żadnych zewnętrznych obrazków,
  czcionek z internetu, emoji ani clip-artów.
- Nazwa pliku: `D-MM-temat-po-polsku.html` → `grafiki/D-MM-temat-po-polsku.png`,
  gdzie `D` = numer działu, `MM` = numer modułu. Przykład: `3-09-mbr-vs-gpt`.
- W Markdown odwołujemy się ścieżką względną: `![Opis](../../grafiki/3-09-mbr-vs-gpt.png)`
  (lekcja leży dwa poziomy pod katalogiem głównym). Tekst alternatywny opisuje, co widać.
- Jedna grafika = jedna myśl. Maksymalnie ~7 elementów. Tekst w grafice po polsku, krótki.
  Jeśli trzeba tłumaczyć grafikę trzema akapitami, podziel ją na dwie.
- Rendery: `node narzedzia/render-grafiki.mjs nazwa1 nazwa2` (bez argumentów – wszystkie).
  Po wyrenderowaniu **obejrzyj PNG** i popraw, jeśli coś się nie mieści lub nakłada.

### Zrzuty ekranu
Zostawiamy tylko zrzuty rzeczywistego interfejsu graficznego (instalator, gparted, nmtui,
PuTTY, ustawienia sieci w GNOME, pulpity środowisk graficznych). Zrzuty terminala,
tabelki z PowerPointa, loga, memy i obrazki stockowe **zastępujemy** grafikami z systemu
albo blokami tekstu. Zachowane zrzuty zmieniają nazwę na nową konwencję
(`git mv grafiki/1_05_1_instalacja3.png grafiki/1-01-instalator-siec.png`).

### Dostępne komponenty (`_styl.css`)
Szkielet pliku:
```html
<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><link rel="stylesheet" href="_styl.css"></head>
<body>
<div id="grafika" class="grafika">            <!-- .waska (640 px) | domyślna 880 px | .szeroka (1100 px) -->
  <div class="tytul"><h1>Tytuł</h1><span class="pod">podtytuł</span></div>
  …
  <div class="podpis">Komentarz pod grafiką.</div>
</div>
</body></html>
```

| Klasa | Do czego | Przykład |
|---|---|---|
| `.karty` + `.karta` (`.akcent`, `.ok`, `.zle`, `.ciemna`) | porównanie 2–4 rzeczy, kafelki pojęć | `<div class="karty"><div class="karta"><h3>…</h3><p>…</p></div>…</div>` |
| `.strzalka` (`.dol`, `.dwie` + `<span>`) | strzałka między elementami we `.wiersz`/`.kolumna` | `<div class="strzalka"></div>` |
| `.kroki` + `.krok` (`.kolumna`) | proces krok po kroku, numeracja automatyczna | `<div class="kroki"><div class="krok"><h3>…</h3><p>…</p></div></div>` |
| `.warstwy` + `.warstwa.w1…w4` | stos warstw (sprzęt → jądro → powłoka) | zob. `2-05-warstwy-systemu.html` |
| `.terminal` (`.p` prompt, `.k` wyróżnienie, `.c` błąd, `.d` drugorzędne) | fragment sesji terminala wewnątrz grafiki | `<div class="terminal"><div class="pasek"><i></i><i></i><i></i><span>opis</span></div><pre>…</pre></div>` |
| `.dyski` + `.dysk` (`.uszkodzony`) + `.blok` (`.a .b .p .x .wolny`) | dyski, RAID, partycje, LVM | zob. `3-09-raid-1.html` |
| `.tabela` (`.tak`, `.nie`) | tabela porównawcza | zob. `3-09-mbr-vs-gpt.html` |
| `.drzewo` (`.kat`, `.plik`, `.op`) | drzewo katalogów z opisami | `<div class="drzewo"><span class="kat">/etc</span> <span class="op">konfiguracja</span><br>…</div>` |
| `.wezel` + `.ikona` (`.akcent`, `.morski`) | komputer/serwer/użytkownik z ikoną SVG (inline, 24×24 viewBox, stroke) | zob. `1-03-jak-dziala-menedzer-pakietow.html` |
| `.porownanie` + `.vs` | dwie kolumny „A kontra B” | `<div class="porownanie"><div class="karta">…</div><div class="vs">vs</div><div class="karta">…</div></div>` |
| `.notatka` (`.ok`, `.zle`) | ramka z wnioskiem lub ostrzeżeniem | `<div class="notatka">…</div>` |
| `.plakietka` (`.bursztyn .morski .czerwien .granat`) | mała etykieta | `<span class="plakietka bursztyn">zalecany</span>` |
| `.wiersz`, `.kolumna`, `.srodek`, `.odstep`, `.male`, `code` | układ i drobiazgi | |

Kolory: granat `#14213d` (system, tekst), bursztyn `#fca311` (akcent, strzałki), morski `#2a9d8f`
(użytkownik, dane, „OK”), czerwień `#e63946` (błąd, awaria), fiolet `#6c5ce7` (czwarty kolor, rzadko).
Nie wprowadzamy innych kolorów. Ikony: proste SVG liniowe (stroke 1.7, zaokrąglone końce),
bez wypełnień i gradientów.

## 6. Zadania

- `Zadania/NN. Nazwa modułu/I. Zadania.md` – 8–20 zadań, od prostych do złożonych, numerowane.
  Zadania mają jasno określony cel („Utwórz…”, „Sprawdź…”, „Wyjaśnij…”). Można dodać
  ramkę `> **Wskazówka:**`.
- `II. Rozwiązania.md` – te same numery, polecenie w bloku ```bash``` i jedno zdanie
  wyjaśnienia. Rozwiązania mają działać na RHEL 9/10.
- Zadania odwołują się tylko do tego, co było w module lub wcześniej.

## 7. Lista kontrolna przed oddaniem modułu

- [ ] `0. O module.md` istnieje i linkuje wszystkie lekcje.
- [ ] Każda lekcja ma pełny szablon (sekcje z pkt 2), 3–8 k znaków, polskie nazewnictwo.
- [ ] Każda grafika ma źródło w `grafiki/zrodla/`, wyrenderowany PNG został obejrzany.
- [ ] Odnośniki `![…](../../grafiki/….png)` wskazują istniejące pliki (sprawdź `ls`).
- [ ] Zrzuty terminala, memy, loga i stare diagramy z modułu usunięte z `grafiki/`
      (`git rm`), zachowane zrzuty GUI przemianowane.
- [ ] `_stare/` modułu usunięte.
- [ ] Zadania i rozwiązania modułu w `Zadania/NN. …/`.
