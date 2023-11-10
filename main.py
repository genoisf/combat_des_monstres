#créé par Francis Genois
#créé en 2022
#combat de monstres TP3

from random import*
#les variables
pointVie = 20
force_adversaire = 0
numero_combat = 0
streak = 0


demander_regle = False
#je defenis ma boucle
while pointVie > 0:

    numero_combat = numero_combat + 1 #le combat augmente chaque fois
    #le combat avec le boss
    if streak %3 == 0 and streak > 0 and demander_regle == False:
        force_adversaire = randint(5,11)
        print("tu tombes contre un boss avec une force de 5-11")



    elif demander_regle == False:
        #un combat avec un adversaire normal
        force_adversaire = randint(1,11)
        print("Vous tombez face à face avec un adversaire de difficulté : %d" %(force_adversaire))
    #le choix pour le combat
    choix = int(input("Que voulez-vous faire ?\n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie"))
    #si le choix est de combattre le monstre
    if choix == 1:
        demander_regle = False
        print("vous combattez le monstre")
        #le rouler des dés
        dé1 = randint(1,6)
        dé2 = randint(1,6)
        dés = dé1 + dé2
        #si tu gagnes le combat
        if dés > force_adversaire:
            print("vous gagnez le combat")
            streak = streak + 1
            print("vous avez maintenant un streak de %d" %(streak))
        #si tu perds le combat
        else:
            streak = 0
            print("vous perdez le combat et vous avez 0 victoires consequtifs")
            pointVie = pointVie - force_adversaire
        print("Force de l’adversaire:%d \npoint de vie de l’usager:%d \ncombat:%d \nlancer des dés:%d" %(force_adversaire, pointVie, numero_combat, dés))

        print("----------")
    #si le choix est fuir
    elif choix == 2:
        demander_regle = False
        pointVie = pointVie - 1
        print("vous fuyez et,vous perdez un point de vie \npoint de vie de l'usager:%d" %(pointVie))

        print("----------")
    #si le choix est d'afficher les regles
    elif choix == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

        print("----------")
        demander_regle = True
    #si le choix est de quitter le jeu
    else:
        print("Merci et au revoir...")
        quit()
#si tu meurs
print("tu es mort")