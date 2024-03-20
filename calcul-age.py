import datetime

def display_age(nom1,annee1) :{
    print(f"Mr/Mme {nom1}  vous avez actuellement {datetime.date.today().year-annee1} Ans;\nen 2050 vous aurez {2050-annee1} Ans.")
}    
nom=input("entre ton nom.\n")
naissance=int(input("entre ton année de naissance.\n"))
display_age(nom, naissance)


