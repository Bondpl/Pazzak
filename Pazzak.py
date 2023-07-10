import random
import os


DECK = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
] * 4

DECK_player = []
DECK_enemy = []

EXTRA_player = [-1, 2, 3, 5, 6]
EXTRA_enemy = [
    -2,
    1,
    3,
    5,
    6,
]
END = 20
pas = False

score_player = 0
score_enemy = 0


def choose_card_player(DECK,DECK_player):
    card_player = random.choice(DECK)
    DECK_player.append(card_player)
    DECK.remove(card_player)

def choose_extra_card(DECK,DECK_player,EXTRA_player):
        if EXTRA_player:
            print("twoje karty",EXTRA_player)
            choice = input("do you want do pick extra card? (y/n): ")
            if choice.lower() == "y":
                print("choose the card\t", EXTRA_player)
                print("index of cards\t  1  2  3  4  5")
                choice = int(input("\nwhat card do you choose "))

                while choice > len(EXTRA_player) or choice <= 0:
                    choice = int(input("wrong index, choose correct one"))

                EXTRA_card = EXTRA_player[choice - 1]
                DECK_player.append(EXTRA_card)
                EXTRA_player.remove(EXTRA_card)
            else:
                retrun: 0


def choose_card_enemy(DECK,DECK_enemy):
    card_enemy = random.choice(DECK)
    DECK_enemy.append(card_enemy)
    DECK.remove(card_enemy)

while score_enemy != 3 or score_player != 3:
    DECK = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        10,
        10,
    ] * 4

    DECK_player = []
    DECK_enemy = []
    while not pas or sum(DECK_player) < END and sum(DECK_enemy) < END:

        #TAB OF PLAYER
        print("+-------------------------------------------+")
        print("|  Your cards:       ", DECK_player, "\t|")
        print("|  Total value:      ", sum(DECK_player), "\t|")
        print("|  Your score:       ", score_player, "\t|")
        print("+-------------------------------------------+\n")

        #TAB OF ENEMY
        print("+-------------------------------------------+")
        print("|  Dealer's cards:   ", DECK_enemy, "\t|")
        print("|  Total value:      ", sum(DECK_enemy), "\t|")
        print("|  Dealer's score:   ", score_enemy, "\t|")
        print("+-------------------------------------------+")


        choice = input("1 - hit\t2 - pass\n")

        if choice == "1":
            choose_card_player(DECK,DECK_player)
            print("+-------------------------------------------+")
            print("|  Your cards:       ", DECK_player, "\t|")
            print("|  Total value:      ", sum(DECK_player), "\t|")
            print("|  Your score:       ", score_player, "\t|")
            print("+-------------------------------------------+\n")
            choose_extra_card(DECK,DECK_player,EXTRA_player)
            if sum(DECK_enemy) < END:
                choose_card_enemy(DECK,DECK_enemy)
            elif sum(DECK_enemy) == END:
                print("krupier spasowal")


        elif choice == "2":
            while sum(DECK_enemy) < END and sum(DECK_enemy) < sum(DECK_player):
                choose_card_enemy(DECK, DECK_enemy)
            if sum(DECK_enemy) == END:
                if sum(DECK_enemy) == sum(DECK_player):
                    print("DRAW!!")
                else:
                    print("YOU LOSE!!")
                score_enemy += 1
            else:
                pas = True
        else:
            choice = input("1 - hit\t2 - pass\n")


        if sum(DECK_player) > END:
            print("PRZEGRALES!!!")
            score_enemy += 1
        elif sum(DECK_player) == END and sum(DECK_enemy) > END:
                print("WYGRALES!!!")
                score_player += 1
        elif sum(DECK_player) == END and sum(DECK_enemy) < END:
            print("WYGRALES!!!")
            score_player += 1
        elif sum(DECK_player) < END and sum(DECK_enemy) == END:
            print("PRZEGRALES!!!")
            score_enemy += 1
        elif sum(DECK_player) == END and sum(DECK_enemy) == END:
            print("REMIS!!!")


