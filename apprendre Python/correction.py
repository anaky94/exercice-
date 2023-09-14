"""
voici comment le programme doit se comporter :
1: demander à l'utilisateur si il souhaite convertir de pouce vers cm 
2: demander à l'utilisateur de rentrer la valeur à convertir ( en precisant l'unité )
3: afficher la valeur convertir 
 """

print("ce programme vous permet d'effectuer des convertion d'unité")
print("1 - pouces vers cm " )
print("2 cm vers pouces")
choice = input("choix (1 ou 2): " )
if choice=="1":
    valeur_str=input( "convertion pouces -> cm. Donnez la valeur en pouces:  ")
    valeur_float=float(valeur_str)
    valeur_convertie=valeur_float*2.5
    print(f" Résultat de la convertion {valeur_float} pouces= {valeur_convertie} cm")