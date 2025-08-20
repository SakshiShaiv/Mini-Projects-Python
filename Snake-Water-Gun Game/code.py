import random

print("Welcome to the snake-water-gun game")
print("enter 1 for snake, enter 2 for water & enter 3 for gun.")
print("let's begin the game. Good Luck!!")

choices={1:"snake",2:"water",3:"gun"}
computerChoice=random.randint(1,3)
userChoice=int(input("Enter your choice:- "))

if userChoice>3 or userChoice<0:
    print("enter a valid choice!!")
else:
    if userChoice==computerChoice:
        print("It's a Draw!!")
        print(f"both have {choices[userChoice]}")
    else:
        if userChoice==1 and computerChoice==2:
            print("You won the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")
        elif userChoice==2 and computerChoice==1:
            print("You lost the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")
        elif userChoice==2 and computerChoice==3:
            print("You win the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")
        elif userChoice==3 and computerChoice==2:
            print("You lost the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")
        elif userChoice==3 and computerChoice==1:
            print("You win the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")
        else:
            print("You lost the game!!")
            print(f"you chose {choices[userChoice]} and computer chose {choices[computerChoice]}")



