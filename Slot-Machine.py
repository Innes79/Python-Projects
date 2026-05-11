import time 
import os 
import random 
import sys 


again = True 
icons = ['🍋', '🍊', '🍒', '🍇', '7️⃣', '🎰', '🍐', '🍎', '🌽', '🍍', '🍓', '🥝', '🧸', '🍌', '🍕']
print("welcome\nthis is a slot machine 🎰\nyour aim is to get 3 of the same icon to get a payout\neach play is 10$ but the payouts are good")
input()
cash = int(input("what is the current currency number on your note\nif this is your first game or you have 0 just put 0\ncash = "))
os.system("cls" if sys.platform=="win32" else "clear")

def default():
    os.system("cls" if sys.platform=="win32" else "clear")
    print("    slot machine")
    print(" ___________________")
    print(" |                 | |")
    print(f" |   [0] [0] [0]   | |")
    print(" |                 | |")
    print(" |                 | •")
    print("  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    input("press enter to roll (10$) ")
    os.system("cls" if sys.platform=="win32" else "clear")


def roll(icons):
    a = random.choice(icons)
    b = random.choice(icons)
    c = random.choice(icons)
    os.system("cls" if sys.platform=="win32" else "clear")
    print("    slot machine")
    print(" ___________________")
    print(" |                 | |")
    print(f" | [{a}] [{b}] [{c}] | |")
    print(" |                 | |")
    print(" |                 | •")
    print("  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    if a == b and a == c and b == c:
      print("you rolled all 3 of the same icon")
      return 85
    elif a == b or a == c or b == c:
      print("you rolled a pair")
      return 35

    else:
      return -10


    
default()
i = roll(icons)
cash = cash + i
while again == True:
    print(f"your cash is {cash}$")
    g = input("would you like to go again(y/n/enter) (10$)").lower()

    
    if g == "y" or g == "":
        i = roll(icons)
        cash = cash + i
    else:
        print(f"you ended off with {cash}$\ntype that in the provided note") 
        again = False 
        break
    
