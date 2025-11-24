import time
import random


print("Loading Hangman Game", end="")
for i in range(3):
    print(".", end="")
    time.sleep(0.5)
print("\n")

name = input("May I know your name? ")
print("Hello,", name, "- Hangman fun starts now!")
time.sleep(1)

print("\nRead before you start:")
print("Choose one letter for each guess")
print("You get 5 attempts")
print("Already used letters won't be counted")
time.sleep(2)

print("\nTake a guess.\n")
time.sleep(0.5)

words = ['apple','mango','banana','orange','kiwi','strawberry']
word = random.choice(words)

guesses = ''
wrong = []            
turns = 5

while turns > 0:         
    failed = 0             
    
    
    print("\nWord: ", end="")
    for char in word:      
        if char in guesses:    
            print(char, end="")    
        else:
            print("_", end="")     
            failed += 1    

    
    if failed == 0:        
        print("\n\n You did it!")
        print("You guessed the word:", word)
        break

    print("\nWrong guesses:", wrong)
    print("Attempts left:", turns)

    guess = input("\nPick a letter: ").lower()
    
    
    if guess in guesses or guess in wrong:
        print("\nYou tried that one before. Choose again!")
        continue

    guesses += guess

    if guess not in word:  
        turns -= 1        
        wrong.append(guess)
        print("\nTry again!")    
        print("Keep going...", turns, "guesses to go") 

        if turns == 2:
            print("Here's a clue : it begins with", word[0])

        if turns == 0:           
            print("\nYou're out of turns")
            print("It was:", word)

print("\nHope you had fun,", name + "!")