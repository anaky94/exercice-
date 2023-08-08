

   
a=NOMBRE_MIN=1
b=NOMBRE_MAX= 10 
NB_QUESTION =4
moyenne=2,5

def poser_question():
   reponse_str= input(f"calculer  : {a} + {b} =")
   reponse_int=int(reponse_str)
   if reponse_int == a+b:
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
elif NB_points> moyenne:

# votre note est de 2/4 -> Excellent!
# 0 --> réviser vos maths!
# moyenne --> int(NB_QUESTION) 2.5 --> é 
# < moyenne --> peut mieux faire 

print("fin de la partie")


 


























































































