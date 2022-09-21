import numpy as num
import random
import os


def WelcomeScreen():
    print(f'###################################')
    print(f'## D&D CHARACTER SHEET GENERATOR ##')
    print(f'############# GTC #################')
    print(f'###################################')


def throwdie():
    dice = [1, 2, 3, 4, 5, 6]
    return random.choice(dice)


def statsheet():
    c = []
    for i in range(0, 4):
        c.append(throwdie())
    c = sorted(c)
    a = 0
    for i in range(1, 4):
        a += c[i]
    return a


def chooserace(dec):
    print(f'Scegli una razza:')
    race = ["Elfo", "Halfling", "Nano", "Umano", "Dragonide", "Gnomo", "Mezzelfo", "Mezzorco", "Tiefling"]
    if dec == "random":
        r = random.choice(race)
    else:
        for i in range(0, len(race)):
            print(race[i])

        count = 0
        while (count == 0):
            r = input()
            for i in range(0, len(race)):
                if race[i] == r:
                    count += 1

            if count == 0:
                print(f'Input Errato')
            #else:
                #print(f'OK')

    return r


def choosesubrace(dec, r):
    s = []
    if r == "Elfo":
        s = ["Dei Boschi", "Alto", "Oscuro"]
    elif r == "Halfling":
        s = ["Piedelesto", "Tozzo"]
    elif r == "Nano":
        s = ["Delle Montagne", "Delle Colline"]
    elif r == "Umano":
        s = ["Standard", "Variante"]
    elif r == "Dragonide":
        s = ["Argento", "Bianco", "Blu", "Bronzo", "Nero", "Oro", "Ottone", "Rame", "Rosso", "Verde"]
    elif r == "Gnomo":
        s = ["Delle Foreste", "Delle Rocce"]
    else:
        print(f'Non sono disponibili sottorazze')
        s = " "
    st = ""
    if s == " ":
        st = ""
    else:
        if dec == "random":
            st = random.choice(s)
        else:
            for i in range(0, len(s)):
                print(s[i])

            count = 0
            while (count == 0):
                st = input()
                for i in range(0, len(s)):
                    if s[i] == st:
                        count += 1

                if count == 0:
                    print(f'Input Errato')
                #else:
                    #print(f'OK')

    return st

def chooseclass(dec):
    print(f'Scegli una classe:')
    c = ["Barbaro", "Bardo", "Chierico", "Druido", "Guerriero", "Ladro", "Mago", "Monaco", "Paladino", "Ranger",
         "Stregone", "Warlock"]
    if dec == "random":
        cin = random.choice(c)
    else:
        for i in range(0, len(c)):
            print(c[i])

        count = 0
        while (count == 0):
            cin = input()
            for i in range(0, len(c)):
                if c[i] == cin:
                    count += 1

            if count == 0:
                print(f'Input Errato')
            #else:
                #print(f'OK')

    return cin

def choosebackground(dec):
    print(f'Scegli un Background:')
    b = ["Accolito", "Artigiano di Gilda", "Ciarlatano", "Criminale", "Eremita", "Eroe Popolare", "Forestiero", "Intrattenitore", "Marinaio", "Monello", "Nobile", "Sapiente", "Soldato", ]
    if dec == "random":
        cin = random.choice(b)
    else:
        for i in range(0, len(b)):
            print(b[i])

        count = 0
        while (count == 0):
            cin = input()
            for i in range(0, len(b)):
                if b[i] == cin:
                    count += 1

            if count == 0:
                print(f'Input Errato')
            #else:
                #print(f'OK')

    return cin


def assignstat(cl, car):
    stats=["Forza", "Destrezza", "Costituzione", "Intelligenza", "Saggezza", "Carisma"]
    cl2 = []
    if cl == "Barbaro":
        cl2.append(car[5])      #FORZA
        cl2.append(car[3])      #DESTREZZA
        cl2.append(car[4])      #COSTITUZIONE
        cl2.append(car[1])      #INTELLIGENZA
        cl2.append(car[2])      #SAGGEZZA
        cl2.append(car[0])      #CARISMA
    elif cl == "Bardo":
        cl2.append(car[0])  # FORZA
        cl2.append(car[4])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[2])  # INTELLIGENZA
        cl2.append(car[1])  # SAGGEZZA
        cl2.append(car[5])  # CARISMA
    elif cl == "Chierico":
        cl2.append(car[4])  # FORZA
        cl2.append(car[2])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[1])  # INTELLIGENZA
        cl2.append(car[5])  # SAGGEZZA
        cl2.append(car[0])  # CARISMA
    elif cl == "Druido":
        cl2.append(car[1])  # FORZA
        cl2.append(car[2])  # DESTREZZA
        cl2.append(car[4])  # COSTITUZIONE
        cl2.append(car[3])  # INTELLIGENZA
        cl2.append(car[5])  # SAGGEZZA
        cl2.append(car[0])  # CARISMA
    elif cl == "Guerriero":
        cl2.append(car[5])  # FORZA
        cl2.append(car[3])  # DESTREZZA
        cl2.append(car[4])  # COSTITUZIONE
        cl2.append(car[2])  # INTELLIGENZA
        cl2.append(car[1])  # SAGGEZZA
        cl2.append(car[0])  # CARISMA
    elif cl == "Ladro":
        cl2.append(car[2])  # FORZA
        cl2.append(car[5])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[0])  # INTELLIGENZA
        cl2.append(car[1])  # SAGGEZZA
        cl2.append(car[4])  # CARISMA
    elif cl == "Mago":
        cl2.append(car[0])  # FORZA
        cl2.append(car[3])  # DESTREZZA
        cl2.append(car[4])  # COSTITUZIONE
        cl2.append(car[5])  # INTELLIGENZA
        cl2.append(car[2])  # SAGGEZZA
        cl2.append(car[1])  # CARISMA
    elif cl == "Monaco":
        cl2.append(car[0])  # FORZA
        cl2.append(car[5])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[2])  # INTELLIGENZA
        cl2.append(car[4])  # SAGGEZZA
        cl2.append(car[1])  # CARISMA
    elif cl == "Paladino":
        cl2.append(car[5])  # FORZA
        cl2.append(car[2])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[0])  # INTELLIGENZA
        cl2.append(car[1])  # SAGGEZZA
        cl2.append(car[4])  # CARISMA
    elif cl == "Ranger":
        cl2.append(car[2])  # FORZA
        cl2.append(car[5])  # DESTREZZA
        cl2.append(car[3])  # COSTITUZIONE
        cl2.append(car[0])  # INTELLIGENZA
        cl2.append(car[4])  # SAGGEZZA
        cl2.append(car[1])  # CARISMA
    elif cl == "Guerriero":
        cl2.append(car[0])  # FORZA
        cl2.append(car[3])  # DESTREZZA
        cl2.append(car[4])  # COSTITUZIONE
        cl2.append(car[1])  # INTELLIGENZA
        cl2.append(car[2])  # SAGGEZZA
        cl2.append(car[5])  # CARISMA
    elif cl == "Warlock":
        cl2.append(car[0])  # FORZA
        cl2.append(car[3])  # DESTREZZA
        cl2.append(car[4])  # COSTITUZIONE
        cl2.append(car[1])  # INTELLIGENZA
        cl2.append(car[2])  # SAGGEZZA
        cl2.append(car[5])  # CARISMA
    else:
        print(f'Ci sonos tati errori')

    for i in range(0, len(cl2)):
        print(f'{stats[i]} {cl2[i]}')
    

    return cl2

def choosname():
    namefile = open("names.dat", "r")
    n=namefile.readlines()
    name = random.choice(n)
    #print(name)
    namefile.close()
    new_name = name[0]
    for i in range(1, len(name)-1):
        new_name = new_name + name[i]

    print(new_name)
    return new_name

class Abilities():
    names = ["Atletica", "Acrobazia", "Furtività", "Rapidità di Mano", "Arcano", "Indagare", "Natura", "Religione",
             "Storia", "Addestrare Animali", "Intuizione", "Medicina", "Percezione", "Sopravvivenza", "Intimidire",
             "Inganno", "Intrattenere", "Persuasione"]
    values = []
    ts_names = ["Forza", "Destrezza", "Costituzione", "Intelligenza", "Saggezza", "Carisma"]
    ts_values = []
    # questa è una flag per indicare se il personaggio abbia o meno competenza in una abilità o tiro salvezza
    proficiency = []

def writetexfile(name, car, ab):
    texfile = open(f'{name}.tex', "w")
    texfile.write(
            "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{graphicx}\n\\usepackage[margin=0.1in]{geometry}\n\\usepackage[dvipsnames]{xcolor}\n\\usepackage{yfonts}\n\\usepackage{comment}\n\\usepackage[italian]{babel}\n\\usepackage{aurical}\n\\usepackage[T1]{fontenc}\n\\usepackage{tabularx}\n\\usepackage{watermark}\n\\usepackage{tikz}\n\\newcommand*\\circled[1]{\\tikz[baseline=(char.base)]{\n\\node[shape=circle,draw,inner sep=2pt] (char) {#1};}}\n\\definecolor{OCRA}{RGB}{204,119,34}\n\n\\begin{document}\n\\thiswatermark{\\centering \\put(-50,-850){\\includegraphics[scale=1.5]{img/paper.jpg}} }\n")
    texfile.write("\\end{document}")
    texfile.close()
    #shfile = open(f'runlatex.sh', "w")
    #command ="pdflatex " + name + ".tex >> .log"
    #os.system(command)


def removetexfiles():
    dec = []
    while dec != 'y' and dec != 'n':
        dec = input(f'Cancellare i files TeX?[Y/N]')
        if dec != 'y' and dec != 'n':
            print(f'Scelta non valida!')
        elif dec == 'y':
            os.system("rm *.tex")
            os.system("rm *.aux")
            os.system("rm *.log")

