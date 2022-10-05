import random
from random import randint


def tornarahorcado(fichero):
    with open(fichero, "r") as filestream:
        for line in filestream:
            currentline = line.split(";")
    paraula = currentline[randint(0, 29)]
    llistaparaula = list(paraula)
    numlletres = len(paraula)
    llistadivinar = list("_"*numlletres)
    return llistaparaula, llistadivinar, numlletres, paraula


def resultatpedrapap(opciomeva, rival):
    if opciomeva == rival:
        return 0
    elif opciomeva == "Pedra":
        if rival == "Paper":
            return 2
        else:
            return 1
    elif opciomeva == "Paper":
        if rival == "Tissores":
            return 2
        else:
            return 1
    elif opciomeva == "Tissores":
        if rival == "Pedra":
            return 2
        else:
            return 1


def adivinar():
    numuser = -1
    intents = 3
    adivinat = False
    a = random.randint(1, 10)

    while numuser != a and intents > 0:
        numuser = input("Adivina un número del 1 al 10 \n")
        while (not numuser.isdigit()):
            numuser = input("El numero ha de ser entre el 1 i el 10 \n")
        numuser = int(numuser)
        if numuser >= 0 and numuser <= 10:
            if numuser < a:
                print("El numero es mes gran")
            elif numuser > a:
                print("El numero es mes petit")
            else:
                print("Has adivinat el numero!!")
                adivinat = True
            intents -= 1
        else:
            print("Escull una opcio valida!!")
    if not adivinat:
        print("Has perdut, el numero era: ", a)


def pedrapap():
    puntsjo = 0
    puntsrival = 0
    opcionsR = ["Pedra", "Paper", "Tissores"]
    while puntsjo < 3 and puntsrival < 3:
        rival = opcionsR[randint(0, 2)]
        inputjo = input(
            "Escull opcio: \n 0. Pedra \n 1.Paper \n 2.Tissores \n")
        while (not inputjo.isdigit()):
            inputjo = input(
                "Ha de ser un numero!!! \nEscull opcio: \n 0. Pedra \n 1.Paper \n 2.Tissores \n")
        inputjo = int(inputjo)
        if (inputjo <= 2 and inputjo >= 0):
            opciomeva = opcionsR[inputjo]
            resultat = resultatpedrapap(opciomeva, rival)
            if (resultat == 0):
                print("Empat!")
            elif (resultat == 1):
                print("Has guanyat la ronda!", opciomeva,
                      " guanya contra ", rival)
                puntsjo += 1
            else:
                print("Has perdut la ronda!", opciomeva, " perd contra ", rival)
                puntsrival += 1

            print("Final de ronada. Punts teus: ", puntsjo,
                  " Punts del rival: ", puntsrival)
        else:
            print("Escull una opcio valida!")
    if puntsrival == 3:
        print("Has Perdut! El rival ha arribat a 3 punts")
    else:
        print("Has guanyat! Has arribat a 3 punts")


def ahorcado():

    tornar = tornarahorcado("palabras.csv")
    llistaparaula = tornar[0]
    llistadivinar = tornar[1]
    numlletres = tornar[2]
    paraula = tornar[3]
    intents = numlletres*2
    intentsmeus = 0
    lletresdites = []
    totaladivinades = 0
    lletraI = ""
    print("La paraula a adivinar es: ", "_"*numlletres)
    while intentsmeus < intents and totaladivinades < numlletres:
        lletradivinada = False
        lletraI = input("Digues una lletra \n")
        while (len(lletraI) > 1 or lletraI in lletresdites or lletraI.isdigit()):
            if (lletraI in lletresdites):
                lletraI = input("Error, Ja has dit la lletra! \n")
            else:
                lletraI = input("Error, Digues una lletra \n")

        lletraI = lletraI.lower()
        lletresdites.append(lletraI)
        counter = 0
        while counter < numlletres:
            if lletraI == llistaparaula[counter]:
                llistadivinar[counter] = lletraI
                lletradivinada = True
                totaladivinades += 1
            counter += 1
        if (lletradivinada):
            print("Has adivinat la lletra! La paraula esta així:")
            print(''.join(llistadivinar))
            intentsmeus += 1

        else:
            print("No has adivinat la lletra ;(")
            print(''.join(llistadivinar))
            intentsmeus += 1
        print("Portes ", intentsmeus, " de ", intents, " intents.")

    if (totaladivinades == numlletres):
        print("Has Guanyat!")
    else:
        print("Has perdut! T'has quedat sense intents La paraula era: ", paraula)


def joc():
    exit = False
    while not exit:
        print("<---------------------------------->")
        print("Escull una Opcio:")
        print("1. Adivinar el número:")
        print("2. Pedra Paper Tisora:")
        print("3. El Penjat:")
        print("4. Sortir:")
        print("<---------------------------------->")

        opcion = int(input("Escriu un numero \n"))
        if opcion == 1:
            adivinar()
        elif opcion == 2:
            pedrapap()
        elif opcion == 3:
            ahorcado()
        elif opcion == 4:
            exit = True
        else:
            exit = True

    print("Adeu!")


joc()
