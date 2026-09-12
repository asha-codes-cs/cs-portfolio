#################
# HANGMAN
#################


#DATA-----------------------------------------------------------------------

#import random module 
import random

#set word list-possible word choices
word_list = [
    "whiteboard",
    "curtain",
    "rhombus",
    "anteater",
    "software",
    "python",
    "terrestrial",
    "inadequate",
    "platypus",
    "eloquently"
    ]

#select random word from word list    
word_choice = random.choice(word_list)    



#FUNCTIONS---------------------------------------------------------------------------

#function to display blanks, and guessed letters
blanks = ["_"]*len(word_choice)
guessed_letters = []
def display_state():
    print("\nWord: "+" ".join(blanks))
    if guessed_letters:
        sorted_guesses = sorted(guessed_letters)
        print("\nGuessed Letters: "+" ".join(sorted_guesses))

#create hangman drawing function
def hangman_draw(stage):
    #each stage draws a different picture based on how many chances are left
    if stage == 0:
        #stage 0
        print(" +--------+")
        print(" |        |")
        for i in range(5):
            print("          |")
        print(" ===============")
        
    if stage == 1:    
        #stage 1
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        for i in range(4):
            print("          |")
        print(" ===============")
        
    if stage == 2:    
        #stage 2
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        print(" |        |")
        for i in range(3):
            print("          |")
        print(" ===============")
 
    if stage == 3:        
        #stage 3
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        print(" |\       |")
        for i in range(2):
            print("          |")
        print(" ===============")
        
    if stage == 4:    
        #stage 4
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        print("/|\       |")
        for i in range(2):
            print("          |")
        print(" ===============")
        
    if stage == 5:    
        #stage 5
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        print("/|\       |")
        print("/         |")
        for i in range(2):
            print("          |")
        print(" ===============")

    if stage == 6:        
        #stage 6
        print(" +--------+")
        print(" |        |")
        print(" O        |")
        print("/|\       |")
        print("/ \       |")
        for i in range(2):
            print("          |")
        print(" ===============")

#GAME------------------------------------------------------------------------

#Introduction
print("~~~HANGMAN~~~")

#Rules
rules = input("Do you need the rules? ")
if rules == "yes":
    print("You have 6 chances to guess the hidden word.\n\n\n")
else:
    pass

#set intial amount of chances    
chances = 6

#set initial hangman_draw() stage
stage = 0

#to run the game
while chances > 0:
    
    #draw picture and display blanked out word
    hangman_draw(stage)
    display_state()
    
    #ask user to input a letter
    guess = str(input("\nEnter a letter: "))
    
    #OUTCOMES AFTER A GUESS----------------------------------------------------------
    
    #prevent the same letter from being repeatedly guessed
    if guess in guessed_letters:
        print("\n\n\nThat letter has already been guessed.")
        continue
    guessed_letters = guessed_letters + [guess]
    
    #if the guessed letter is in the word
    if guess in word_choice:
        for i, letter in enumerate(word_choice):
            if letter == guess:
                blanks[i] = guess
        print("\n\n\nGood Guess!")
    
    #if the guessed letter is not in the word
    else:    
        chances = chances - 1
        print("\n\n\nWRONG! You have",chances," chances left.")
        stage = 6 - chances
        
        
    #winning condition    
    if "_" not in blanks:
        hangman_draw(stage)
        display_state()
        print(f"\n\n-----CONGRATULATIONS------")
        print(f"You got the word with {chances} chances left!")
        break

#GAME OVER
else:
    hangman_draw(6)
    print("\n\n----GAME OVER----")
    print(f"The word was {word_choice}. Better luck next time!")
