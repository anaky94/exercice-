 
"""" premier programme Formation Pyhon 

#nom = input("quel est ton nom? " )
#age = input("quel est votre age? ")

#print(type(nom))
#print(type(age))
#str(38) --> "38"
#1,5 --> float
# vrai ou faut boolean (true/false)
#str-->chaine / int --> 
"""
# == égal 
# < inférieur 
# <= inérieur ou égal
# > supérieur 
# >=supérieur ou égal
# true / False (boolean)
# elif --> else /if 
# age > 60 : vous etes sénior
#age < 10 : vous êtes enfant
# ado si age >= 12 et age < 18 
# bebe si age == 1 ou age 2 
# afficher_information_personne
# parametre: nom, age 

def afficher_informations_personne(nom, age, taille=0):
    print()
    print("vous vous appeleez " + nom + ", vous avez "+str(age) + " ans ")
    print("l'an prochain vous aurez " + str(age+1)+" ans")

    
    if age == 17:
        print("vous êtes presque majeur")
    elif 12 <=  age < 18:
        print("vous etes ado")
    elif age == 1 or age == 2:
        print("vous êtes un bebe")
    elif age == 18:
        print("vous êtes juste majeur")
    elif age > 60:
        print("vous êtes sénior")
    elif age < 10:
        print("vous êtes enfant")
    elif age >= 18:
        print("vous etes majeurs")
    else:
        print("vous êtes mineur")
    if not taille ==0:
        print("votres taille : "+ str(taille) + "m")


def demander_nom():
    reponse_nom= ""
    while reponse_nom=="":
        reponse_nom=input("quel est votre nomm ?")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str =input(nom_personne+ " quel est votre age ? ")
        try:
            age_int = int(age_str)
        
        except ValueError:
            print("Ereur: vous devez rentrer un nombre pour L'age ")
    return age_int 


#demander le nom
#nom1 = demander_nom()
#nom2 = demander_nom()

#nom1 = "personne1"
#nom2 = "personne2"

#demander l'age
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

#afficher les resultats
#afficher_informations_personne(nom1, age1)
#afficher_informations_personne(nom2, age2)


#n = 0 # cree la variable 
#print(n)

#n = 10 # reaffecter la variable 
#print(n)
#n = n + 1 # incrémenter
#print(n)

 
NB_PERSONNES = 1
for i in range(0,NB_PERSONNES):
    nom = "personne " + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom, age, 1.89)







