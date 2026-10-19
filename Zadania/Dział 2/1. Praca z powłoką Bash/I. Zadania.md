![](../../../grafiki/2-1-zadania.png)

# Zadania – Praca z powłoką Bash

> Zestawy odpowiadają kolejnym tematom modułu; numeracja zaczyna się od nowa w każdym z nich.

## Praca na powłoce

**1.** Sprawdź, w jakim katalogu aktualnie się znajdujesz.  

**2.** Wyświetl zawartość bieżącego katalogu.  

**3.** Utwórz nowy katalog o nazwie `szkolenie` w bieżącej lokalizacji.  

**4.** Przejdź do katalogu `szkolenie`.  

**5.** Utwórz pięć plików: `plik1`, `plik2`, `plik3`, `plik4`, `plik5` – za pomocą jednego polecenia.  

**6.** Utwórz ukryty plik o nazwie `.ukryty.txt`.  

**7.** Wyświetl pełną zawartość katalogu, łącznie z plikami ukrytymi.  

**8.** Zmień nazwę pliku `.ukryty.txt` na `plik6`.  

**9.** Zapisz tekst `Szkolenie Linux` do pliku `plik3`.  

**10.** Wyświetl zawartość pliku `plik3`.  

**11.** Z aktualnej lokalizacji utwórz folder `/tmp/test`.  

**12.** Czym jest katalog `/tmp`? Jakie ma właściwości?  

**13.** Skopiuj całą zawartość bieżącego katalogu do `/tmp/test`.  

**14.** Wyświetl zawartość katalogu `/tmp/test`.  

**15.** Przejdź jeden katalog wyżej.  

**16.** Wyświetl zawartość `/tmp`, pokazując tylko folder `test`.  

**17.** Przejdź do katalogu `/tmp/test` i usuń wszystkie znajdujące się w nim pliki.  

**18.** Wróć katalog wyżej.  

**19.** Usuń pusty katalog `test`.  

**20.** Przejdź do katalogu domowego użytkownika.  

**21.** Wyświetl historię ostatnio używanych poleceń.  

**22.** Zapisz historię poleceń do pliku `historia.txt`.

## Prompt

**1.** Korzystając z pomocy jednek z poniższych stron, wygeneruj swój własny styl wiersza poleceń dla powłoki bash. 
- https://scriptim.github.io/bash-prompt-generator/
- https://bashrcgenerator.com/
- https://ezprompt.net/

**2.** Wygenerowany bash zapisz w pliku konfiguracyjnym .bashrc znajdującym się w twoim katalogu domowym użytkownika.
```
cd ~/.
nano .bashrc
```

**3.** Załaduj pownonie powłowkę. 
```
bash
```

## Aliasy

**1.** **Utwórz tymczasowy alias `czas` do wyświetlenia aktualnej daty i godziny.**

**2.** **Utwórz tymczasowy alias `etc` do szybkiego wyświetlenia zawartości katalogu `/etc`.**

**3.** **Utwórz tymczasowy alias `pakiety` do wyświetlenia listy wszystkich zainstalowanych pakietów.**

**4.** **Utwórz tymczasowy alias `dom` do szybkiego przejścia do katalogu domowego.**

**5.** **Utwórz tymczasowy alias `dysk` do wyświetlenia zajętości dysku w formie czytelnej dla użytkownika.**

**6.** **Utwórz stały alias `aktualizuj` do wykonania aktualizacji systemu, wyczyszczenia cache oraz wyświetlenia komunikatu o powodzeniu.**

## Dowiązania – symlink i hardlink

**1.** W swoim katalogu domowym utwórz podkatalog „links”. Przejdź do tego katalogu. Utwórz plik „abc” z dowolną treścią.

**2.** Sprawdź informacje pliku abc. W szczególności zwróć uwagę na jego numer i-węzła, jego rozmiar i uprawnienia.

**3.** Utwórz dowiązanie stałe o nazwie „def” do pliku abc. Spójrz na cechy tego pliku.

**4.** Zmodyfikuj uprawnienia pliku def (np. 400). Następnie spójrz na uprawnienia abc.

**5.** Spójrz na charakterystykę systemu plików i zanotuj/zapamiętaj rozmiar cs-root

**6.** Usuń plik abc. Zobacz, co się stało z plikiem def.

**7.** Spójrz na charakterystykę systemu plików i sprawdź rozmiar cs-root

**8.** Skasuj plik def

**9.** Ponownie sprawdź rozmiar cs-root

## Edytory tekstu

**1.** **Utwórz nowy plik tekstowy o nazwie `temp.txt` za pomocą dowolnego edytora.**  

**2.** **Wpisz do pliku frazę:**  
   ```
   Szkolenie Linux
   ```

**3.** **Zapisz plik i wyjdź z edytora.**  

**4.** **Otwórz plik `temp.txt` w edytorze `vi`.**  

**5.** **Dopisz do istniejącej frazy słowa `jest proste` korzystając ze skrótu `A` (duże A).**  
- Skrót `A` przechodzi do końca linii i włącza tryb INSERT.

**6.** **Wyjdź z edytora `vi` bez zapisywania zmian.**  
- Użyj polecenia `:q!` w trybie COMMAND.

**7.** **Pobierz "Pana Tadeusza" w formacie `.txt` przy użyciu `wget`.**  
- Wskazówka: możesz użyć pliku z Wolnych Lektur, np.:
     ```
     wget https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt
     ```  

**8.** **Otwórz pobraną książkę (`pan-tadeusz.txt`) za pomocą edytora `vi`.**  

**9.** **Wyszukaj w tekście imię "Tadeusz" i przejdź przez kolejne wystąpienia.**  
- W trybie COMMAND: `/Tadeusz` + Enter, potem `n` (next).

**10.** **Uruchom plik `pan-tadeusz.txt` w edytorze `nano`.**  

**11.** **Wyszukaj frazę `Tadeusz` i przejdź przez kolejne wystąpienia.**  
- Użyj skrótu: `Ctrl+W`, wpisz `Tadeusz`, zatwierdź Enter. Następne wystąpienia: `Ctrl+W`, Enter.

**12.** **Wyjdź z edytora `nano` bez zapisywania zmian.**  
- Skrót: `Ctrl+X`, następnie `N`.

**13.** **Otwórz plik `temp.txt` za pomocą edytora `nano`.**  

**14.** **Usuń cały wiersz za pomocą odpowiedniego skrótu.**  
- Skrót: `Ctrl+K`.

**15.** **Wpisz nową frazę:**  
   ```
   Używam edytora nano
   ```

**16.** **Zapisz zmiany i wyjdź z edytora.**  
- Skróty: `Ctrl+O` (zapisz), Enter (potwierdź), `Ctrl+X` (wyjdź).

  Wiecej zadań praktycznych możesz znaleźć online, na przykład na stronie [https://vim.is/#exercise](https://vim.is/#exercise)
