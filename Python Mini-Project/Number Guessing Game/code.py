import random
target=random.randint(0,100)
print('"Welcome to The-Number-Guessing-Game!!"')
print("Guess a integer number.Let's see if you guessed a correct digit that lies between 0 to 100 or not? you have only 10 attempts...")
print("Let's begin the game.....")
attempt=0
while True:
    if attempt==10:
        print("no more attempts...you lost the game...Game Over!!")
        break
    num=int(input("Enter a number of your choice:- "))
    if num>100 or num<0:
        print("out of range...think between 0 to 100")
    elif num==target:
        print("congratulations!! You won the Game...Your number is correct")
        break
    elif num<target:
        print("Oh no!! your number is too small...try again with a larger one")
    else:
        print("Oh no!! your number is too large...try again with a smaller one")
    attempt+=1
print("End of Game.")