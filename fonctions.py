def display(nombre1,nombre2) :
    moy=(nombre1+nombre2)/2
    return moy
    #print(f"la moyenne de : {i}  et de {j}  est : {(i+j)/2}.\n")

premier=int(input("entre le premier nombre.\n"))
deuxième=int(input("entre le second nombre.\n"))
print(f"la moyenne de : {premier}  et de {deuxième}  est : {display(premier,deuxième)}.\n")

