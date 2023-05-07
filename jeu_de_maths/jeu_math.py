import random
NOMBRE_MAX=10
NOMBRE_MIN=1

def poser_question():
    a=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    poser_qusestion=int(input(f"calculer {a}+{b}"))
    poser_qusestion=question_str
    if poser_qusestion == a+b:
        