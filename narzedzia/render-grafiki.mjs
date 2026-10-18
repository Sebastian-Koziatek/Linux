#!/usr/bin/env node
// Renderuje grafiki szkoleniowe: grafiki/zrodla/*.html  →  grafiki/*.png
//
// Użycie:
//   node narzedzia/render-grafiki.mjs              # wszystkie źródła
//   node narzedzia/render-grafiki.mjs 1-01-nosniki # tylko wybrane (nazwa bez .html)
//
// Wymaga Playwright z Chromium. Skrypt szuka pakietu `playwright` w katalogu
// wskazanym zmienną PLAYWRIGHT_DIR, a gdy jej nie ma – w sąsiednim projekcie
// ../cv (tam jest zainstalowany w tym środowisku). Nie instalujemy node_modules
// w tym repozytorium.
import { createRequire } from 'node:module';
import { readdirSync, existsSync, mkdirSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const zrodla = path.join(repo, 'grafiki', 'zrodla');
const wyjscie = path.join(repo, 'grafiki');

const playwrightDir = process.env.PLAYWRIGHT_DIR || path.resolve(repo, '..', 'cv');
let chromium;
try {
  ({ chromium } = createRequire(path.join(playwrightDir, 'noop.js'))('playwright'));
} catch {
  console.error(`Nie znaleziono pakietu playwright w ${playwrightDir}. Ustaw PLAYWRIGHT_DIR na katalog z node_modules/playwright.`);
  process.exit(1);
}

const wybrane = process.argv.slice(2);
const pliki = readdirSync(zrodla)
  .filter((f) => f.endsWith('.html') && (!f.startsWith('_') || wybrane.includes(f.replace(/\.html$/, ''))))
  .filter((f) => wybrane.length === 0 || wybrane.includes(f.replace(/\.html$/, '')))
  .sort();

if (pliki.length === 0) {
  console.error('Brak źródeł do wyrenderowania.');
  process.exit(1);
}
mkdirSync(wyjscie, { recursive: true });

// Playwright wymaga Chromium w dokładnie swojej wersji; jeśli w cache jest inna
// (np. z MCP Playwright), wskazujemy ją ręcznie. Można też podać PLAYWRIGHT_CHROMIUM.
function znajdzChromium() {
  if (process.env.PLAYWRIGHT_CHROMIUM) return process.env.PLAYWRIGHT_CHROMIUM;
  const cache = path.join(process.env.HOME || '', 'Library', 'Caches', 'ms-playwright');
  if (!existsSync(cache)) return undefined;
  const kandydaci = readdirSync(cache)
    .filter((d) => d.startsWith('chromium_headless_shell-'))
    .sort()
    .reverse()
    .map((d) => path.join(cache, d, 'chrome-headless-shell-mac-arm64', 'chrome-headless-shell'))
    .filter((p) => existsSync(p));
  return kandydaci[0];
}
const browser = await chromium.launch({ executablePath: znajdzChromium() });
const context = await browser.newContext({ deviceScaleFactor: 2, viewport: { width: 1400, height: 1000 } });
const page = await context.newPage();
let bledy = 0;
for (const plik of pliki) {
  const nazwa = plik.replace(/\.html$/, '');
  try {
    await page.goto(pathToFileURL(path.join(zrodla, plik)).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const el = page.locator('#grafika');
    if ((await el.count()) === 0) throw new Error('brak elementu #grafika');
    await el.screenshot({ path: path.join(wyjscie, `${nazwa}.png`), type: 'png' });
    console.log(`✓ ${nazwa}.png`);
  } catch (e) {
    bledy++;
    console.error(`✗ ${nazwa}: ${e.message}`);
  }
}
await browser.close();
if (!existsSync(path.join(zrodla, '_styl.css'))) console.warn('Uwaga: brak grafiki/zrodla/_styl.css');
process.exit(bledy ? 1 : 0);
