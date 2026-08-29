# Słowniki
W tym katalogu są zgromadzone słowniki dla PSS. Słowniki są zgrupowane w różne poziomy. 

## Jak korzystać
Aby korzystać ze słowników z wykorzystaniem programu Plover, należy:
1. Pobrać wybrany słownik
2. Przenieść go do wybranego katalogu, gdzie przechowuje się słowniki
3. Z programu Plover wybrać opcję "Dodaj słownik" ("Add dictionary"), a następnie "Załaduj słownik" ("Load dictionary")
4. Wskazać pobrany słownik w oknie wyboru.

Zaleca się utrzymywać hierarchię słowników zgodną z zamieszczoną poniżej.

## Hierarchia słowników
Przy tworzeniu nowych słowników zaleca się unikanie konfliktów ze słownikami na poziomach równym lub niższym.
W razie potrzeby zawsze zaleca się pierwszeństwo słowników niższego poziomu (bliższych podstawie).
Wszystkie materiały dotyczące PSS zakładają używanie słowników poziomu 0, a materiały zaawansowane również poziomu 1.

### Poziom 0
Na poziom 0 składają się słowniki, które są uważane za niezbędne do korzystania z PSS w najbardziej podstawowym zakresie.
Poziom 0 zawiera następujące słowniki:
* rdzenie_bazowe.json - rdzenie słów uzyskane na podstawie listy 10000 najczęściej używanych słów Jerzego Kazojcia
(https://pl.wiktionary.org/wiki/Indeks:Polski_-_Najpopularniejsze_s%C5%82owa_1-10000_wersja_Jerzego_Kazojcia), jak również niektóre inne rdzenie
występujace w pospolitych, często występujących słowach
* przyrostki_bazowe.json - proste przyrostki fleksyjne i przyrostki morfologiczne na podstawie listy Jerzego Kazojcia
* przedrostki_bazowe.json - proste przedrostki na podstawie listy Jerzego Kazojcia
* skroty_gramatyczne.json - zaimki (w tym wersje skrócone dla złożonych zaimków), spójniki, przyimki, partykuły
* interpunkcja.json - znaki iterpunkcyjne i formatujące tekst

### Poziom 1
Na poziom 1 składają się słowniki, które są uważane za niezbędne do korzystania z PSS w sposób wydajny, jednakże nie wychodzą one poza słownictwo
zawarte w słownikach na poziomie 0.
Poziom 1 zawiera następujące słowniki:
* przedrostki_zlozone.json - praktyczne złożenia kilku prostych przedrostków w jeden
* przyrostki_zlozone.json - złożone przyrostki fleksyjne, nie łączone z przyrostkami morfologicznymi
* przyrostki_rozszerzone.json - najczęściej występujące przyrostki łączące przyrostki morfologiczne z przyrostkami złożonymi
* skrocenia.json - jednoakordowe skróty dla najczęstszych grup oraz słów

### Poziom 2
Na poziom 2 składają się słowniki, które wykraczają poza podstawowe słownictwo, pozostając nadal w standardowej odmianie języka polskiego.
Na poziom 2 składać się będą następujące kategorie:
* powszechne nazwy własne - polskie imiona, państwa świata, ich stolice, województwa i ich stolice, organizacje międzynarodowe
* słowniki tematyczne - prawniczy, sądowy, informatyczny, lekarski etc.

### Poziom 3
Na poziomie 3 znajdują się słowniki, które mogą zawierać słownictwo wykraczające poza standardową odmianę języka polskiego.
Na poziom 3 składać się będą przykładowo takie kategorie:
* niespolszczone zapożyczenia z języków obcych
* wyrazy gwarowe
* wyrazy slangowe
* nazwy poszczególnych miejscowości - ze względu na złożoność

## Stan prac
Na ten moment kształt prac nad słownikami wygląda następująco:
* poziom 0 - trwają prace nad listą 10000 słów, celem wyekstrahowania rdzeni, przedrostków i przyrostków
* poziom 1 - trwają prace nad listą 10000 słów, celem wyekstrahowania przyrostków i przedrostków, oraz wyznaczenia skróceń
* poziom 2 - nierozpoczęte
* poziom 3 - nierozpoczęte
