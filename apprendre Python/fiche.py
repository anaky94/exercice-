
#On demande le nom et l'age de la personne
# Premier programme

nom = input("quel est votre nom ? ")
age = input("quel est votre age ? ")


age_prochain=0
while age_prochain==0:
    print("Quel est votre age? ")
    try:
        age_prochain = int(age) + 1
    except ValueError :
        print("Erreur: Vous devez rentrer un nombre pour l'age")
  
print("fin de la boucle")
#print("vous vous apeler " + nom + " et vos avez "+str(age)+" ans")
#print("vous aurez "+str(age_prochain)+" ans l'année prochaine")












