#!/usr/bin/env python
"""""""""""""""
Kies een liedje
"""""""""""""""
b = "Birds in the Trap Sing Mcknight" #Hier maak ik een string die het album defineerd
a = "ASTROWORLD"
t = "Travis Scott"
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory


# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

class liedjes: #Hier maak ik een class genaamd liedjes
    def __init__(self, artiest, titel, album): #hier geef ik de parameters mee die per nummer alles printen
        self.titel = titel
        self.artiest = artiest
        self.album = album
    def zingen(self): #Hier maak ik een functie aan binnen de class die het nummer gaat printen
        print("")
        print(self.artiest,"-", self.titel) #Hier word eerst de artiest dan een streepje en dan de titel gepriny
        print("(",self.album,")") #Hier word het album geprint tussen haakjes
        print("")

# FUNCTIONS
def main():
    sicko_mode = liedjes(t,"SICKO MODE", a) #Hier defineer ik het de liedjes
    goosebumps = liedjes(t, "goosebumps", b)
    butterfly = liedjes(t,"BUTTERFLY EFFECT", a)
    putf = liedjes(t, "pick up the phone", b)
    print("1 = SICKO MODE") #Dit geef ik mee voor de gebruiker, zodat hij weet welk getal hij in moet voeren
    print("2 = goosebumps")
    print("3 = BUTTERFLY EFFECT")
    print("4 = pick up the phone")
    try: #Hier gebruik ik een try en exceot
        keuze = int(input('Kies een nummer 1, 2, 3 of 4: ')) #Hier maakt de gebruiker een keuze
        if keuze == 1: #Dit gebeurd er als de ze de eerste keuze maken
            sicko_mode.zingen() #Hier word de functie zingen gebruikt
            f = open("liedjes/sickomode.txt", "r") #Hier open ik het tekstbestandje genaamd sickomode dat in de map 'liedjes' zit
            print(f.read()) #Hier lees ik het bestandje

        elif keuze == 2: #Hier gebeurd exact hetzelfde maar dan als de tweede keuze gemaakt word
            goosebumps.zingen()
            f = open("liedjes/goosebumps.txt", "r")
            print(f.read())

        elif keuze == 3:
            butterfly.zingen()
            f = open("liedjes/butterfly.txt", "r")
            print(f.read())

        elif keuze == 4:
            putf.zingen()
            f = open("liedjes/pick up the phone.txt", "r")
            print(f.read())

        elif keuze != '1' or '2' or '3' or '4': #Moest de keuze een ander cijfer zijn komt er deze foutmelding, en word het programma opnieuw gestard
            print("Gelieve een getal tussen 1 en 4 in te geven")
            main()

    except ValueError: #Moest de keuze geen cijfer zijn komt er deze error, en word het programma opnieuw gestart
        print("Ik vroeg om een cijfer!")
        main()



if __name__ == '__main__':
    main()
