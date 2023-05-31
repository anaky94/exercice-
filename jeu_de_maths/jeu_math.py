import random
<<<<<<< HEAD
NOMBRE_MAX=10
NOMBRE_MIN=1

def poser_question():
    a=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    poser_qusestion=int(input(f"calculer {a}+{b}"))
    poser_qusestion=question_str
    if poser_qusestion == a+b:
        
=======

NOMBRE_MAX=100
NOMBRE_MIN=10
NB_QUESTION=4
MOYENNE=int(NB_QUESTION)

def poser_question():

    a=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    O=random.randint(0,1)
    #0->+
    #1->*
    opérateur_str="+"
    if O ==1:
        opérateur_str="*"

    reponse_str=input(f"calculer {a} {opérateur_str} {b} =")
    peponse_int=int(reponse_str)

    calcule=a+b
    if peponse_int == calcule:
        
        return True
        
    return False



poser_question()
nb_point =0
for i in range(0, NB_QUESTION):
    print (f"question n{i+ 1} sur {NB_QUESTION}:")
    if poser_question():
        print("Réponse correcte")
        nb_point +=1
    else:
        print("reponse incorrecte")
    print()


print(f"votre note est de {nb_point} / {NB_QUESTION}") 
if nb_point == NB_QUESTION:
    print("excellent")
elif nb_point ==0: 
    print("Révisez vos maths !")
elif nb_point>MOYENNE:
    print("pas mal")
else: 
    print("peut mieux faire")










































>>>>>>> 81c916a046e3832fd10c62803724374d1b14dc27
