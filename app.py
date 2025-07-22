#import des librairies utilisées
import sqlite3
import wikipedia



commands = ["exit", "help", "joe", "search"]

print('Bienvenue sur l\'application ! \n \n"help" : afin de voir les commandes disponibles')

while True : 
    cmd = input("\n > 2")
    if cmd == "exit":
        print("bye")
        break
    if cmd == "help":
        print("voici la liste des commandes disponibles : ")
    if cmd not in commands: 
        print('commande non connue \n"help" : pour voir les commandes disponibles')
    if cmd == "search":
        user_ans = input("veuillez entrez le nom de la personne recherchée : \n ")
        