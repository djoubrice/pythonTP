import random

joueur1 = input("Quel est votre nom ?\n")
joueur2 = input("Quel est le nom du joueur 2 ?\n")

pierre = "pierre"
papier = "papier"
ciseaux = "ciseaux"

point1 = 0
point2 = 0


while point1 < 2 or point2 < 2:
    choix1 = input("Quel est le choix du premier joueur ?\n")
    
    choix2 = random (pierre,papier,ciseaux)
    if (choix1 == pierre and choix2 == ciseaux) or (choix1 == papier and choix2 == pierre) or (choix1 == ciseaux and choix2 == papier) :
        print (joueur1+(" est gagnant"))
        point1 = point1 + 1
        
    else :
        print (joueur2+(" est gagnant"))
        point2 = point2 +1

    if point1==2 or point2 == 2 :
            break        

