
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
# afficher_information_personne
# parametre: nom, age 
def afficher_informations_personne(nom, age):
    print("vous vous appeleez " + nom + ", vous avez"+str(age) + " ans ")
    print("l'an prochain vous aurez " + str(age+1)+"ans")



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

#=====================================================================>

#demander le nom
nom1 = demander_nom()
nom2 = demander_nom()


#demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#afficher les resultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)


#n = 0 # cree la variable 
#print(n)

#n = 10 # reaffecter la variable 
#print(n)
#n = n + 1 # incrémenter
#print(n)


"""print("debut de la boucle")
n=0
while n < 10:
    print("valeur de n :" + str(n))
    n = n + 1
print("fin de la boucle")
 """







