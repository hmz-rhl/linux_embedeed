# Projet4

le projet4 consiste a utiliser les capteurs d'une [sense-hat](https://pythonhosted.org/sense-hat/) brancher a un [RaspberryPi](https://www.raspberrypi.com) sur le reseau local pour les afficher dans un dashboard [Node-Red](https://nodered.org)
la communication entre la raspberry et le serveur se fait par le protocole mqtt.

il y a 6 topics hebergé par la machine server:
matrice
temperature
pressure
humidity
meteo
compass

il y a d'une part le serveur qui recuperera les information provenant du sense-hat et les affichera dans un dashboard. Lui, est abonne a tous les topics de la sense-hat sauf matrice ou il est publisher.

et d'autre part la raspberry qui enverra ses informations, ainsi q'affichera le texte recu par le serveur. Elle, est abonnee a un seul topics "matrice", et publies dans tous les autres topics.

## Prerequis

### machine serveur (rapsberry ou autre sous linux)

il vous faut Node-Red:
#   installation de Node-Red et mosquitto:
'''
#   mettre a jour les paquets
sudo apt-get update

#   installation de mosquitto
sudo apt-get install mosquitto mosquitto-clients

#   installation de Node-Red
sudo apt-get install node-red

### RaspberryPi avec sense-hat

il vous faut Node-Red, pyton, mosquitto ainsi que le module sense-hat:
'''bash
#   mettre a jour les paquets
sudo apt-get update

#   installation de python
sudo apt-get install python

#   installation du module
sudo apt-get install sense-hat

#   installation de Node-Red
sudo apt-get install node-red

'''

## configuration

recuperer le fichier flow.js et le dossier script, et deposer les dans votre repertoire personnel.
lancer node-red sur les deux machines, puis toujours sur les deux machines ouvrez : ** http://localhost:1880  **



### machine serveur (sur rapsberryPi ou tout autre sous linux)

importez le flow_server.js dans node-red, et deployez le.
veillez a récuperer l'adresse ip qu'on nommera **IPserver** de cette machine vous en aurez besoin pour la configuration de la sense-hat

### Sense-hat

importez le flow_sense_hat.js
ouvrez un node mqtt et configurer le pour qu'il se connecte au bon server, donc mettez l'adresse ip de la machine server.
Deployez le flow.

## Utilisation

### Interface Node-Red
vous ouvrez un navigateur et vous tapez: ** http://IPserver:1880/ui **

### Possibiltes

#### Web API

joke : api qui génère une blague aleatoire
temperature a paris

#### Sensors

Boussole
thermometre
hygrometre
pression atm.

#### Matrix

envoyer des messages colore qui s'affiche sur la sense-hat



