##################### SIMPLE LISTS
bodovi = [83, 73, 61, 95,41, 31]

# add two new elements to the list 100 and 50
bodovi.append(100)
bodovi.append(50)
print(bodovi)

#####################

# print all even numbers from the list and save them in  a new list
even = []
for i in bodovi:
    if i % 2 == 0:
        even.append(i)
print(f'Parni preko for petlje: {even}')

# print all odd numbers from the list and save them in  a new list using comprehension
odd = [i for i in bodovi if i % 2 != 0]
print(f'Neparni comprehension: {odd}')

#####################
less_40 = []
for i in bodovi:
    if i < 40:
        less_40.append(i)
print(f'Manji od 40 preko for petlje: {less_40}')

less_40 = [i for i in bodovi if i < 40]
print(f'Manji od 40 comprehension: {less_40}')

#####################

# iterate the list and using a for loop assing a value to an elelment of the list
for i in bodovi:
    if 90 > i < 100:
        print ("Odlican")
    if 80 > i < 90:
        print ("Vrlo dobar")
    if 70 > i < 80:
        print ("Dobar")
    if 60 > i < 70:
        print ("Dovoljan")
    if 50 > i:
        print ("Nedovoljan")


#####################

# write a program that demostrates information maninpulation about books in a dictionary
# every book has a title, author, year and availability
# starting point
knjiznica = {
    'Harry Potter': {'autor': 'J.K. Rowling', 'godina': 2001, 'dostupno': 5},
    'Lord of the Rings': {'autor': 'J.R.R. Tolkien', 'godina': 1954, 'dostupno': 3}
}

# add a new book to the library
knjiznica['Witcher'] = {'autor': 'Andrzej Sapkowski', 'godina': 1994, 'dostupno': 0}

# print all books in the library
for i in knjiznica:
    print(i)
print([i for i in knjiznica])

##################### LIST COMPREHENSION

# create a list from 1 to 100 using comprehension
lista = [i for i in range(1,100)]
print(lista)

# from this list create a list "filtrirani_brojevi" that will contain numbers => 49 and <=80 using comprehension
filtrirani_brojevi = [i for i in lista if 49 < i < 80]
print(filtrirani_brojevi)

##################### DICTIONARY COMPREHENSION
studenti = {
    "Ana": 100,
    "Marko": 25,
    "Petra": 49,
    "Ivan": 56,
    "Mia": 89,
    "Lovro": 80,
    "Stipe":73,
    "Lea":60,
    "Tomislav":51,
    "Leo":99
}

# Create a dictionary "filtrirani_studenti" that will contain only students that have names witih 3 letters or more and a minimum of 50 points
filtrirani_studenti = {k: v for k, v in studenti.items() if len(k) >= 3 and v >= 50}
print(filtrirani_studenti)


