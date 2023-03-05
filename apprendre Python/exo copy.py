import random

def demander_nombre(nb_min, nb_max):
    nombre_int= 0 
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magigique entre {nb_min} et {nb_max} ? ")
        try:   
            nombre_int=int(nombre_str)
        except:
            print("Erreur: vous devez rentrer un nombre. Réesayer ")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: Le nombre doit être entre {nb_min} et {nb_min}. Reésayer")
                nombre_int=0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX=10
NOMBRE_MAGIQUE= random.randint(NOMBRE_MIN, NOMBRE_MAX)
nombre=0
NB_VIES=4
vies=NB_VIES


while not nombre == NOMBRE_MAGIQUE and vies >0 :
    print( f"Il vous reste {vies} vies ")
    nombre = demander_nombre (NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("bravo vous avez gagner !")
        print (f"Il vous restait {vies} vies " )
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre est plus petit")
        vies -=1
    else:
        print("le nombre est plus grand ")
        vies -=1
if vies==0:
    print(f"Vous avez perdu ! le nombre magique etais : {NOMBRE_MAGIQUE} ")














































































































 














