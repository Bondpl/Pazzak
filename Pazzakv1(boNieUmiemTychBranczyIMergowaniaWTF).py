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


def choose_card_player():
    if EXTRA_player:
        choise = input("do you want do pick extra card? (y/n): ")
        if choise.lower() == "y":
            print("choose the card\t", EXTRA_player)
            print("index of cards\t  1  2  3  4  5")
            choise = int(input("\nwhat card do you choose "))

            while choise > len(EXTRA_player) or choise <= 0:
                choise = int(input("wrong index, choose correct one"))

            EXTRA_card = EXTRA_player[choise - 1]
            DECK_player.append(EXTRA_card)
            EXTRA_player.remove(EXTRA_card)

    card_player = random.choice(DECK)
    DECK_player.append(card_player)
    DECK.remove(card_player)


def choose_card_enemy():
    card_enemy = random.choice(DECK)
    DECK_enemy.append(card_enemy)
    DECK.remove(card_enemy)


while not pas and sum(DECK_player) < END and sum(DECK_enemy) < END:
    print(
        "wybrane karty :",
        DECK_player,
        "\t  wartosc kart:",
        sum(DECK_player),
        "\tscore :",
        score_player,
    )
    print(
        "\n\nkarty krupiera :",
        DECK_enemy,
        "\twartosc kart:",
        sum(DECK_enemy),
        "\tscore :",
        score_enemy,
    )

    choise = input("1 - hit\t2 - pass\n")

    if choise == "1":
        choose_card_player()
        if sum(DECK_enemy) < END:
            choose_card_enemy()

    elif choise == "2":
        while sum(DECK_enemy) < END and sum(DECK_enemy) < sum(DECK_player):
            choose_card_enemy()
            if sum(DECK_enemy) == END:
                score_enemy = score_enemy + 1
                break
            elif sum(DECK_enemy) > END:
                score_enemy = score_enemy - 1
        pas = True
    else:
        choise = input("1 - hit\t2 - pass\n")

    if sum(DECK_player) == END:
        score_player += 1
    elif sum(DECK_enemy) == END:
        score_enemy += 1

    if sum(DECK_player) > END:
        print("PRZEGRALES!!!")
        score_player = score_player - 1
    elif sum(DECK_player) == END and sum(DECK_enemy) > END:
        print("WYGRALES!!!")
        score_player = score_player + 1
    elif sum(DECK_player) == END and sum(DECK_enemy) == END:
        print("REMIS!!!")

    # if sum(DECK_enemy) > END:
    #     print("PRZEGRALES!!!")
    #     score_enemy = score_enemy - 1
    # elif sum(DECK_enemy) == END:
    #     print("WYGRALES!!!")
    #     score_enemy = score_enemy + 1
