import random

print("How many attempts for the game?")
attempts = int(input())
print("\n" + str(attempts) + " attempts have been chosen. What is the maximum number allowed for the game?")
maxnumber = int(input())

randomnumber = random.randint(0, maxnumber)
numberhint = [0, maxnumber]

print("\nPlease select your first number guess. The number can be any number between 0 and " + str(maxnumber) + ".")

while attempts > 0:
    number = int(input())
    if number == randomnumber:
        print("Congratulations, you guessed the number!")
        break
    elif number < randomnumber:
        attempts -= 1
        print("Sorry, your guess was too low. You now have " + str(attempts) + " attempts left.")
        numberhint[0] = number
    elif number > randomnumber:
        attempts -= 1
        print("Sorry, your guess was high. You now have " + str(attempts) + " attempts left.")
        numberhint[1] = number
    if attempts == 0:
        print('You lose!')
        break
    print(f"Please make another guess. (hint: the number is between {numberhint[0]} and {numberhint[1]}.")
