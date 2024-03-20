import math
import random

def factorielle(nombre) : 
    fact=1
    while int(nombre) > 0 : 
        fact=fact*int(nombre)
        nombre = int(nombre)-1
    return fact

def perimetre (rayon):
    longeur=2*math.pi*int(rayon)
    return longeur

def random_custom(nombre) : 
    nb=random.randint(0,int(nombre))
    return nb


nb1=int(input("entre un nombre et ensuite un entre ton choix.\n"))
choix=int(input(f"""Veuillez entrer votre choix :\n    
                1- Calcul factorielle.\n    
                2- Calcul perimetre.\n
                3- renvoie un nombre aléatoire entre 0 et {nb1}.\n  """))
if choix==1 :
    print(f"la factorielle de {nb1} est : {factorielle(nb1)}")
elif choix==2 :
    print(f"le perimètre du cercle de rayon {nb1} est : {perimetre(nb1)}")
elif choix==3 :
    print(f"le système à généré ce nombre aléatoire : {random_custom(nb1)}")