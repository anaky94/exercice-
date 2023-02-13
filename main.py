
"""" premier programme Formation Pyhon 

#nom = input("quel est ton nom? " )
#age = input("quel est votre age? ")

#print(type(nom))
#print(type(age))
#str(38) --> "38"
#1,5 --> float
# vrai ou faut boolean (true/false)
#str--> int int 
"""
"""
nom = input("quel est vontre nom? " )

age = 0
while age ==0:
    age_str = input ("quel est votre age ")
    try:
        age = int(age_str) + 1 
    except:
        print("Ereeur: vous devez rentrer un nombre pour L'age ")

#print("fin de la boucle")    

print("vous avez appelez" + nom + ",vous avez " + str(age) + " ans")
print("l'an prochain vous aurez " + str(age + 1 ) + " ans")
"""


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

#mot_de_passe= ""
mot_de_passe= input("quel est le mot de passe? ")
while  not mot_de_passe == "majabu":
    mot_de_passe = input("Quel est le mot de passe ? ")
print("Mot de passe corect bienvenue " + mot_de_passe + " !" )





