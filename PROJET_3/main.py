# Projet 3 : Création d'une liste de courses

import sys

LISTE = []

MENU = """Choississez parmi les 5 options suivantes :  
1.  Ajouter un élément à la liste de courses
2.  Retirer un élément de la liste de courses
3.  Afficher les éléments de la liste de courses
4.  Vider la liste de courses
5.  Quitter le programme
0 Votre Choix: """


CHOIX_MENU = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)
    if user_choice not in CHOIX_MENU:
        print("Veuillez choisir une action valide...")
        continue

    if user_choice == "1": #Ajout élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses :")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste de courses !")
    
    elif user_choice == "2": #Supprimer élément
        item = input("Veuillez choisir l'élément à supprimer de la liste de courses :")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été retiré de la liste de courses !")
        else:
            print(f"L'élément {item} n'est pas présent dans liste !")

    elif user_choice == "3": #Afficher élément de la liste
        print(f"Veuillez trouver votre liste de courses ci-dessous :")
        for i, item in enumerate(LISTE, 1):
            print(f"{i}. {item}")
    
    elif user_choice == "4": #Vider liste de courses
        LISTE.clear()
        print("La liste a été vidée !")

    elif user_choice == "5": #Quitter le programme
        print("Au revoir !") 
        sys.exit()

    print("-" * 50)
