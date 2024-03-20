import random
liste=["pierre","papier","ciseaux"]
nom=input("entre ton nom, tu vas jouer contre l'ordinateur.\n")
choix=int(input("""entre ton choix :\n
              1- pierre.\n
              2- Papier.\n
              3- Ciseaux.\n"""))
nbre_ordi=random.randint(1,3)
pointjoueur=0
pointordi=0

if (choix==1 and nbre_ordi==3) or (choix==2 and nbre_ordi==1) or (choix==3 and nbre_ordi==2): 
     print (f"""{nom} remporte la manche et marque 1 point.\n
            {nom} à jouer {liste[(choix-1)]}.\n
             L'ordinateur à jouer {liste[nbre_ordi]} """)
     pointjoueur+=1
else : 
     print (f"""L'ordinateur remporte la manche et marque 1 point.\n
             L'ordinateur à jouer {liste[nbre_ordi]}.\n
             {nom} à jouer {liste[(choix-1)]}.\n""")
     pointordi+=1
     
