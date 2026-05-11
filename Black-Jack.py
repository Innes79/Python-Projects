import os 
import sys
import random

def hit(current_hand):
    card = random.randint(1, 13)
    if card >= 11:
        return 10
    elif card == 1:
        if current_hand <= 10:
            return 11
        else:
            return 1
    else:
        return card

def show_results(hand, ComHand, multiplier):
    print("\n" + "="*30)
    print(f"YOUR FINAL SCORE: {hand}")
    print(f"DEALER FINAL SCORE: {ComHand}")
    print("="*30)
    
    if hand > 21:
        print(f"RESULT: You busted! Type -{20 * multiplier}$ into your note.")
    elif ComHand > 21:
        print(f"RESULT: Dealer busted! Add +{50 * multiplier}$ to your note.")
    elif hand > ComHand:
        print(f"RESULT: You win! Add +{50 * multiplier}$ to your note.")
    elif hand < ComHand:
        print(f"RESULT: Dealer wins. Type -{20 * multiplier}$ into your note.")
    else:
        print(f"RESULT: It's a tie (Push). Add +{5 * multiplier}$ to your note.")
    print("="*30)

multiplier = 1
com_hand = 0
player_hand = 0

print("Welcome to Blackjack!")
print("Instructions: Get close to 21 without going over.")
print("Hit (h), Stand (s), or Double Down (d).")
input("\nPress Enter to start...")

os.system("cls" if sys.platform=="win32" else "clear")

player_hand = hit(player_hand)
com_hand = hit(com_hand)

print(f"Your starting score is: {player_hand}")
print(f"The dealer is showing one card.")

while player_hand < 21:
    option = input("\nWhat would you like to do? (h/s/d): ").lower()
    
    if option == "h":
        new_card = hit(player_hand)
        player_hand += new_card
        print(f"You drew a {new_card}. Your score is now: {player_hand}")
        if player_hand > 21:
            print("Bust!")
            break
            
    elif option == "s":
        print("You chose to stand.")
        break
        
    elif option == "d":
        multiplier = 2
        new_card = hit(player_hand)
        player_hand += new_card
        print(f"Double Down! You drew a {new_card}. Final score: {player_hand}")
        break
        
    else:
        print("Invalid input. Please enter h, s, or d.")

if player_hand <= 21:
    print("\nDealer's turn...")
    while com_hand < 17:
        card = hit(com_hand)
        com_hand += card
        print(f"Dealer draws a card... Dealer score: {com_hand}")

show_results(player_hand, com_hand, multiplier)
