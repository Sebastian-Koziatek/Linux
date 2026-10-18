# Zadania: Woluminy logiczne LVM

Zadania wykonuj na **dodatkowych dyskach** `/dev/sdb` i `/dev/sdc` maszyny szkoleniowej (powinny być czyste – bez partycji, macierzy i systemów plików; jeśli zostały na nich ślady po module 09, posprzątaj według tamtejszych rozwiązań). Dysku systemowego `/dev/sda` i grupy systemowej (`rl`/`cs`/`rhel`) nie zmieniamy – tylko odczytujemy.

> **Wskazówka:** po każdym kroku sprawdzaj efekt poleceniami `pvs`, `vgs`, `lvs` i `lsblk`.

1. Sprawdź, czy dyski `/dev/sdb` i `/dev/sdc` są widoczne w systemie i czyste (bez partycji oraz systemów plików).
2. Wyświetl istniejące w systemie grupy woluminów oraz woluminy logiczne. Jak nazywa się grupa utworzona przez instalator i jakie woluminy zawiera?
3. Utwórz na dysku `/dev/sdb` tablicę GPT i jedną partycję zajmującą cały dysk, o typie **Linux LVM**.
4. Utwórz wolumin fizyczny (PV) na partycji `/dev/sdb1`. Sprawdź listę PV w systemie.
5. Utwórz grupę woluminów o nazwie `vg_szkolenie` zawierającą `/dev/sdb1`. Sprawdź jej rozmiar i wolne miejsce.
6. Utwórz w grupie `vg_szkolenie` wolumin logiczny o nazwie `lv_szkolenie` i rozmiarze **5 GiB**.
7. Sprawdź, pod jakimi dwiema ścieżkami w `/dev` widoczny jest nowy wolumin.
8. Załóż na woluminie system plików XFS, utwórz katalog `/szkolenie` i zamontuj w nim wolumin. Utwórz w nim plik z dowolną treścią.
9. Sprawdź, czy wolumin jest zamontowany i ile ma wolnego miejsca.
10. Powiększ wolumin `lv_szkolenie` o **2 GiB** razem z systemem plików – bez odmontowywania. Udowodnij poleceniem `df -h`, że system plików urósł.
11. Dodaj cały dysk `/dev/sdc` (bez partycjonowania) jako drugi wolumin fizyczny do grupy `vg_szkolenie`. Sprawdź, o ile urosło wolne miejsce w grupie.
12. Powiększ wolumin `lv_szkolenie` o **całe pozostałe wolne miejsce** grupy.
13. Wyświetl szczegółowe informacje o grupie `vg_szkolenie` (m.in. rozmiar PE, liczbę PE wolnych i zajętych) oraz o woluminie `lv_szkolenie`.
14. Wyjaśnij: czym różni się `lvextend -r` od `lvextend` bez tej opcji? Co trzeba zrobić dodatkowo, gdy `-r` pominięto – i jakim poleceniem dla XFS, a jakim dla ext4?
15. Wyjaśnij: dlaczego woluminu z systemem plików XFS nie można zmniejszyć i jaki z tego praktyczny wniosek przy planowaniu rozmiarów woluminów?
16. Utwórz migawkę woluminu `lv_szkolenie` o nazwie `lv_szkolenie_przed` i rozmiarze 1 GiB. Zmień zawartość pliku na woluminie, a potem sprawdź listą `lvs`, że migawka istnieje i zaczęła zajmować miejsce. Usuń migawkę.
17. Wyjaśnij: co daje połączenie mdadm RAID 1 z LVM i w jakiej kolejności układa się warstwy takiego serwera?
18. Posprzątaj w poprawnej kolejności: odmontuj wolumin, usuń LV, grupę i woluminy fizyczne, tak by `lsblk` pokazywał czyste dyski. Dlaczego kolejność usuwania musi być odwrotna do kolejności tworzenia?
