"""
POKERHAND
När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas.
Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
poker_hand(cards)
"Du fick ett par med valören: 5"

1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
Exempel på ett kort: ["hjärter", 12]

2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

Fortsätt att lägga till fler kontroller till funktionen.
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
pretty_print_card(["hjärter", 5]) → "hjärter fem"

Lista med pokerhänder.
Ett par (två lika kort)
Två par
Tretal (tre lika)
Straight (5 kort i följd, t.ex. 7-8-9-10-11)
Flush / färg (alla kort har samma färg)
Hus (par och tretal med olika valörer)
Fyrtal
Straight flush (5 kort i följd, med samma färg)
Femtal

"""

import random

from exercise_functions import print_exercise_divider

CARD_SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
ORDERED_CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

pair_count = 0
pair = False
pairs = ""
three_of_a_kind = False
three_of_a_kind_cards = ""
four_of_a_kind = False
four_of_a_kind_cards = ""
five_of_a_kind = False
five_of_a_kind_cards = ""

def reset_globals():
    global pair_count
    global pair
    global pairs
    global three_of_a_kind
    global three_of_a_kind_cards
    global four_of_a_kind
    global four_of_a_kind_cards
    global five_of_a_kind
    global five_of_a_kind_cards
    pair_count = 0
    pair = False
    pairs = ""
    three_of_a_kind = False
    three_of_a_kind_cards = ""
    four_of_a_kind = False
    four_of_a_kind_cards = ""
    five_of_a_kind = False
    five_of_a_kind_cards = ""

def reset_card_deck():
    # Rebuild the card deck
    fresh_card_deck = []
    for suit in CARD_SUITS:

        for value in ORDERED_CARD_VALUES:
            fresh_card_deck.append([suit,value])

    return fresh_card_deck

def deal_card(play_deck):
    # Randomly select a card from the deck
    # then remove it from the deck so it can't be selected again
    new_card = random.choice(play_deck)
    play_deck.remove(new_card)
    return new_card

def deal_hand(play_deck):
    new_hand = []
    counter = 0
    while counter < 5:
        new_hand.append(deal_card(play_deck))
        counter += 1
    return new_hand

def sort_hand(player_hand):

    player_hand.sort(key=lambda card: (ORDERED_CARD_VALUES.index(card[1]), card[0]))
    return player_hand


def pretty_print_card(card):
    return f"{card[1]} of {card[0]}"

def pretty_print_hand(hand):

    print("\nPlayers hand:")
    print("-"*20)
    for card in hand:
        print(pretty_print_card(card))

def get_card_value(card):
    return card[-1]

def get_card_suit(card):
    return card[0]

def get_value_counts(player_hand):

    value_counts = {}
    for card in player_hand:

        card_value = get_card_value(card)
        if card_value in value_counts:
            value_counts[card_value] += 1
        else:
            value_counts[card_value] = 1

    return value_counts

def get_suit_counts(player_hand):

    suit_counts = {}
    for card in player_hand:

        card_suit = get_card_suit(card)
        if card_suit in suit_counts:
            suit_counts[card_suit] += 1
        else:
            suit_counts[card_suit] = 1

    return suit_counts

def check_multiples(ordered_hand):

    global pair_count
    global pair
    global pairs
    global three_of_a_kind
    global three_of_a_kind_cards
    global four_of_a_kind
    global four_of_a_kind_cards
    global five_of_a_kind
    global five_of_a_kind_cards

    value_counts = get_value_counts(ordered_hand)

    for key, value in value_counts.items():

        if value == 2:
            pair_count += 1
            pair = True
            pairs += f"Pair of {key}s "
        elif value == 3:
            three_of_a_kind = True
            three_of_a_kind_cards = f"Three {key}s"
        elif value == 4:
            four_of_a_kind = True
            four_of_a_kind_cards = f"Four {key}s"
        elif value == 5:
            five_of_a_kind = True
            five_of_a_kind_cards = f"Five {key}s"

def check_full_house(player_hand):
    suit_counts = get_suit_counts(player_hand)

    pair_found = False
    triple_found = False

    for key, value in suit_counts.items():
        if value == 2:
            pair_found = True
        elif value == 3:
            triple_found = True

    return pair_found and triple_found

def check_straight(ordered_hand):
    # 5 cards sequential, any suit
    # Convert our card values into their index ranks so they can be compared
    ranks = [ORDERED_CARD_VALUES.index(card[1]) for card in ordered_hand]

    # Check if each rank is exactly 1 higher than the previous one
    for i in range(len(ranks) - 1):
        if ranks[i + 1] != ranks[i] + 1:
            return False

    return True

def check_flush(ordered_hand):
    # 5 cards same suit, not sequential
    # Extract just the suits: hand[i][0]
    suits = [card[0] for card in ordered_hand]
    # A set of unique suits should be len 1
    return len(set(suits)) == 1

def check_straight_flush(is_straight, is_flush):
    # 5 cards same suit, sequential
    if is_straight and is_flush:
        return True
    else:
        return False

def check_royal_flush(is_straight_flush, ordered_hand):
    # Ace, King, Queen, Jack, 10 same suit
    # if we know we have a straight flush and the last card
    # of the ordered hand is an Ace, then we have a Royal Flush
    return is_straight_flush and ordered_hand[-1][1] == "Ace"


def analyse_hand(ordered_hand):

    global pair_count
    global pair
    global pairs
    global three_of_a_kind
    global three_of_a_kind_cards
    global four_of_a_kind
    global four_of_a_kind_cards
    global five_of_a_kind
    global five_of_a_kind_cards
    straight = False
    flush = False
    straight_flush = False
    royal_flush = False
    full_house = False
    high_card = False

    value_counts = get_value_counts(ordered_hand)
    check_multiples(ordered_hand)
    straight = check_straight(ordered_hand)
    flush = check_flush(ordered_hand)
    straight_flush = check_straight_flush(straight, flush)
    royal_flush = check_royal_flush(straight_flush, ordered_hand)

    if not pair \
            and not three_of_a_kind \
            and not four_of_a_kind \
            and not five_of_a_kind \
            and not full_house \
            and not straight \
            and not flush:
        high_card = True

    print("\nAnalysis of players hand:")
    print("-"*30)
    print(f"High card             : {high_card} {f' - ({pretty_print_card(ordered_hand[-1])})' if high_card else ''}")
    print(f"Two of a kind found   : {pair} {f' - ({pairs})' if pair else ''}")
    print(f"Three of a kind found : {three_of_a_kind} {f' - ({three_of_a_kind_cards})' if three_of_a_kind else ''}")
    print(f"Four of a kind found  : {four_of_a_kind} {f' - ({four_of_a_kind_cards})' if four_of_a_kind else ''}")
    print(f"Five of a kind found  : {five_of_a_kind} {f' - ({five_of_a_kind_cards})' if five_of_a_kind else ''}")
    print(f"Full House            : {full_house}")
    print(f"Straight              : {straight}")
    print(f"Flush                 : {flush}")
    print(f"Straight flush        : {straight_flush}")
    print(f"Royal Flush           : {royal_flush}")


def play(test_hand=None):
    # Plays a round. Accepts an optional custom_hand for testing
    reset_globals()
    print("\n\n♥️♠️♦️♣️ POKERHAND ♣️️♦️️♠️♥️️")
    if test_hand is not None:
        print("\n--- Testing Mode: Using predefined hand ---")
        hand = test_hand
    else:
        print("\nDealing new hand...")
        card_deck = reset_card_deck()
        hand = deal_hand(card_deck)

    sorted_hand = sort_hand(hand)
    pretty_print_hand(sorted_hand)
    analyse_hand(sorted_hand)


def run_tests():

    print_exercise_divider(4,"Pokerhand - Testing High Card")
    hand = [['Diamonds', '2'], ['Diamonds', '4'], ['Hearts', '6'], ['Clubs', '8'], ['Spades', 'Ace']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Pair")
    hand = [['Diamonds', '2'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '6'], ['Spades', '7']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing 2 Pairs")
    hand = [['Diamonds', '2'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '6'], ['Spades', '6']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Three of a kind")
    hand = [['Diamonds', '3'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '6'], ['Spades', '7']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Four of a kind")
    hand = [['Diamonds', '3'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '3'], ['Spades', '7']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Five of a kind")
    hand = [['Diamonds', '3'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '3'], ['Spades', '3']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Full House")
    hand = [['Diamonds', '3'], ['Diamonds', '3'], ['Hearts', '3'], ['Clubs', '6'], ['Spades', '6']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Straight")
    hand = [['Diamonds', '3'], ['Diamonds', '4'], ['Hearts', '7'], ['Clubs', '6'], ['Spades', '5']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Flush")
    hand = [['Diamonds', '3'], ['Diamonds', '3'], ['Diamonds', '3'], ['Diamonds', '6'], ['Diamonds', '6']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Straight Flush")
    hand = [['Diamonds', '3'], ['Diamonds', '7'], ['Diamonds', '5'], ['Diamonds', '6'], ['Diamonds', '4']]
    play(hand)

    print_exercise_divider(4,"Pokerhand - Testing Royal Flush")
    hand = [['Diamonds', 'Queen'], ['Diamonds', '10'], ['Diamonds', 'Jack'], ['Diamonds', 'King'], ['Diamonds', 'Ace']]
    play(hand)


choice = input("Press T to run tests or Enter to play a hand: ")
if choice.upper() == "T":
    run_tests()
else:
    play()

