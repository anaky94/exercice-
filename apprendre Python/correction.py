"""
voici comment le programme doit se comporter :
1: demander à l'utilisateur si il souhaite convertir de pouce vers cm 
2: demander à l'utilisateur de rentrer la valeur à convertir ( en precisant l'unité )
3: afficher la valeur convertir 
 """

# convertion de unit1 vers unit2  
def effectuer_convertion(unit1, unit2, facteur):
    valeur_str=input( f"convertion {unit1} -> {unit2} . Donnez la valeur en pouces: {unit1} (ou 'q' pour quitter) ")
    if valeur_str=="q":
        exit()
    valeur_float=float(valeur_str)
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f" Résultat de la convertion {valeur_float} {unit1}= {valeur_convertie} {unit2}")

print("ce programme vous permet d'effectuer des convertion d'unité")
print("1 - pouces vers cm " )
print("2 cm vers pouces")
choice = input("choix (1 ou 2): " )
while True: 
    if choice=="1":
        effectuer_convertion("pouce", "cm", 2.54)
    if choice=="2":
        effectuer_convertion("cm","pouces", 0.394)