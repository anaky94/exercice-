import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 4 


def poser_question():
    a= random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b= random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str=input(f"calculer:  {a}+{b} = ")
    reponse_int=reponse_str
    if reponse_int == a+b:
        print("Reponse correct")
    else:
        print("Reponse incorecte ")


# question N°1 sur 4
for i in range (0, NB_QUESTIONS):
    print(f"question N°{i+1} sur {NB_QUESTIONS}: ")
    poser_question()
    print()












