'''
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större.
Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal.
Exempel: card = random.randint(1, 13)

Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal)
Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.
'''
from exercise_functions import print_exercise_divider
import random
from time import sleep

def deal_a_card(min_card_value, max_card_value):
    return random.randint(min_card_value, max_card_value)

def first_to_21_v1():
    index = 2
    result = 1
    while result < 21:
        result = result + index
        index += 1
        print(result)


def first_to_21_v2():

    total = 0

    while total < 21:
        next_card = deal_a_card(1, 13)
        total += next_card
        print(total)

def first_to_21_v3():

    continue_game = "y"
    min_card_value = 1
    max_card_value = 11

    while continue_game.lower() == "y":

        print("\n♥️♠️♦️♣️♥️♠️♦️♣️♥️♠️♦️♣️\n")
        card_1 = deal_a_card(min_card_value, max_card_value)
        card_2 = deal_a_card(min_card_value, max_card_value)
        player_total = card_1 + card_2

        dealer_card_1 = deal_a_card(min_card_value, max_card_value)
        dealer_card_2 = deal_a_card(min_card_value, max_card_value)
        dealer_total = dealer_card_1 + dealer_card_2

        while player_total <= 21:
            print(f"Your current total is {player_total}")
            print(f"Dealer's first card is {dealer_card_1}")
            continue_game = input(f"\nDo you want to stick or twist? (s/t): ")

            if continue_game.lower() == "s":
                break
            elif continue_game.lower() == "t":
                next_card = deal_a_card(min_card_value, max_card_value)
                print(f"\nYou pulled {next_card}\n")
                player_total += next_card


        print(f"Your total is  : {player_total}")
        print(f"Dealer total is: {dealer_total}...")
        sleep(2)
        dealer_twist = False
        # Dealer turn
        while dealer_total <= 21:

            dealer_twist = False
            if dealer_total < 9:
                dealer_twist = True
            elif dealer_total < 15:
                dealer_twist = random.choice([True,True,True,False])
            elif dealer_total < 19:
                dealer_twist = random.choice([True,False,False,False])

            if dealer_twist:
                print("Dealer decided to twist...")
                next_card = deal_a_card(min_card_value, max_card_value)
                print(f"They pulled a {next_card}")
                dealer_total += next_card
                print(f"Their new total is {dealer_total}")
                sleep(3)
            else:
                print("Dealer decided to stick...")
                sleep(2)
                break

        if player_total > 21:
            print("You're bust! Dealer wins! 💩")
        elif dealer_total > 21:
            print("Dealer is bust! You win! 🎉")
        elif player_total == dealer_total:
            print("The scores are equal... Dealer wins! 💩")
        elif player_total < dealer_total:
            print("Dealer wins! 💩")
        elif player_total > dealer_total:
            print("You win! 🎉")

        continue_game = input(f"\nPlay another round? (y/n): ")




# print_exercise_divider(4, "3-v1")
# first_to_21_v1()
#
# print_exercise_divider(4, "3-v2")
# first_to_21_v2()

print_exercise_divider(4, "3-v3")
first_to_21_v3()

