#!/usr/bin/env python3
"""Kontrola spójności materiałów.

Użycie:  python3 narzedzia/sprawdz.py [--usun-osierocone]

Sprawdza:
  * odnośniki do grafik w plikach .md wskazują istniejące pliki,
  * linki do innych lekcji (.md) wskazują istniejące pliki,
  * każdy plik w grafiki/*.png jest gdzieś użyty (osierocone można usunąć),
  * każda grafika D-MM-*.png ma źródło w grafiki/zrodla/,
  * nie zostały katalogi _stare,
  * każdy moduł ma „0. O module.md”, a lekcje mają sensowną długość.
"""
import os
import re
import sys
import urllib.parse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAFIKI = os.path.join(REPO, 'grafiki')
ZRODLA = os.path.join(GRAFIKI, 'zrodla')
MIN_ZNAKOW, MAX_ZNAKOW = 2500, 12000
LINK = re.compile(r'(!?)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')

bledy, uwagi = [], []
uzyte_grafiki = set()
md_pliki = []
for katalog, podkatalogi, pliki in os.walk(REPO):
    podkatalogi[:] = [d for d in podkatalogi if d not in ('.git', 'node_modules', '.obsidian')]
    if os.path.basename(katalog) == '_stare' or '/_stare/' in katalog + '/':
        bledy.append(f'Pozostał katalog _stare: {os.path.relpath(katalog, REPO)}')
        podkatalogi[:] = []
        continue
    for p in pliki:
        if p.endswith('.md'):
            md_pliki.append(os.path.join(katalog, p))

for sciezka in sorted(md_pliki):
    rel = os.path.relpath(sciezka, REPO)
    if rel.startswith('narzedzia'):
        continue
    tekst = open(sciezka, encoding='utf-8').read()
    tekst_bez_kodu = re.sub(r'```.*?```', '', tekst, flags=re.S)
    for obraz, cel in LINK.findall(tekst_bez_kodu):
        if cel.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        cel_czysty = urllib.parse.unquote(cel.split('#')[0])
        pelna = os.path.normpath(os.path.join(os.path.dirname(sciezka), cel_czysty))
        if not os.path.exists(pelna):
            bledy.append(f'{rel}: brak celu odnośnika „{cel}”')
            continue
        if pelna.startswith(GRAFIKI + os.sep):
            uzyte_grafiki.add(os.path.relpath(pelna, GRAFIKI))
            if not cel.startswith('../../grafiki/') and not rel.startswith('README'):
                uwagi.append(f'{rel}: odnośnik do grafiki nie w konwencji ../../grafiki/: „{cel}”')
    if re.search(r'<h\d[^>]*align', tekst):
        uwagi.append(f'{rel}: nagłówki HTML <h2 align> zamiast Markdown')
    if re.match(r'(Dział|Zadania)', rel) and not os.path.basename(rel).startswith('0. '):
        n = len(tekst)
        prog = 1200 if rel.startswith('Zadania') else MIN_ZNAKOW
        if n < prog:
            uwagi.append(f'{rel}: tylko {n} znaków')
        elif n > MAX_ZNAKOW:
            uwagi.append(f'{rel}: aż {n} znaków – rozważ podział')

for dzial in sorted(d for d in os.listdir(REPO) if d.startswith('Dział')):
    for modul in sorted(os.listdir(os.path.join(REPO, dzial))):
        pelna = os.path.join(REPO, dzial, modul)
        if os.path.isdir(pelna) and not os.path.exists(os.path.join(pelna, '0. O module.md')):
            bledy.append(f'{dzial}/{modul}: brak „0. O module.md”')

obrazy = sorted(f for f in os.listdir(GRAFIKI) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')))
osierocone = [f for f in obrazy if f not in uzyte_grafiki]
for f in obrazy:
    if re.match(r'\d-\d\d-', f) and not os.path.exists(os.path.join(ZRODLA, f[:-4] + '.html')):
        if not f.endswith(('.jpg', '.webp')):
            uwagi.append(f'grafiki/{f}: brak źródła HTML w grafiki/zrodla/ (zrzut ekranu? w porządku)')
for f in sorted(os.listdir(ZRODLA)):
    if f.endswith('.html') and not f.startswith('_') and not os.path.exists(os.path.join(GRAFIKI, f[:-5] + '.png')):
        bledy.append(f'grafiki/zrodla/{f}: niewyrenderowane (brak PNG)')

print(f'Plików .md: {len(md_pliki)}, grafik: {len(obrazy)}, użytych: {len(uzyte_grafiki)}, osieroconych: {len(osierocone)}')
for b in bledy:
    print('BŁĄD  ', b)
for u in uwagi:
    print('uwaga ', u)
if osierocone:
    print('\nOsierocone grafiki (nieużywane w żadnym .md):')
    for f in osierocone:
        print('  ', f)
    if '--usun-osierocone' in sys.argv:
        for f in osierocone:
            os.remove(os.path.join(GRAFIKI, f))
        print(f'Usunięto {len(osierocone)} plików.')
sys.exit(1 if bledy else 0)
