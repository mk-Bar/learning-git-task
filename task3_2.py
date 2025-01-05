# Zadanie 1
# Pamiętasz zadanie z listą zakupów?

# Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka. 
# Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.

# W pliku, który właśnie utworzyliśmy:

# zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
# Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
# Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
# Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
# Twój program po uruchomieniu, powinien wyświetlić następujące informacje:

# Lista zakupów
# Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
# Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
# W sumie kupuję 6 produktów.

listaZakupow={"piekarnia":["chleb", "pączek", "bułki"], 
              "warzywniak": ["marchew", "seler", "rukola"]}


for sklep,rzeczy in listaZakupow.items():
    
    sklep=sklep.capitalize()
    rzeczy=[produkt.capitalize() for produkt in rzeczy]
    print(f"Idę do {sklep} i kupuję tam {rzeczy}")
    