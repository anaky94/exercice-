
"""" premier programme Formation Pyhon 

#nom = input("quel est ton nom? " )
#age = input("quel est votre age? ")

#print(type(nom))
#print(type(age))
#str(38) --> "38"
#1,5 --> float
# vrai ou faut boolean (true/false)
#str--> int int 

nom = "toto"
age =  30

nom = input("quel est vontre nom? " )
age = input("quel est votre age? " )

try:
    age_prochain = int(age) + 1 
except ValueError:
    print("Ereeur: vous devez rentrer un nombre pour L'age ")
else:
    print("vous avez appelez" + nom + ",vous avez" + str(age) + "ans")
    print("l'an prochain vous aurez " + str(age_prochain) + "ans")

""" 
""" 
n = 0 # cree la variable 
print(n)

n = 10 # reaffecter la variable 
print(n)
n = n + 1 # incrémenter
print(n)
""" 
print("debut de la boucle")
n=0
while n < 10:
    print("valeur de n :" + str(n))
    n = n + 1
print("fin de la boucle")








