#Första försöket med python 

import random
Done = False
# Initialize deck and player hands
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

random.shuffle(deck)

player_hand = []
computer_hand = []

# Helper function to calculate the value of a hand
def hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            num_aces += 1
            value += 11
        else:
            value += ranks.index(card['rank'])
            value += 2 # to compensate for rank 2 having index 0 etc

    # Handle aces
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value


def print_hand_value(prompt, hand, score):
    print(prompt)
    for card in player_hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total Value: {score}")

# Deal two initial cards to player and computer
player_hand.append(deck.pop())
computer_hand.append(deck.pop())
player_hand.append(deck.pop())
computer_hand.append(deck.pop())

# Main game loop
while not Done:
    player_score = hand_value(player_hand)
    computer_score = hand_value(computer_hand)

    print_hand_value("\nYour Hand:", player_hand, player_score)

    #Computer only shows the first card
    print("\nComputer's Hand:")
    print(f"{computer_hand[0]['rank']} of {computer_hand[0]['suit']}")
    print("Total Value: ???")

    # Check for blackjack
    if player_score == 21:
        print("Congratulations! You have a blackjack. You win!")
        break
    elif computer_score == 21:
        print("Computer has a blackjack. You lose!")
        break

    # Player's turn
    while True:
        action = input("\nDo you want to 'Hit' or 'Stand'? ").lower()
        if action not in ['hit', 'stand']:
            print("Invalid input. Please enter 'Hit' or 'Stand'.")
        else:
            if action == 'hit':
                player_hand.append(deck.pop())
                player_score=hand_value(player_hand)
                print_hand_value("\nYour Hand:", player_hand, player_score)
                if player_score >= 21:
                    break
            else:
                break

    # Computer's turn
    if player_score <= 21:
        while computer_score < 17:
            computer_hand.append(deck.pop())
            computer_score = hand_value(computer_hand)
            print_hand_value("\nComputer Hand:", computer_hand, computer_score)

    # Check for busts
    if player_score > 21:
        print("\nYou busted! Computer wins.")
        break
    elif computer_score > 21:
        print("\nComputer busted! You win.")
        break

    # Compare scores
    print("\nFinal Results:")
    print_hand_value("\nYour Hand:",player_hand, player_score)
    print_hand_value("\nComputer's Hand:", computer_hand, computer_score)

    if player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

    break
