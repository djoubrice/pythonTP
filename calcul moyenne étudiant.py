nom=input("entrez le nom de l'étudiant...\n")
i=0
note=[]
matière=[]
somme=0
#vérifie si le nombre de matière entré est réellement un chiffre. 
while True :
    try:
        nb=int(input("entrez le nombre de matière...\n"))
    except ValueError:
        print("Votre réponse n'est pas acceptable, veuillez entrer une valeur Valide")
        continue
    else : 
        break

for i in range(nb):
    matière.append( input("entre le nom de la matière\n"))
    while True :
        try:
            note.append( float(input(f"entre la note de la matière {matière[i]}\n")))
        except ValueError:
            print("Votre réponse n'est pas acceptable, veuillez entrer une valeur Valide")
            continue
        else : 
            break
    somme=somme+note[i]
moyenne=somme/nb

print(f"\nl'étudiant {nom} à obtenue la note de : {moyenne}\n")
print(f"### détails des notes de Mr {nom} ###")
for i in range(nb) :
    print(f"{matière[i]} ------ note : {note[i]}")
