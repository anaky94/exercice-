 
#def effectuer_convertion(unit1: str, unit2: str, facteur: float):
#   valeur_str = input(f" convertion{unit1}->  ")

"""
True: l'utilisateur ne veut plus convertis 
False; L'utilisateur a donné une valeur a convertir
"""
def effectuer_convertion(unit1:str , unit2: str, facteur: float):  
    valeur_str=input(f"Conversion {unit1} -> {unit2}. donnez la valeur en {unit1} (ou 'q' pour quitter): ")
    if valeur_str == "q": 
        print("vous avez quitter")
        return True
    try:
        valeur_float=float(valeur_str)
    except ValueError:
        print("erreur rentré une valeur numérique\n utilisez le '.' et non une virgule ")
        print()
        return effectuer_convertion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float *2.54, 2)
    print(f"Resultat de la convertion: {valeur_float} {unit1} = {valeur_convertie}  {unit2}")
    return False



print("ce programme vous permet d'effectuer des conversions d'unitées ")
print("1-pouces vers cm ")
print("2-cm vers pouces ")
choix=input("votre choix (1 ou 2): ")

while True:
    if choix=="1":
       if effectuer_convertion("pouces", "cm", 2.54):
            break
    if choix =="2":
        if effectuer_convertion("cm", "pouces", 0.394):
            break
    