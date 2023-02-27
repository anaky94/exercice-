#coding:utf-8
"""
 Importer un module : import <nom_module>
                      from < nom_module> import <nom_fonction>
                      from < nom_module> import 

module pour le joueur
"""
   

reponse ="rouge"
reponse = input("quel est votre reponse ? ")
print("votre reponse est bien " + reponse, "?")
if reponse == "rouge":
    print("vous y êtes presque continuer ainsi")
else:
    print("retentez plus tard ")


def demander_reponse():
    reponse = "rouge"
    while reponse == "":
        reponse=input("quel est votre reponse")
    return reponse

personne1= demander_reponse()
personne2= demander_reponse()