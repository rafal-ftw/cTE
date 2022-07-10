# cTE
Car tool engine


# prequirements:
- pip install webdriver-manager



# notes
1. odpalamy backend w Javie
2. Backend dziala z baza za pomocą hibernate/jdbc - jest encja artykułu (marka, model, rok, cena, data dodania artykułu)
3. Baza jest skonstruowana w nastepujacy sposob - tabele nazywane PRODUCENT
4. schemat - ID(sekwencja dodania do bazy) - MODEL - PRICE - YEAR - ADDITIONDATE (todo: wyszczególnienie artykułów (link?) 


[mamy na bazie kilka producentów, np bmw oraz audi - chcemy informacje nt. serii 3 g30, serii 5 f10, a4 b8]
5. skrypt w pythone zbierający dane z otomoto dla danego modelu (funkcja scrapAllModelData(manufacturer, model, generation))
6. skrypt POBIERA z pliku models.json parametry do wykonywania funkcji scrapAllModelData
7. skrypt wykonuje i zapisuje
8. skrypt wysyla za pomoca biblioteki requests request POST z wynikami do STOJĄCEGO BACKENDU
9. backend sprawdza rekordy (w servisie dla aktualizacji aut)
10. sprawdza unikalne wartosci, jesli istnieje rekord z dana unikalna wartoscia ale cena sie zmienia to robimy update na rekordzie
11. baza to mysql? ? ? z jakis liquibasem  ? ?


12. mamy rekordy - kurwa louda - react wyswietla nam srednia cene dla danych aut z przedzialu x do przedzialu y : ) 
