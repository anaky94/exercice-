
import random
   
a=NOMBRE_MIN=1
b=NOMBRE_MAX= 10 
NB_QUESTION =4
moyenne=int(2)

def poser_question():
   a=random.randint(NOMBRE_MIN, NOMBRE_MAX)
   b=random.randint(NOMBRE_MIN, NOMBRE_MAX)
   o=random.randint(0,1)

   
   operateur_str="+"
   if o ==1:
      operateur_str="*"

   reponse_str= input(f"calculer  : {a} {operateur_str} {b} =")
   reponse_int=int(reponse_str)
   calcul=a+b
   if o==1:
      calcul=a*b
   
   if reponse_int == calcul:
      return True
      #print("réponse correcte")
   return False
     # print("reponse incorect")
      

NB_points = 0
for i in range(0, NB_QUESTION):
   print( f"questionn {i+1} sur {NB_QUESTION}:")
   if poser_question():
      print("Reponse corecte")
      NB_points += 1
   else:
      print("reponse incorecte")
   print()

print( f"votre note est {NB_points} /{NB_QUESTION}")
if NB_points == NB_QUESTION:
   print("Ecxellent")
elif NB_points ==0:
   print("Réviser vos Maths")
elif NB_points > moyenne:
   print("pas mal")
else:
   print("peut miux faire")


print("fin de la partie")


 


























































































