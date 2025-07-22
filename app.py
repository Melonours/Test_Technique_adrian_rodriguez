#Import des librairies utilisées
import sqlite3
import wikipedia

#Set up de la langue par défaut de wikipédia en français
wikipedia.set_lang("fr")


#Fonctions utilisées dans l'app

#Fonction d'insertion dans la DB


#Fonction de recherche du nom demandé par l'utilisateur sur wikipédia
def validate(user_request):
    value = wikipedia.search(user_request, results= 1)
    print(value)
    joe = wikipedia.page(value)
    print(joe.title, joe.summary)

#Fonction de lancement de la recherche et de suggestion en cas de mauvaise typo
def search(answer): 
    validate_list = ["Yes", "Oui", "Y", "O", ""]

    search_name = wikipedia.suggest(answer)

    validate_search = input(f"Did you mean {search_name.title()} ?").capitalize()

    if validate_search in validate_list:
            
        validate(search_name)



#Variables globales
user_ans = ""

commands = ["exit", "help", "search"]


#Début de l'app
print('Welcome to the app ! \n \nType "help" to see more commands')

while True : 
    cmd = input("\n >>")
    if cmd == "exit":
        print("bye")
        break
    if cmd == "help":
        print(f"\nHere are the available commands : {commands} ")
    if cmd not in commands: 
        print('\nUnknown command, type "help" to see the available commands')
    if cmd == "search":
        user_ans = input("\nPlease type the name of the person you're looking for : \n")
        search(user_ans)


