import random
print("Hello,What is your name?")
name=input()
secretnumber = random.randint(1,20)
print("Well, "+name+", I am thinking of a number between 1 and 20")

#ask the player to guess 6 times
for guessesTaken in range(1,7):
    print("Take a guess..")
    guess=int(input())
    if guess < secretnumber:
        print("Your guess is too low")
    elif guess > secretnumber:
        print("Your guess is too high")
    else:
        break #this condition is correct guess

if guess == secretnumber:
    print("Good job, "+name+" ! You guessed my number in  "+ str(guessesTaken) +"  guesses")
else:
    print("Nope..the number I was thinking of was" +str(guessesTaken)+ "guesses")
