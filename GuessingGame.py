import random
number = random.randint(1, 10)

name = input("Hello, What's your name?")
number_of_guesses = 0
print ("Alrighty! "+name+" I'm thinking of a number between 1 and 10. Guess it.")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Too low. Try guessing a bit higher. Or a lot higher.. your choice.")
    if guess > number:
        print ("Eeeeei chiiiill... too high. Guess again. Try a smaller number this time")
    if guess == number:
        break
if guess == number:
        print ("Correct. Good Job. You guessed the number in " + str(number_of_guesses) + " tries")
else:
        print('Guessing games are clearly not your thing.Anyway the number was ' +str(number)+ " better luck next time.")

