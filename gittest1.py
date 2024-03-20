import time
print("Les jeux disponibles sont: \n" 
      "1 : morpion\n"
      "2 : pierre-feuille-ciseau\n"
      "3 : jeu aléatoire du dé\n"
      "4 : jeu des stylos\n"
      "5 : pendu\n")

Start = input("Entrez le numéro du jeu auquel vous voulez jouer : ")
if Start == "1":

    print("Vous avez choisi le jeu du morpion ! ")
    print("Commençons...")
    time.sleep(1)



    plateau = [" " for i in range(9)]


    def afficherPlateau(p, gagnant=None):
        print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
        print("---+---+---")
        print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
        print("---+---+---")
        print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
        if gagnant:
            print(" Partie terminée : le joueur " + gagnant + " a gagné !!!")


    def morpion():
        joueur = "X"
        tour = 0

        while True:
            afficherPlateau(plateau)
            print(" Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")

            move = int(input()) - 1

            if plateau[move] == " ":
                plateau[move] = joueur
                tour += 1
            else:
                print("! Case déjà occupée, choisissez-en une autre.")
                continue

            if plateau[0] == plateau[1] == plateau[2] != " " \
            or plateau[3] == plateau[4] == plateau[5] != " " \
            or plateau[6] == plateau[7] == plateau[8] != " " \
            or plateau[0] == plateau[3] == plateau[6] != " " \
            or plateau[1] == plateau[4] == plateau[7] != " " \
            or plateau[2] == plateau[5] == plateau[8] != " " \
            or plateau[0] == plateau[4] == plateau[8] != " " \
            or plateau[2] == plateau[4] == plateau[6] != " ":
                afficherPlateau(plateau, joueur)
                break

            if tour == 9:
                print("Égalité")
                break

            if joueur == "X":
                joueur = "0"
            else:
                joueur = "X"


    morpion()

if Start == "2":
    print("Vous avez choisi le jeu du pierre feuille ciseau ! ")
    print("Commençons...")
    time.sleep(1)

    joueur1 = input("Entrez le nom du joueur 1:").capitalize()
    joueur2 = input("Entrez le nom du joueur 2:").capitalize()


    def jeu():
        while True:

            jr1 = input(joueur1 + ": pierre, feuille ou ciseau? " + " \U0001F600")
            saut_de_ligne="\n"
            print(saut_de_ligne*50)
            jr2 = input(joueur2 + ": pierre, feuille ou ciseau? " + " \U0001F607")

            if jr1 == "pierre" and jr2 == "feuille":
                print(jr1 + " VS " + jr2)
                print(joueur2 + " a battu " + joueur1 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == "pierre" and jr2 == "ciseau":
                print(jr1 + " VS " + jr2)
                print(joueur1 + " a battu " + joueur2 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == "feuille" and jr2 == "pierre":
                print(jr1 + " VS " + jr2)
                print(joueur1 + " a battu " + joueur2 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == "feuille" and jr2 == "ciseau":
                print(jr1 + " VS " + jr2)
                print(joueur2 + " a battu " + joueur1 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == "ciseau" and jr2 == "pierre":
                print(jr1 + " VS " + jr2)
                print(joueur2 + " a battu " + joueur1 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == "ciseau" and jr2 == "feuille":
                print(jr1 + " VS " + jr2)
                print(joueur2 + " a battu " + joueur1 + " \U0001F605")
                print("--------Nouvelle partie---------")
                print("\n")
            elif jr1 == jr2:
                print(jr1 + " VS " + jr2)
                print("Egalité")
                print("--------Nouvelle partie---------")
                print("\n")


    jeu()

if Start == "3":
    print("Vous avez choisi le jeu du dé aléatoire ! ")
    print("Commençons...")
    time.sleep(1)

    from random import *




    while True:
        print("Le dé est en train d'être lancé...")
        time.sleep(2)
        print("C'est bon ! ")
        print("\n")
        res = randint(1, 6)
        guess = input("Entrez le numéro du dé lancé \U0001F910 :")
        if int(guess) == res:
            print("Bravoo, vous avez de la chance aujourd'hui. Allez jouer au loto  \U0001F601")

            print("Encore:")
        else:
            print("C'est raté, le chiffre était " , res , " \U0001F612")
            print("Encore:")

if Start == "4":
    print("Vous avez choisi le jeu des stylos ! ")
    print("Commençons...")
    time.sleep(1)
    j1 = input("Joueur 1, entrez votre nom: ").capitalize()
    j2 = input("Joueur 2, entrez votre nom: ").capitalize()
    a = "|"
    k = int(input("Entrez le nombre de stylo de départ:"))
    b = a * k
    print("Vous jouez avec " + str(k) + " stylos")
    print(b)

    while True:
        p1 = int(input(str(j1) + ", entrez le nombre de stylos à enlever:"))
        print("\n")
        k = k - int(p1)
        print("Il reste " + str(k) + " stylos.")
        b = a * k
        print(b)
        if len(b) == 1:
            print("Fin, " + str(j1) + " a gagné!")
            break
        p2 = int(input(str(j2) + ", entrez le nombre de stylos à enlever:"))
        print("\n")
        k = k - int(p2)
        print("Il reste " + str(k) + " stylos.")
        b = a * k
        print(b)
        if len(b) == 1:
            print("Fin, " + str(j2) + " a gagné!")
            break

if Start == "5":
    print("Vous avez choisi le jeu du pendu ! ")
    print("Commençons...")
    time.sleep(1)

    mot = str(input("Entrez le mot: "))
    for m in range(30):
        print("|")
    word = list(mot)
    essai = 10
    print("Vous avez 10 essais")
    cache = ["_" for i in mot]
    print(" ".join(cache))
    while True:
        letter = str(input("Entrez une lettre: "))


        if letter in mot:
            for k in range(len(word)):
                if letter == word[k]:
                    cache[k] = word[k]


                else:
                    cache[k] = cache[k]
            print(" ".join(cache))
        else:
            essai -= 1
            print("Raté... il vous reste plus que " + str(essai) + " essais .")
            print(" ".join(cache))
            if essai == 9:
                print(" _")
            if essai == 8:
                print("/_\ ")
            if essai == 7:
                print(" |")
                print(" |")
                print(" |")
                print("/_\ ")
            if essai == 6:
                print(" |―")
                print(" |")
                print(" |")
                print("/_\ ")
            if essai == 5:
                print(" |――")
                print(" |")
                print(" |")
                print("/_\ ")
            if essai == 4:
                print(" |――!")
                print(" |")
                print(" |")
                print("/_\ ")
            if essai == 3:
                print(" |---┬")
                print(" |   O")
                print(" |")
                print("/_\ ")
            if essai == 2:
                print(" |---┬")
                print(" |   O")
                print(" |   |")
                print("/_\  ")
            if essai == 1:
                print(" |---┬")
                print(" |   0")
                print(" |   ┼")
                print("/_\  ")
            if essai == 0:
                print(" |---┬")
                print(" |   0")
                print(" |   ┼")
                print("/_\  ^")

        if cache == word:
            print("Bravo !! Vous avez gagné. Vous avez trouvé le mot: " + mot + "!")
            break
        elif essai == 0:
            print("Dommage, vous avez perdu... le mot était: " + mot)
            break