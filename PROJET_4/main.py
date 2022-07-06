#Projet 4 : Création du jeux du "nombre mystère"

from random import randint

#Générer le nombre aléatoire entre 0 et 100

nombre_a_trouver = randint(1, 100)

essai_restant = 5

print("***LE JEU DU NOMBRE MYSTERE***")

#Debut de la boucle

while essai_restant > 0:
    print(f"Il te reste {essai_restant} essai{'s' if  essai_restant > 1 else ''}")

#Si l'utilisateur entre autre chose qu'un nombre, afficher " Veuillez entrer un nombre valide"

    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entre un nombre valide")
        continue

#Afficher si le nombre de l'user est plus petit ou plus grand que le nombre mystère

    user_choice = int(user_choice)

    if nombre_a_trouver > user_choice:
        print(f"C'est plus grand que {user_choice}.")
    elif nombre_a_trouver < user_choice:
        print(f"C'est plus petit que {user_choice}.")
    else:
        break

    essai_restant -= 1

#Afficher gagné ou perdu

if  essai_restant == 0:
    print(f"Dommage, le nombre mystère était {nombre_a_trouver}.")
else:
    print(f"Bravo ! Le nombre mystère était {nombre_a_trouver}")
    print(f"Tu as trouvé le nombre mystère en {6 - essai_restant} essai")

print("Fin du game")
