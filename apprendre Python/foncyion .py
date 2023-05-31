


#definition de la fonction 
def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas passé de nom l'age vaut",age)
    else:
        if age==0:
            print ("l apersonne est", nom)
        else:
            print("la personne est",nom, ",son age est" ,age, "ans")
    print("le nom comporte",len(nom), "caractère")



afficher_infos_personne()








