

   
a=NOMBRE_MIN=1
b=NOMBRE_MAX= 10 
NB_QUESTION =4

def poser_question():
   reponse_str= input(f"calculer  : {a} + {b}=")
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




 


























































































