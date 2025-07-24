#Import des librairies utilisées
from os import error
import sqlite3
import wikipedia

#Set up de la langue par défaut de wikipédia en français
# wikipedia.set_lang("fr")


#Fonctions utilisées dans l'app

#Fonction d'insertion dans la DB


#Fonction de recherche du nom demandé par l'utilisateur sur wikipédia
# def validate(user_request):
#     print(user_request)
#     value = " "
#     value = wikipedia.search(user_request, results = 1)
#     print(value)
#     joe = ""
#     joe = wikipedia.page(title = value)
#     print(joe.title)

#     try :
#         print(joe.summary)
#     except wikipedia.exceptions.DisambiguationError as e :
#         print(e.options)



#Fonction de lancement de la recherche et de suggestion en cas de mauvaise typo
# def search(answer): 
#     validate_list = ["Yes", "Oui", "Y", "O", ""]

#     search_name = wikipedia.suggest(answer)
#     print(str(search_name))

#     if search_name == None :
#         mex = wikipedia.search(answer)
#         print(mex)

#     validate_search = input(f"Did you mean {search_name} ?").capitalize()

#     if validate_search in validate_list:
#         print(search_name)
#         validate(search_name)
#     else :
#         print("joe")

def validate(user_validation):
    

def search(answer):
    rep = wikipedia.search(answer, results = 1)
    print(rep)

    if rep == []:
        print("I don't know this person \n")
        rep = wikipedia.suggest(answer).title()
        input(f"Did you mean {rep} ?")

    validate()

    person = wikipedia.page(rep, auto_suggest=False)
    print(person.title)

#Variables globales
user_ans = ""

commands = ["exit", "help", "search"]

validate_list = ["Yes", "Oui", "Y", "O", ""]

#Début de l'app
print('Welcome to the app ! \n \nType "help" to see more commands')

while True : 
    cmd = input("\n >>").strip()
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


