nombre=input("entre un chiffre \n")
taille=len(nombre)
tableau=list(map(int,nombre))
somme=0
for i in range(taille) : 
    somme = somme+tableau[i]
print(f"la somme des chiffres du nombre {nombre} est égale à :  {somme}")

