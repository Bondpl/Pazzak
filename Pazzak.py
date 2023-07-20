import random

DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] * 4
EXTRA_PLAYER = [-1, 2, 3, 5, 6]
EXTRA_ENEMY = [-2, 1, 3, 5, 6]
END = 20
score_player = 0
score_enemy = 0

def choose_card(deck, hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

def choose_extra_card(hand, extra):
    if extra:
        print("Twoje karty:", extra)
        choice = input("Czy chcesz dobrać dodatkową kartę? (t/n): ")
        if choice.lower() == "t":
            print("Wybierz kartę:", extra)
            print("Indeksy kart: 1 2 3 4 5")
            choice = int(input("Którą kartę wybierasz? "))
            while choice > len(extra) or choice <= 0:
                choice = int(input("Niewłaściwy indeks, wybierz poprawny: "))
            extra_card = extra[choice - 1]
            hand.append(extra_card)
            extra.remove(extra_card)
        else:
            return 0

def play_game():
    global score_player, score_enemy

    while score_enemy != 3 and score_player != 3:
        deck = DECK.copy()
        hand_player = []
        hand_enemy = []
        pas = False

        while not pas and sum(hand_player) < END and sum(hand_enemy) < END:
            # Player's turn
            print("+-------------------------------------------+")
            print("|  Twoje karty:       ", hand_player, "\t|")
            print("|  Łączna wartość:   ", sum(hand_player), "\t|")
            print("|  Twój wynik:       ", score_player, "\t\t|")
            print("+-------------------------------------------+\n")
            # Enemy's turn
            print("+-------------------------------------------+")
            print("|  Karty przeciwnika: ", hand_enemy, "\t|")
            print("|  Łączna wartość:   ", sum(hand_enemy), "\t|")
            print("|  Wynik przeciwnika: ", score_enemy, "\t\t|")
            print("+-------------------------------------------+")

            choice = input("1 - dobierz\t2 - spasuj\n")

            if choice == "1":
                choose_card(deck, hand_player)
                print("+-------------------------------------------+")
                print("|  Twoje karty:       ", hand_player, "\t|")
                print("|  Łączna wartość:   ", sum(hand_player), "\t|")
                print("|  Twój wynik:       ", score_player, "\t\t|")
                print("+-------------------------------------------+\n")
                choose_extra_card(hand_player, EXTRA_PLAYER)
                if sum(hand_enemy) < END:
                    choose_card(deck, hand_enemy)
                elif sum(hand_enemy) == END:
                    print("Przeciwnik spasował")
            elif choice == "2":
                while sum(hand_enemy) < END and sum(hand_enemy) < sum(hand_player):
                    choose_card(deck, hand_enemy)
                pas = True
            else:
                choice = input("1 - dobierz\t2 - spasuj\n")

            # Determine the winner
            if sum(hand_player) == END and sum(hand_enemy) != END:
                print("WYGRAŁEŚ!!!")
                score_player += 1
            elif pas and sum(hand_player) < END and sum(hand_player) > sum(hand_enemy) and sum(hand_enemy) < END:
                print("WYGRAŁEŚ!!!")
                score_player += 1
            elif sum(hand_enemy) > END and sum(hand_player) <= END:
                print("WYGRAŁEŚ!!!")
                score_player += 1
            elif sum(hand_enemy) == END and sum(hand_player) != END:
                print("PRZEGRAŁEŚ!!!")
                score_enemy += 1
            elif sum(hand_player) > END and sum(hand_enemy) <= END:
                print("PRZEGRAŁEŚ!!!")
                score_enemy += 1
            elif sum(hand_player) == sum(hand_enemy) and sum(hand_player) <= END:
                print("REMIS!!!")
            elif sum(hand_player) > END and sum(hand_enemy) > END:
                print("REMIS!!!")

            # Player's turn summary
            print("+-------------------------------------------+")
            print("|  Twoje karty:       ", hand_player, "\t|")
            print("|  Łączna wartość:   ", sum(hand_player), "\t|")
            print("|  Twój wynik:       ", score_player, "\t\t|")
            print("+-------------------------------------------+\n")
            # Enemy's turn summary
            print("+-------------------------------------------+")
            print("|  Karty przeciwnika: ", hand_enemy, "\t|")
            print("|  Łączna wartość:   ", sum(hand_enemy), "\t|")
            print("|  Wynik przeciwnika: ", score_enemy, "\t\t|")
            print("+-------------------------------------------+")

        if score_enemy == 3:
            print("PRZEGRAŁEŚ!!!")
        elif score_player == 3:
            print("WYGRAŁEŚ!!!")

play_game()
