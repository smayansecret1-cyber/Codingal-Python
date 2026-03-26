print("\n")

print("\n")

print("Welcome the the game checker app, enter the game and the following details to find out can you play the game")

print("\n")

game=input("Enter the game's name :) :")

print("\n")

playersn=int(input("Enter the number of players needed to play the game :) :"))

print("\n")

print("We got all the information needed now pls answer the following questions")

print("\n")

weather=input("Is it raining, Y or N? :) :")

print("\n")

players=int(input("Enter the Number of players there are currently :) :"))

if weather.lower()=="y":

    print("\n Sorry, you cant play cause its raining")

elif weather.lower()=="n":

    if players==playersn:

        print("\n")

        print("you can play")

    elif players!=playersn:

        print("\n")

        print("Sorry you cant play, you are short of",playersn-players,"players")

else:

    print("With your information we can't tell can you play or not pls try again")

print("\n")

print("\n")