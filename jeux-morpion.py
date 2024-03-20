import random

niveau_jeux=1; point_vie=5

def niveau_ennemi(i) :
   n= random.randint((int(i)-1),(int(i)+1))
   return n

nom=input("entre ton nom tu vas jouer contre l'ordinateur !\n")
print(f"{nom} , tu es au niveau {niveau_jeux}, et tu as {point_vie} Point de vie\n")

while point_vie >1 :
    niveau_ordi=niveau_ennemi(niveau_jeux)
    if niveau_ordi <= niveau_jeux : 
        niveau_jeux +=1
        print(f"{nom} tu as gangé la partie - tu passes au niveau {niveau_jeux}, et tu as maintenant {point_vie} points de vie\n")
        
    else :
        point_vie =point_vie-1
        print(f"{nom} tu as perdu la partie.  -  tu restes au niveau {niveau_jeux}, et tu as maintenant {point_vie} points de vie\n")
        