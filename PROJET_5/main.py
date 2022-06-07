#Création d'un jeu de rôle pour le terminal

from random import randint


hero_health = 50
mob_health = 50
nombre_de_potions = 3
passer_son_tour = False

while True:
    if passer_son_tour:
        print("Le hero passe son tour.")
        passer_son_tour = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou souhaitez-vous utiliser une potion (2) ? ")

#Mouvement du joueur
        if user_choice == "1":
            hero_attack = randint(5, 10)
            mob_health -= hero_attack
            print(f"Vous avez infligé {hero_attack} de dégats au monstre")

        elif user_choice == "2" and nombre_de_potions > 0:
             potion_health = randint(15,30)
             hero_health += potion_health
             nombre_de_potions -= 1
             passer_son_tour = True
             print(f"Vous avez récupéré {potion_health} de points de vie grace à la potion.")
        else:
            print("Vous n'avez plus de potions...")
            continue

    if mob_health <= 0:
        print("Tu as gagné le combat !")
        break

#Mouvement du mob
    ennemy_attack = randint(5, 15)
    hero_health -= ennemy_attack
    print(f"L'ennemi inflige {ennemy_attack} de dégats au héro")

    if hero_health <= 0:
        print("Vous avez perdu ce combat !")
        break

#Stats à chaque tour
    print(f"Il vous reste {hero_health} points de vie.")
    print(f"Le mob a encore {mob_health} points de vie.")
    
    print("-" * 50)

print("FIN DU GAME")
