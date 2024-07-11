logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
from replit import clear
import random
end_of_game = False
def deal_card():
    global deal_card
    global comapre
    global calculate_score
    global player_cards
    global dealer_cards
    global cards
    global dealer_card1
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    player_cards.extend([player_card1, player_card2])
    dealer_cards = []
    dealer_card1 = random.choice(cards)
    dealer_cards.append(dealer_card1)


def calculate_score():
    global dealer_card1
    global deal_card
    global comapre
    global calculate_score
    global player_cards
    global dealer_cards
    global player_score
    global dealer_score
    player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, your current score {player_score}.")
    print(f"Dealer's card: {dealer_card1}.")
    dealer_score = sum(dealer_cards)
    if player_cards == [11, 10] or player_cards == [10, 11]:
        player_score = 0
        print("You got the Blackjack! You win!")
        if input("Do you want to play again? Type 'yes' or 'no':\n ") == "yes":
            print(logo)
            deal_card()
            calculate_score()
            compare()
        else:
            end_of_game = True
            exit()
    else:
        if player_score >= 21 or dealer_score >= 21 and dealer_score > 17:
            compare()
        else:
            if input("Do you want to draw another card? Type 'y' or 'n':\n") == "y":
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, your current score: {player_score}.")
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        calculate_score()
                        compare()
            else:
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        compare()
                compare()
    if player_score > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        print(f" Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n You went over 21, You lose.")
        if input("Do you want to play again? Type 'yes' or 'no':\n") == "yes":
            print(logo)
            deal_card()
            calculate_score()
        else:
            end_of_game = True
            exit()
    else:
        if player_score >= 21 or dealer_score >= 21 and dealer_score > 17:
            compare()
        else:
            if input("Do you want to draw another card? Type 'y' or 'n':\n") == "y":
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, your current score: {player_score}.")
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        calculate_score()
                        compare()
            else:
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        compare()
                compare()
    if dealer_cards == [11, 10] or dealer_cards == [10, 11]:
        dealer_score = 0
        print("Dealer got the Blackjack! Dealer wins!")
        if input("Do you want to play again? Type 'yes' or 'no': ") == "yes":
            print(logo)
            deal_card()
            calculate_score()
        else:
            end_of_game = True
            exit()
    else:
        if player_score >= 21 or dealer_score >= 21 and dealer_score > 17:
            compare()
        else:
            if input("Do you want to draw another card? Type 'y' or 'n':\n") == "y":
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, your current score: {player_score}.")
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        calculate_score()
                        compare()
            else:
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        compare()
                compare()
    if dealer_score > 21 and 11 in dealer_cards:
        dealer_cards.remove(11)
        dealer_cards.append(1)
        compare()
    else:
        if player_score >= 21 or dealer_score >= 21 and dealer_score > 17:
            compare()
        else:
            if input("Do you want to draw another card? Type 'y' or 'n':\n") == "y":
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, your current score: {player_score}.")
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        calculate_score()
                        compare()
            else:
                while dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score < 17:
                      dealer_cards.append(random.choice(cards))
                      dealer_score = sum(dealer_cards)
                    else:
                        compare()
                compare()


def compare():
    global deal_card
    global comapre
    global calculate_score
    global player_score
    global dealer_score
    if player_score == dealer_score:
        print(
            f"Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n It's a draw!")
    elif dealer_score == 0:
        print("Dealer got the blackjack! Dealer wins!")
    elif player_score == 0:
        print("You got the BlackJack! You win!")
    elif player_score > 21:
        print(
            f"Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n You went over 21. You lose.")
    elif dealer_score > 21 and player_score <= 21:
        print(
            f"Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n Dealer went over 21. You win!")
    elif dealer_score < 21 and player_score < 21 and dealer_score > player_score:
        print(
            f"Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n Dealer has a higher score. Dealer wins!")
    elif dealer_score < 21 and player_score < 21 and dealer_score < player_score:
        print(
            f"Your final hand: {player_cards}, your final_score: {player_score}.\n Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}.\n You have a higher score. You win!")
    else:
        end_of_game = True
    if input("Do you want to play again? Type 'yes' or 'no':\n") == "yes":
      clear()
      print(logo)
      deal_card()
      calculate_score()
    else:
      end_of_game = True
      exit()


if input("Do you want to play Blackjack? Type 'yes' or 'no':\n") == "yes":
    deal_card()
    calculate_score()
else:
    end_of_game = True
    exit()

while not end_of_game:
    if input("Do you want to draw another card? Type 'y' or 'n':\n") == "y":
        player_cards.append(random.choice(cards))
        player_score = sum(player_cards)
        print(f"Your cards: {player_cards}, your current score: {player_score}.")
        while dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
            if dealer_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
            else:
                calculate_score()
                compare()
    else:
        while dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
            if dealer_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
            else:
                compare()
        compare()


