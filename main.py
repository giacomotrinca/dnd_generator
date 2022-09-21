import library as lib
import os
import tkinter
import tkinter.messagebox
from tkinter import Button, Label
lib.WelcomeScreen()
car = []
for i in range(0, 6):
    car.append(lib.statsheet())
    #print(car[i])
car = sorted(car)

print(f'Scegli la Modalità:')
print(f'Razza, Classe e Sottoclasse Causale -> [random]')
print(f'Scelgo Razza, Classe e Sottoclasse -> [choose]')

dec = []
while dec != "random" and dec != "choose":
    dec = input()
    if dec != "random" and dec != "choose":
        print(f'Scelta non valida!')


r = lib.chooserace(dec)
s = lib.choosesubrace(dec, r)
race = r + " " + s
print(race)
c = lib.chooseclass(dec)
print(c)
b = lib.choosebackground(dec)
print(b)
ab = lib.Abilities()
car = lib.assignstat(c, car)
name = lib.choosname()

lib.writetexfile(name, car, ab)

lib.removetexfiles()


