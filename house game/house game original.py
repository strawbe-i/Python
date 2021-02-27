import math
import tkinter

def getNumber(minimum, maximum):
    while True:
        try:
            x = int(input())
            if x >= minimum and x <= maximum:
                break
            elif x < minimum:
                print("That number is too small. Please try again.")
            elif x > maximum:
                print("That number is too big. Please try again.")
            else:
                print("...")
        except ValueError:
            print("That's not a number. Try again.")
    return x

#House Game
#There are 10 turns
#You'll start with 10 dollars
#Each turn you can buy as many houses as you want at 5 dollars each
#Every turn each house makes you 3 dollars
#The goal is to have as much money as possible at the end of the 10 turns

print("Welcome to the House Game!\nThere are 10 turns\nYou'll start with 10 dollars\nEach turn you can buy as many houses as you want at 5 dollars each\nEvery turn each houses you own makes you 3 dollars\nThe goal is to have as much money as possible at the end of the game")
while True:
    print("Would you like to play with these default rules (Default) or make custom rules (Custom)?")
    while True:
        gameType = input()
        if gameType == "Custom" or gameType == "custom" or gameType == "c":
            print("How many turns? (Minimum 1 Maximum 100 Default 10)")
            turns = getNumber(1,100)
            print("How much starter money? (Minimum 1 Maximum 1,000,000,000 Default 10)")
            money = getNumber(1,1000000000)
            print("How many starter houses? (Minimum 0 Maximum 1,000,000 Default 0)")
            houses = getNumber(0,1000000)
            print("How much will houses cost? (Minimum 0 Maximum 1,000,000,000 Default 5)")
            houseCost = getNumber(0,1000000000)
            print("How much will houses make per turn? (Minimum 0 Maximum 1,000,000,000 Default Default 3)")
            houseRevenue = getNumber(0,1000000000)
            break
        elif gameType == "Default" or gameType == "default" or gameType == "d":
            houseCost = 5
            houseRevenue = 3
            turns = 10
            houses = 0
            money = 10
            break
        else:
            print("Type 'Default' to use the default rules or 'Custom' to set your own.")

    for x in range(1,turns+1):
        newHouses = 0
        print("Turn", x)
        print("You currently have", houses, "houses and", money, "dollars. How many houses will you buy?")
        while True:
            try:
                newHouses = int(input())
                if newHouses*houseCost <= money and newHouses >= 0:
                    break
                elif newHouses*houseCost > money:
                    print("That would cost", newHouses*houseCost, "dollars, but you only have", money, "dollars. Buy less houses or none.")
                elif newHouses < houseCost:
                    print("You can't buy a negative number of houses. Try again.")
                else:
                    print("What? You shouldn't be here, but try again...")
            except ValueError:
                print("That's not a number, try again.")
        houses = houses + newHouses
        money = money - newHouses*houseCost + houses*houseRevenue
    print("You finished with", money, "dollars and", houses, "houses. Good job?")
    print("Would you like to play again? (Y/N)")
    while True:
        again = input()
        if again == "Y" or again == "y":
            break
        elif again == "N" or again == "n":
            break
        else:
            print("Please type 'Y' or 'N'")
    if again == "N" or again == "n":
        break
