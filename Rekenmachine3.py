#!/usr/bin/env python
##########################################
#          Rekenmachine Versie 3         #
##########################################
# IMPORTS

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

#De functies +, -, * en / worden hier aangemaakt
# Plus
def plus(x, y): #Eerst heb ik 4 functies aangemaakt voor alle soort bewerkingen
    return x + y

# Min
def min(x, y):
    return x - y

# Maal
def maal(x, y):
    return x * y

# Gedeeld door
def delen(x, y):
    return x / y


print("1.Plus") #Hier vraag ik de gebruiker of hij +, -, * of / wilt gebruiken
print("2.Min")
print("3.Maal")
print("4.Delen door")


def main():
    try: #Hier gebruik ik 'try en except'
        # Laat de gebruiker een bewerking kiezen
        keuze = int(input("Voer keuze in (1/2/3/4): ")) #Hier maakt de gebruiker de keuze tussen min/maal/...

        if keuze == 1 or keuze == 2 or keuze == 3 or keuze == 4:
            # Controlleert of de gebruiker een juiste keuze gemaakt heeft
            num1 = float(input("Voer eerste cijfer in: ")) #De gebruiker word gevraagd het eerste cijfer in te voeren
            num2 = float(input("Voer tweede cijfer in: ")) #De gebruiker word gevraagd het tweede cijfer in te voeren

            if keuze == 1:
                print(num1, "+", num2, "=", plus(num1, num2)) #Dit gebeurd er als de gebruiker 'plus' heeft gekozen

            elif keuze == 2:
                print(num1, "-", num2, "=", min(num1, num2)) #Dit gebeurd er als de gebruiker 'min' heeft gekozen

            elif keuze == 3:
                print(num1, "*", num2, "=", maal(num1, num2)) #Dit gebeurd er als de gebruiker 'maal' heeft gekozen

            elif keuze == 4:
                print(num1, "/", num2, "=", delen(num1, num2)) #Dit gebeurd er als de gebruiker 'gedeeld door' heeft gekozen


        elif keuze != 1 or keuze != 2 or keuze != 3 or keuze != 4: #Moest de gebruiker een ander getal ingevoerd hebben,
                                                                    # komt er deze foutmelding
            print("Voer aub een getal in van 1 tot 4!")
            main()

    except ValueError: #Deze except word alleen gebruikt als de gebruiker geen getal heeft ingevoerd
        print("Ik vroeg om een getal")
        main()


if __name__ == '__main__':
    main()
