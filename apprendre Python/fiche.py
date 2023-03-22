
#On demande le nom et l'age de la personne
# Premier programme

nom = input("quel est votre nom ? ")
age = int(input("quel est votre age ? "))

try:
    age_prochain = int(age) + 1
except:
    print("Erreur Vous devez rentrer un nombre pour l'age")


print("vous vous apeler " + nom + " et vos avez "+str(age)+" ans")
print("vous aurez "+str(age_prochain)+" ans l'année prochaine")




