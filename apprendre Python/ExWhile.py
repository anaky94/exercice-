#ex 1
# Ecrire un programme qui affiche les 20 premeiers 
#termes de la table de multiplication par 7
"""
age = input("quel age as tu ? ")
age = int(age)

if age > 0 and age <= 100:  
    print(" L'age est validé")
else:
    print("l'age est incorect")
"""

"""
Gérer les exceptionns:  
Element à retenir dans tout les cas de figure : 
     try/except    
     (else/finally)
      Types dexception    : ValueError
                          NameError
                          TypeError 
                          ZeroDivisionError 
                          OsError
                          AssertionError

    
"""
"""
ageUtulisateur = input("Quel age as-tu?")

try: 
    ageUtulisateur = int(ageUtulisateur)
    
except:
    print("l'age indiqué est incorect !")
else:
    print("tu as", ageUtulisateur, "ans")
finally: 
    print("Fin du progarmme")
"""












