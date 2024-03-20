
livre_disponible=["harry potter", "le seigneur des anneaux", "triple X", "le petit-prince", "colonies des vacances", "Murders"]

def afficher_livre(liste) : 
    print("*****Liste des livres Disponible*****\n")
    for i in range(len(liste)) : 
        print(f"{i+1} --- {liste[i]}.\n")


afficher_livre(livre_disponible)
num=int(input("entre le numéro d'un livre que tu veux louer.\n"))
if (livre_disponible.count(livre_disponible[num-1])>0) : 
    print(f"vous avez louez le livre  {livre_disponible[num-1]}. Merci de votre emprunt.\n")
    livre_disponible.remove(livre_disponible[num-1])
   
else : 
    print("désolé, le livre n'est pas disponible.\n")
afficher_livre(livre_disponible)