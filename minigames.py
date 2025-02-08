import pendu
import mastermind
import morpion

#Menu principal
def choix_jeu():
    jeu = int(input("A quel jeu souhaitez-vous jouer ? \n1 - Pendu \n2 - Mastermind \n3 - Morpion\n"))
    while jeu != 1 and jeu != 2 and jeu != 3:
        jeu = int(input("Cette option n'est pas proposée, veuillez choisir un chiffre entre 1, 2 et 3\n"))

    if jeu == 1: pendu.pendu()
    elif jeu == 2: mastermind.mastermind(mastermind.menu())
    elif jeu == 3: morpion.morpion()


choix_jeu()