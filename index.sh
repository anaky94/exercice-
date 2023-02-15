#!/bin/bash 

#let nember=145+6
# result=$((45+23))
#number=$((96 + 4444))
#echo $number 


# bourne (sh) --> bash, csh, zsh, ksh 
# - lt, -l 
# -gt, -ge
# -eq, -ne
# =, !=
# -e : existe dans le répertoire courant 
# -f : si c'est un fichier 
# -d : si c'est un répertoire 

nb1='hello'
nb2='world'
nb3='world'

if [ $nb1 -le $nb2] ; then 
    echo 'nb1 < nb2' 
elif [ $nb1 -gt $nb2] ; then 
    echo 'nb1> nb2'
else 
    echo 'nb1 = nb2'
fi
