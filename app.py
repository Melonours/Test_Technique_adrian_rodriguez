#Import des librairies utilisées
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


#Fonction d'insertion de la data dans la DB
def add_to_db(data):
    # print(data.title, data.summary)
    title = data.title
    summary = data.summary
    data_to_insert = [title, summary]
    # print(type(title), type(summary))
    con = sqlite3.connect("wikiDB.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS famous_people(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(65) , summary VARCHAR(127))")
    cur.execute(f"INSERT INTO famous_people(name, summary) VALUES (?, ?)", data_to_insert)
    con.commit()

    #* Décommenter ceci afin de pouvoir voir l'ensemble des données dans la db 
    for row in cur.execute('SELECT * FROM famous_people'):
        print(row)

    con.close
    
    print("Data added succesfully !")

#Fonction de validation du choix de l'utilisateur
def validate(user_validation):
    if user_validation in validate_list:
        return True
    else:
        return False

#Fonction de recherche sur wikipedia et gestion d'erreurs si page non trouvée    
def wikipedia_search(rep):
    try:
        person = wikipedia.page(rep, auto_suggest=False)
        # print(person.original_title, person.summary)
        user_validation = input(f"Do you want to add {person.title} to the db ?").title()
        validation = validate(user_validation)
        if validation == True :
            add_to_db(person)
        else:
            print("Insertion aborted")
    except wikipedia.exceptions.PageError as e:
            print(e)

#Fonction principale de rechercher de l'application
def search(answer):
    rep = wikipedia.search(answer, results = 1)
    # print(rep)

    if rep == [] or None:
        print("I don't know this person \n")
        rep = wikipedia.suggest(answer)
        if rep == None :
            print("Can't search for an empty query !")
        else:
            user_validation = input(f"Did you mean {rep} ?").title()
            validation = validate(user_validation)
            if validation == True:
                wikipedia_search(rep)
            else :
                print("Alright")
        #* Refactorisé dans une seule fonction afin d'éviter la répétition
        # try:
        #     person = wikipedia.page(rep, auto_suggest=False)
        #     print(person.title, person.summary)
        #     user_validation = input("Do you want to add it to the db ?").title()
        #     validation = validate(user_validation)
        #     if validation == True :
        #         add_to_db(person)
        # except wikipedia.exceptions.PageError as e:
        #     print(e)
    else :
        wikipedia_search(rep)
        #* Refactorisé dans une seule fonction afin d'éviter la répétition
        # try:
        #     person = wikipedia.page(rep, auto_suggest=False)
        #     print(person.title, person.summary)
        #     user_validation = input("Do you want to add it to the db ?").title()
        #     validation = validate(user_validation)
        #     if validation == True :
        #         add_to_db(person)
        # except wikipedia.exceptions.PageError as e:
        #     print(e)


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
        print("Bye bye !")
        break
    if cmd == "help":
        print(f"\nHere are the available commands : {commands} ")
    if cmd not in commands: 
        print('\nUnknown command, type "help" to see the available commands')
    if cmd == "search":
        user_ans = input("\nPlease type the name of the person you're looking for : \n")
        if user_ans.isdigit():
            print("Can't search for only numbers !")
        else :
            search(user_ans)


