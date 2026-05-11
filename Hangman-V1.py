import random
import time 
import os
import sys

def clear():
    os.system("cls" if sys.platform=="win32" else "clear")

times = 1
found_letters = []
done = False

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   
print("***Welcome to hangman V1****")
time.sleep(0.5)
word = input("Enter a word for the computer to guess: ").lower()
time.sleep(0.5)
clear()
while done == False:
    selected_letter = random.choice(letters)
    times += 1
    print("Does your word include the letter", selected_letter)
    yn = input("(y/n)").lower()
    if selected_letter in letters:
      letters.remove(selected_letter)

    if yn[0] == "y":
        if selected_letter in word:
            print("hmm ok")
            if selected_letter not in found_letters:
                found_letters.append(selected_letter)
            time.sleep(0.5)
            clear()
              

        else: 
            print("the ai detected that",selected_letter,"is not in the word, you lied")
            time.sleep(0.5)
            clear()
    if yn[0] == "n":
        if selected_letter in word:
            print("The ai detected the letter in the word, you cheated")
            time.sleep(0.7)
            if selected_letter not in found_letters:
                found_letters.append(selected_letter)
            print(selected_letter,"is in the word")
        time.sleep(0.3)
        clear() 
    if all(letter in found_letters for letter in word):
        print("The computer found the word, the word was",word)
        print("the computer got the word in", times, "guesses ")
        break
    print("the computer has found the letters",found_letters,"\n")

        
    
    
