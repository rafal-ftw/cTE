# cTE
Car tool engine


# prequirements:
- pip install webdriver-manager



# notes
. odpalamy backend w Javie
. Backend dziala z baza za pomocą hibernate/jdbc - jest encja artykułu (marka, model, rok, cena, data dodania artykułu)
. Baza jest skonstruowana w nastepujacy sposob - tabele nazywane PRODUCENT
. schemat - ID(sekwencja dodania do bazy) - MODEL - PRICE - YEAR - ADDITIONDATE (todo: wyszczególnienie artykułów (link?) 


[mamy na bazie kilka producentów, np bmw oraz audi - chcemy informacje nt. serii 3 g30, serii 5 f10, a4 b8]
. skrypt w pythone zbierający dane z otomoto dla danego modelu (funkcja scrapAllModelData(manufacturer, model, generation))
. skrypt POBIERA z pliku models.json parametry do wykonywania funkcji scrapAllModelData
. skrypt wykonuje i zapisuje
. skrypt wysyla za pomoca biblioteki requests request POST z wynikami do STOJĄCEGO BACKENDU
. backend sprawdza rekordy (w servisie dla aktualizacji aut)
. sprawdza unikalne wartosci, jesli istnieje rekord z dana unikalna wartoscia ale cena sie zmienia to robimy update na rekordzie
. baza to mysql? ? ? z jakis liquibasem  ? ?


. mamy rekordy - kurwa louda - react wyswietla nam srednia cene dla danych aut z przedzialu x do przedzialu y : ) 
