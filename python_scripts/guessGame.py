
import random

random_num = random.randint(1,10) 

guess = None

while True:
    print("*" * 25)
    print("\n" * 2)
    guess = input("Pick a number from 1 to 10:  ")
    print("\n" * 2) 
    guess = int(guess)


    if guess < random_num:
        print("Too Low\n")
        print("\n" * 2)
    elif guess > random_num:
         print("Too High\n")
         print("\n" * 2)
    else:
        print("You Got It!\n")
        print("\n" * 2)
        play_again = input("Do you want to play again? y/n \n").lower
        if play_again == 'y':
            guess = None
            random_num = random.randint(1,10)            
        else:
            break
print("\n" * 2)            
print("*" * 25)

