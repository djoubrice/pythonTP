j=0 ; k=0
boites_outils=["tournevis","Marteau","clé","piles","scie","peinture","rouleau"]
boites_outils.append("fers")
print(boites_outils)
for i in boites_outils : 
    if i == "scie" : 
        j=boites_outils.index("scie")
        nom=boites_outils[j]
        boites_outils.remove(i)
        k+=1
if k==0 : 
    print("scie n'est pas dans la liste ")

else : 
    print(f"{nom} a été trouvé dans la liste à l'index {j}.\n")

