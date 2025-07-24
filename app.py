#Import des librairies utilisées
from os import error
from re import S
import sqlite3
import wikipedia

#Set up de la langue par défaut de wikipédia en français
#TODO permettre à l'utilisateur de changer la langue de wikipédia
# wikipedia.set_lang("fr")


#**Fonctions utilisées dans l'app

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

def add_to_db(answer):
    print("added to db")

def validate(user_validation):
    if user_validation in validate_list:
        return True
    else:
        return False
    

def search(answer):
    rep = wikipedia.search(answer, results = 1)
    print(rep)

    if rep == []:
        print("I don't know this person \n")
        rep = wikipedia.suggest(answer).title()
        
        user_validation = input(f"Did you mean {rep} ?").title()
        validate(user_validation)
        try:
            person = wikipedia.page(rep, auto_suggest=False)
            print(person.title, person.summary)
            user_validation = input("Do you want to add it to the db ?").title()
            validation = validate(user_validation)
            if validation == True :
                add_to_db(person)
        except wikipedia.exceptions.PageError as e:
            print(e)
    else :
        try:
            person = wikipedia.page(rep, auto_suggest=False)
            print(person.title, person.summary)
            user_validation = input("Do you want to add it to the db ?").title()
            validation = validate(user_validation)
            if validation == True :
                add_to_db(person)
        except wikipedia.exceptions.PageError as e:
            print(e)


#Variables globales
user_ans = ""
user_validation = ""

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


