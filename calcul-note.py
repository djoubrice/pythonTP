import statistics
def calcul_moy(listes) :
     return statistics.mean(listes)

nombre_matiere=0 ;  i=0

nom=input("entre le nom de l'étudiant.\n")
nombre_matiere=int(input(f" entre le nombre de matière de l'étudiant {nom}.\n"))
note_mat=[0 for i in range(nombre_matiere)]
nom_mat=["" for i in range(nombre_matiere)]

while nombre_matiere > 0 :
     nombre_matiere -=1
     nom_mat[i]=input("entre de le nom de la matière.\n")
     note_mat[i]=int(input("entre la note de la matière.\n"))
     
moy=calcul_moy(note_mat)

print(moy)
