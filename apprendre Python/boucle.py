"""for num_client in range (1,4 ):
    print("vous etes le client n°"+ str(num_client))
"""
# for each : pour chaque valeur d'une liste données 



age_prochain=0
while age_prochain==0:
    age = input("quel est votre age ? ")
    try:
        age_prochain = int(age) + 1
    except:
        print("Erreur")
       

print("vous vous avez " + str(age)+ " ans" )

age_prochain=""
while age_prochain=="":
    age=input("quel est votre age? ")
    try:
        age_prochain = int(age)+1
    except:
        print("erreur")
