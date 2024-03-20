liste_etudiant=[{"nom":"Alice","age":20,"sexe":"F","niveau":"licence"},
                {"nom":"Bob","age":22,"sexe":"M","niveau":"Master"},
                {"nom":"Claire","age":21,"sexe":"F","niveau":"licence"},
                {"nom":"Sam","age":25,"sexe":"N","niveau":"licence"}]
a=[];b=[];c=[]
liste_menu=["Ajouter un étudiant","Afficher les étudiants masculins","Afficher les étudiants Feminin","Afficher les étudiants X",
            "Afficher la lise de tous les étudiants","quittez"]

def afficher_menu(liste) : 
    print("*****Menu principal*****\n")
    for i in range(len(liste)) : 
        print(f"{i+1} --- {liste[i]}.\n")

def afficher_tous_etudiants(liste) : 
    print("*****Liste complète des étudiants Dans liste*****\n")
    for i in range(len(liste)) : 
        print(f"{i+1} --- {liste[i]}.\n")

def ajouter_etudiant(liste,ajout):
    liste.append(ajout)
    
def mise_a_jour_etudiant(nom,age,sexe,niveau):
    for i in liste_etudiant : 
        if i["nom"]==nom : 
            i["age"]=age ;  i["sexe"]=sexe;  i["niveau"]=niveau

def tri_par_sexe(param):
    etudiantM=[] ; etudiantF=[] ; etudiantB=[]
    for i in range(len(param)) :
        if param[i]["sexe"]=="F":
            etudiantF.append(param[i])
        elif param[i]["sexe"]=="M":
            etudiantM.append(param[i])
        elif param[i]["sexe"]=="N":
            etudiantB.append(param[i])
    return etudiantF, etudiantM, etudiantB


afficher_tous_etudiants(liste_etudiant)
mise_a_jour_etudiant("Alice","25","N","Tiktok")
ajouter_etudiant(liste_etudiant,{"nom":"popina","age":25,"sexe":"F","niveau":"licence"}) 
a,b,c=tri_par_sexe(liste_etudiant)
print("feminin :" , a[0]["niveau"], "\nmasculin :",b, "\nbinaire :" , c) 




