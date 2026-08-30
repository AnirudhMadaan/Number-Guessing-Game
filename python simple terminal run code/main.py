import random
number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100")
print ("you will only get 7 attempts")

while True:
    guess = int(input("\nEnter your guess: "))

    attempts = attempts + 1

    if guess == number:
        print("\n🎉 Correct! You guessed the number!")
        print("Total attempts:", attempts)
        break

    elif guess < number:
        print("📉 Too low! Try a higher number.")
    elif attempts == 7:
        print("out of attempts")
        break    


    else:
        print("📈 Too high! Try a lower number.")