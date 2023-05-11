import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 4 


def poser_question():
    a= random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b= random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str=input(f"calculer:  {a}+{b} = ")
    reponse_int=int(reponse_str)
    if reponse_int == a+b:
        return True
        #print("Reponse correct")
    
        #print("Reponse incorecte ")
    return False

nb_point=0
for i in range (0, NB_QUESTIONS):
    print(f"question N°{i+1} sur {NB_QUESTIONS}: ")
    if poser_question():
        print("Reponse Correcte")
        nb_point +=1
    else:
        print("Réponse incorrecte")
    print()
   
print(f"votre note est {nb_point}/{NB_QUESTIONS}")









































































































