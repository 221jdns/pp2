import random
def guessGame():
    guessnumber=random.randint(1,20)
    tries=0
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20")
    while True:
        print("Take a guess.")
        num=int(input())
        t+=1
        if(num<guessnumber):
            print("Your guess is too low.")
        elif(num>guessnumber):
            print("You guess is too big")
        else:
            print(f"Good job, {name}! You guessed my number in {t} guesses!")
            break