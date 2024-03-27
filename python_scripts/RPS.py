

print("...rock...")
print("...paper...")
print("...scissors...")


player1 = input("(enter Player 1's choice):").lower()
print("*****    NO CHEATING   **** \n\n" * 20)
print("...rock...")
print("...paper...")
print("...scissors...")

player2 = input("(enter Player 2's choice):").lower()
if player1 and player2:
    if player1 == player2:
         print("It' a tie")
    elif player1 == "rock":
        if player2 == "scissors":
             print("Player 1 win!!!")
        elif player2 == "paper":
             print("Player 2 win!!!")

    elif player1 == "paper":
        if player2 == "rock":
             print("Player 1 win!!")
        elif player2 == "scissors":
             print("Player 2 win!!")
    elif player1 == "scissors":
        if player2 == "paper":
             print("Player 1 win!!")
        elif player2 == "rock":
             print("Player 2 win!!")
    
    
else:
    print("Something went wrong...")
