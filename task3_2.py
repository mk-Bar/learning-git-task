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


# Zadanie 2
# Napisz program, który:

# Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
# W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
# Przesyłanie zadań
# Zrób zrzuty ekranu z uruchomienia Twoich programów przez VSCode wraz z ich kodem źródłowym i wyślij je swojemu Mentorowi.

# Wskazówka: Staraj się trzymać porządek w strukturze projektu i plików. Dobrym pomysłem będzie utrzymywanie każdego zadania jako osobnego pliku.

# Zestaw zrzutów ekranu przekaż Mentorowi w jeden z poniższych sposobów:

# umieść je w nowym katalogu na swoim dysku sieciowym (np. Dropbox, Google Drive, etc.), wklej poniżej link do katalogu (uzyskany za pomocą guzika "Udostępnij"),
# otwórz nowy dokument na Google Docs i przeciągnij do niego zrzuty ekranu, wklej poniżej link do tego dokumentu (uzyskany za pomocą guzika "Udostępnij"),
# zrób zdjęcie ekranu aparatem typu Polaroid i wyślij je gołębiem pocztowym.
num=0
liczby=[]
while num<101:
    liczby=liczby+[num]
    num=num+1

liczbyPodzielnePrzez5=[liczba for liczba in liczby if liczba%5==0]
liczbyPodzielnePrzez5DoPotegi3=[liczba**3 for liczba in liczbyPodzielnePrzez5]
print(liczby)
print(liczbyPodzielnePrzez5)
print(liczbyPodzielnePrzez5DoPotegi3)