
#demander nom
nom=""
while nom=="":
    non=input("Quel est votre nom ?")


# demander age 
def demander_age():
    age_str=0
    while  age_str==0:
        age_str=input("quel est votre age ? ")
                
        try:
            age=int(age_str)
        except:
            print("erreur ")
    

demander_age()








































































































 














