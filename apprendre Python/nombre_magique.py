
import random


def demander_nombre(nb_min, nb_max):
    nombre_int=0
    while nombre_int==0:
        nombre_str=input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ")
        try:
            nombre_int= int(nombre_str)
        except:
            print("Erreur rentrez un nombre")
        else: 
            if nombre_int < nb_min or nombre_int > nb_max: 
                print(f"Erreur le nombre doit entre {nb_min} et {nb_max}. Réesayer")
                nombre_int =0
    return nombre_int

NOMBRE_MAX=10
NOMBRE_MIN= 1
NOMBRE_MAGIQUE=random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES=4
nombre =0
vies=NB_VIES

while not nombre == NOMBRE_MAGIQUE and vies >0:
    nombre=demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    print(f"il vous reste {vies} vies")
    if nombre == NOMBRE_MAGIQUE :
        print("Félicitation vous avez Gagnez !")
    elif nombre >NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies-=1
    else:
        print("Le nombre magique est plus grand ")
        vies-=1
if vies==0:
    print(f"vous avez Perdu  le nombre magique etais {NOMBRE_MAGIQUE} !") 



























