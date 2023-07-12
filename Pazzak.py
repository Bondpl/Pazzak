import random
import os

DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] * 4
DECK_player = []
DECK_enemy = []
EXTRA_player = [-1, 2, 3, 5, 6]
EXTRA_enemy = [-2, 1, 3, 5, 6]
END = 20
pas = False
score_player = 0
score_enemy = 0

def choose_card_player(DECK, DECK_player):
    card_player = random.choice(DECK)
    DECK_player.append(card_player)
    DECK.remove(card_player)

def choose_extra_card(DECK, DECK_player, EXTRA_player):
    if EXTRA_player:
        print("Twoje karty:", EXTRA_player)
        choice = input("Czy chcesz dobrać dodatkową kartę? (t/n): ")
        if choice.lower() == "t":
            print("Wybierz kartę:", EXTRA_player)
            print("Indeksy kart: 1 2 3 4 5")
            choice = int(input("Którą kartę wybierasz? "))
            while choice > len(EXTRA_player) or choice <= 0:
                choice = int(input("Niewłaściwy indeks, wybierz poprawny: "))
            EXTRA_card = EXTRA_player[choice - 1]
            DECK_player.append(EXTRA_card)
            EXTRA_player.remove(EXTRA_card)
        else:
            return 0

def choose_card_enemy(DECK, DECK_enemy):
    card_enemy = random.choice(DECK)
    DECK_enemy.append(card_enemy)
    DECK.remove(card_enemy)

while score_enemy != 3 and score_player != 3:
    DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] * 4
    DECK_player = []
    DECK_enemy = []
    pas = False

    while not pas and sum(DECK_player) < END and sum(DECK_enemy) < END:
        # TAB OF PLAYER
        print("+-------------------------------------------+")
        print("|  Twoje karty:       ", DECK_player, "\t|")
        print("|  Łączna wartość:   ", sum(DECK_player), "\t|")
        print("|  Twój wynik:       ", score_player, "\t\t|")
        print("+-------------------------------------------+\n")
        # TAB OF ENEMY
        print("+-------------------------------------------+")
        print("|  Karty przeciwnika: ", DECK_enemy, "\t|")
        print("|  Łączna wartość:   ", sum(DECK_enemy), "\t|")
        print("|  Wynik przeciwnika: ", score_enemy, "\t\t|")
        print("+-------------------------------------------+")

        choice = input("1 - dobierz\t2 - spasuj\n")

        if choice == "1":
            choose_card_player(DECK, DECK_player)
            print("+-------------------------------------------+")
            print("|  Twoje karty:       ", DECK_player, "\t|")
            print("|  Łączna wartość:   ", sum(DECK_player), "\t|")
            print("|  Twój wynik:       ", score_player, "\t\t|")
            print("+-------------------------------------------+\n")
            choose_extra_card(DECK, DECK_player, EXTRA_player)
            if sum(DECK_enemy) < END:
                choose_card_enemy(DECK, DECK_enemy)
            elif sum(DECK_enemy) == END:
                print("Przeciwnik spasował")

        elif choice == "2":
            while sum(DECK_enemy) < END and sum(DECK_enemy) < sum(DECK_player):
                choose_card_enemy(DECK, DECK_enemy)
            pas = True
        else:
            choice = input("1 - dobierz\t2 - spasuj\n")

        # RULES FOR SCORES TO PLAYER
        if sum(DECK_player) == END and sum(DECK_enemy) != END:
            print("WYGRAŁEŚ!!!")
            score_player += 1

        elif pas and sum(DECK_player) == END and sum(DECK_enemy) != END:
            print("WYGRAŁEŚ!!!")
            score_player += 1

        elif pas and sum(DECK_player) < END and sum(DECK_player) > sum(DECK_enemy) and sum(DECK_enemy) < END:
            print("WYGRAŁEŚ!!!")
            score_player += 1

        elif sum(DECK_enemy) > END and sum(DECK_player) <= END:
            print("WYGRAŁEŚ!!!")
            score_player += 1
        # RULES FOR SCORES TO ENEMY
        elif sum(DECK_enemy) == END and sum(DECK_player) != END:
            print("PRZEGRAŁEŚ!!!")
            score_enemy += 1 

        elif sum(DECK_player) > END and sum(DECK_enemy) <= END:
             print("PRZEGRAŁEŚ!!!")
             score_enemy += 1 

        # DRAW
        elif sum(DECK_player) == sum(DECK_enemy) and sum(DECK_player) <= END:
            print("REMIS!!!")
        elif sum(DECK_player) > END and sum(DECK_enemy) > END:
            print("REMIS!!!")
        
        # TAB OF PLAYER
        print("+-------------------------------------------+")
        print("|  Twoje karty:       ", DECK_player, "\t|")
        print("|  Łączna wartość:   ", sum(DECK_player), "\t|")
        print("|  Twój wynik:       ", score_player, "\t\t|")
        print("+-------------------------------------------+\n")
        # TAB OF ENEMY
        print("+-------------------------------------------+")
        print("|  Karty przeciwnika: ", DECK_enemy, "\t|")
        print("|  Łączna wartość:   ", sum(DECK_enemy), "\t|")
        print("|  Wynik przeciwnika: ", score_enemy, "\t\t|")
        print("+-------------------------------------------+")

    if score_enemy == 3:
        print("PRZEGRAŁEŚ!!!")
    elif score_player == 3:
        print("WYGRAŁEŚ!!!")
