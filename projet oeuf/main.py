import time
print("cuissons des oeufs")
print("1 oeuf à la coque : 3 min ")
print("2 oeuf  mollets : 6 minutes ")
print("3 oeuf durs : 9 minutes")
while True:
    choix= input("votre choix: ")
    if choix== "1" or choix == "2" or choix == "3":
        break
    print("Erreur: vous devez choisir 1, 2 ou 3\n")

duree= 0
if choix== "1":
    duree=3*60
if choix =="2":
    duree= 6*60
if choix == "3":
    duree= 9*60


while duree > 0:
    for i in range(5):
        time.sleep(1)
        print( ".", end="", flush=True)
        duree -= 1 
        if duree <= 0:
            break         
      
    

    min = duree // 60
    sec = duree-min *60
    print()
    print(f"temps restant :{min:02d}:{sec:02d}", end="", flush= True)

print (" cuisson terminé ")



















