#!/usr/bin/env python
"""""""""""""""""""""
Een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken, 
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import random

# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# FUNCTIONS

def main():
    f = open("getallen.txt", "a") #Eerst open ik het tekstbestandje
    print("Nieuwe getallen in de lijst: ")
    for x in range(20): #Hier maak ik een for loop aan die 20 keer opnieuw gebeurd
        n = str(random.randint(0, 50)) #Hier maak ik een string aan die random getallen weer gaat geven van 0 tot 50
        f.write(n) #Hier schrijf ik het random getal in het tekstbestand
        f.write("\n") #Hier geef ik een enter in zodat elk getal op een nieuwe lijn start
        print(n) #Hier geef ik de gebruiker alle nieuwe random getallen weer

    data = []
    with open(r'getallen.txt') as f: #Nog een loop waar ik het gemiddelde bereken
        for line in f: #Hier geef ik in dat de cijfers per line geprint staan
            fields = line.split() #De functie 'split' word hier gebruikt
            rowdata = map(float, fields)
            data.extend(rowdata)
    print("Het gemiddelde van de lijst is: ", sum(data) / len(data)) #Hier print ik het gemiddelde
    f.close() #Het bestandje word gesloten

if __name__ == '__main__':
    main()
