 
#def effectuer_convertion(unit1: str, unit2: str, facteur: float):
#   valeur_str = input(f" convertion{unit1}->  ")


print("ce programme vous permet d'effectuer des conversions d'unitées ")
print("1-pouces vers cm ")
print("2-cm vers pouces ")
choix=input("votre choix (1 ou 2): ")
if choix =="1":
    valeur_str=input("Conversion vers cm. donnez la valeur en pouces: ")
    valeur_float=float(valeur_str)
    valeur_convertie = round(valeur_float *2.54, 2)
    print(f"Resultat de la convertion: {valeur_float} pouces = {valeur_convertie} cm ")

   def effectuer_convertion("pouces", "cm", 2.54):

if choix =="2":
    valeur_str=input("Conversion vers pouces. donnez la valeur en cm: ")
    valeur_float=float(valeur_str)
    valeur_convertie = round(valeur_float *0.394, 2)
    print(f"Resultat de la convertion: {valeur_float} cm = {valeur_convertie} pouces ")
    
    def effectuer_convertion("pouces", "cm", 2.54):