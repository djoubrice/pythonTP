file =5
personne=["" for i in range(file*2)]
i=5
def affichage(listes, m) : 
     k=int(m)
     while k >0 :
        print(f"{listes[(int(k)*2)-1]}  ::  {listes[(int(k)*2)-2]}.  \n")
        k-=1

def moyenne(listes): 
    aget=0
    for i in range(5) : 
        aget=aget+int(listes[i*2])
    moy=aget/5
    return moy

while file >0 :
    nom=input("entrez votre nom.\n")
    age=int(input("quel est votre âge.\n"))
    personne[(file*2)-1]=nom ; personne[(file*2)-2]=age
    id_v=input("possedez vous une piece id valide? (oui/non)\n")
    if (age>=18) and (id_v=="oui") : 
        print(f"vous êtes autorisé à entrer dans la boite. car vous avez {age} et vous avez une ID valide.\n")
    else : 
        print(f"vous n'êtes autorisé à entrer dans la boite. car vous avez {age} ou vous n'avez pas une ID valide.\n")
    file -=1
affichage(personne,i)
print(f"la moyenne des ages est : {moyenne(personne)}")
