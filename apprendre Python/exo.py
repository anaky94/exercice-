def demander_nombre(nb_min, nb_max):
    nombre_str = input(f"quel est le nombre magi enntre {nb_min} et {nb_max} ? ")
    nombre_int=int(nombre_str)
    return nombre_int
    

NOMBRE_MIN = 1
NOMBRE_MAX=10
NOMBRE_MAGIQUE=50
nombre=0

while not nombre ==NOMBRE_MAGIQUE:
    nombre = demander_nombre (NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("bravo vous avez gagner")
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre est plus petit")
    else:
        print("le nombre est plus grand ")
















