#coding:utf-8
"""
 Importer un module : import <nom_module>
                      from < nom_module> import <nom_fonction>
                      from < nom_module> import 

module pour le joueur
"""
   

"""
pour effectuer un test sur l'ensemble du module 
if __name__=="__main__":
    print("bonjour, tout le monde")
    au_revoir()
"""
def parler(personnage, message):
    print ("{} : {}".format (personnage, message))

def au_revoir():
    print("au_revoir :) !")

if __name__=="__main__":
    print("bonjour, tout le monde")
    au_revoir()