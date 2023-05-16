 
#def effectuer_convertion(unit1: str, unit2: str, facteur: float):
#   valeur_str = input(f" convertion{unit1}->  ")

def effectuer_convertion(unit1 , unit2, facteur):  
    valeur_str=input(f"Conversion {unit1} -> {unit2}. donnez la valeur en {unit1} (ou 'q' pour quitter): ")
    if valeur_str == "q": 
        return True
    valeur_float=float(valeur_str)
    valeur_convertie = round(valeur_float *2.54, 2)
    print(f"Resultat de la convertion: {valeur_float} {unit1} = {valeur_convertie}  {unit2}")



print("ce programme vous permet d'effectuer des conversions d'unitées ")
print("1-pouces vers cm ")
print("2-cm vers pouces ")
choix=input("votre choix (1 ou 2): ")

while True:
    if choix=="1":
        effectuer_convertion("pouces", "cm", 2.54)
    if choix =="2":
        effectuer_convertion("cm", "pouces", 0.394)
    