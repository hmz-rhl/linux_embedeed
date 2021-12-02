#!/bin/bash

echo "
 #####     ###    ###       #####   ##  ##   ###        ###     ######   ######    ####    #####  ######
#######   #####   ###      #######  ### ###  ###       #####    ######  ### ###  ######  #######  ######
### # #  ### ###  ###      ### # #  ### ###  ###      ### ###    ###    ###  ##    ###   ### # #  ###
##       ### ###  ###      ##       ##  ###  ###      ### ###    ###    ### ###    ###   ##       ######
##       ### ###  ###      ##       ###  ##  ###      ### ###    ###    ######    ###    ##       #####
### # #  #######  ### ###  ### # #  ### ###  ### ###  #######    ###    ### ###   ###    ### # #  ###
#######  ### ###  #######  #######  #######  #######  ### ###    ###     ### ### #####   #######  #######
 #####    ##  ##   #####    #####    #####    #####    ##  ##   #####    ### ###  #####   #####    #####"

echo
echo " 1- Addition"
echo " 2- Soustraction"
echo " 3- Multiplication"
echo " 4- Division"
echo
read -p "choisir une opération : " choix

while [ $choix -lt 1 ] || [ $choix -gt 4 ]; do
	read -p "attention ! seulement entre 1 et 4: " choix
done

read -p "a: " a
echo
read -p "b: " b
echo 

case "$choix" in
	1)
	echo $a + $b =
	echo "scale=3; $a+$b" | bc;;
	2)
	echo $a - $b = 
	echo "scale=3; $a-$b" | bc;;
	3)
	echo $a * $b =
	echo "scale=3; $a*$b" | bc;;
	4)
	echo $a / $b =
	echo "scale=4; $a/$b" | bc;;
esac
