#!/usr/bin/env python
"""""""""""""""""""""
Random wachtwoord generator
"""""""""""""""""""""
# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

# IMPORTS
import random
import string

def random_wachtwoord(letters, cijfers): #Hier maak ik een functie aan die een random wachtwoord genereerd,
                                         # met als parameters het aantal letters en het aantal cijfers
    string_1 = ''.join((random.choice(string.ascii_letters) for i in range(letters))) #Hier geef ik de eerste parameter in 'letters'
                        # en zeg ik dat het eerste cijfer aangeeft hoeveel letters er in het random wachtwoord gaan zitten
    string_1 += ''.join((random.choice(string.digits) for i in range(cijfers))) #Hier herzelfde maar dan cijfers
    lijst = list(string_1) #Hier maak ik het wachtwoord aan
    random.shuffle(lijst) #Hier shuffle ik de letters en cijfers door elkaar
    string_2 = ''.join(lijst)
    return string_2 #Hier geef ik het mee aan de gebruiker

def main():
    try: #Hier gebruik ik een 'try en except'
        print("Typ '1' of '2'") #Hier geef ik gewoon info weer aan de gebruiker
        print("1 = Zwak wachtwoord")
        keuze = int(input("2 = Sterk wachtwoord: ")) #Hier vraag ik de gebruiker een input te geven genaamd keuze

        if keuze == 1: #Dit gebeurd er als de gebruiker de keuze heeft gemaakt een zwak wachtwoord aan te maken
            print("Zwak wachtwoord:", random_wachtwoord(6, 2)) #Hier word het zwakke wachtwoord aangemaakt met 6 letters en 2 cijfers

        if keuze == 2: #Dit gebeurd er als de gebruiker de keuze heeft gemaakt een sterk wachtwoord aan te maken
            print("Sterk wachtwoord:", random_wachtwoord(7, 4)) #Hier word het sterke wachtwoord aangemaakt met 7 letters en 4 cijfers

        elif keuze != '1' or '2': #Moest de keuze een ander cijfer zijn, komt er deze foutmelding en word het programma opnieuw gestard
            print("Kies cijfer '1' of '2'")
            main()

    except ValueError: #Moest de keuze geen cijfer zijn komt er te staan 'typ een cijfer' en start het programma ook opnieuw op
        print("Typ een cijfer")
        main()


if __name__ == '__main__':
    main()