#Projet 2 : Calculatrice avec Gestion des erreurs

a = b = ""


while not (a.isdigit() and b.isdigit()):
    a = input("Veuillez entrer un premier nombre :")

    b = input("Veuillez entrer un deuxième nombre:")

    if not (a.isdigit() and b.isdigit()):

        print("Veuillez entrer deux nombres valides")


print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {int(a) + int(b)}.")
