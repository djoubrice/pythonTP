liste_course1=[] ; liste_course2=[]
liste_menu=["Ajouter un article","supprimer un article","afficher la liste des courses","quittez"]

def afficher_menu(liste) : 
    print("*****Menu principale*****\n")
    for i in range(len(liste)) : 
        print(f"{i+1} --- {liste[i]}.\n")

def afficher_produit(liste) : 
    print("*****Liste des produits Dans le panier*****\n")
    for i in range(len(liste)) : 
        print(f"{i+1} --- {liste[i]}.\n")

def ajouter_article(liste,nom):
    liste.append(nom)
    
def retirer_article(liste, nom):
    if liste.count(nom)>0 :
        liste.remove(nom)
        print(f"{nom} a été retiré de la liste.\n")
    else :
        print(f" désolé {nom} n'est pas dans la liste des courses.\n")



while True : 
    choix_liste=int(input("""choisie la liste que tu veux utiliser.\n 1- liste 1  \n 2- liste 2"""))
    afficher_menu(liste_menu)
    choix=int(input("entrez votre choix :   "))
    if choix == 1 :
        nom=input("entre le nom du produit que tu veux ajouter.\n")
        if choix_liste == 1 :
            ajouter_article(liste_course1,nom)
            print(f"{nom} a été ajouter à la liste 1.\n")
        elif choix_liste ==2 :
            ajouter_article(liste_course2,nom)
            print(f"{nom} a été ajouter à la liste 2.\n")
        
    elif choix==2 :
        nom=input("entre le nom de l'article que tu veux supprimer\n") 
        if choix_liste == 1 :
            retirer_article(liste_course1,nom)
            print(f"{nom} a été supprimer de la liste 1.\n")
        elif choix_liste ==2 :
            retirer_article(liste_course2,nom)
            print(f"{nom} a été supprimer de la liste 2.\n")
    elif choix==3 : 
        if choix_liste == 1 :
            afficher_produit(liste_course1)
            
        elif choix_liste ==2 :
           afficher_produit(liste_course2)
    else : 
        break   