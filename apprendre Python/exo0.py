# ecrire un programme qui affiche une suite de 12 nombre dont chaque terme soit egal au triple du terme precedent 

a, c = 1, 1
while c <= 13:
    print(a, end=" ")
    a, c = a*3, c+1