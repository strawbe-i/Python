from tkinter import *

#House Game
#There are 10 turns
#You'll start with 10 dollars
#Each turn you can buy as many houses as you want at 5 dollars each
#Every turn each house makes you 3 dollars
#The goal is to have as much money as possible at the end of the 10 turns

#Updated gui

#Function to clear window
def clear(root):
    for widget in root.winfo_children():
        widget.destroy()

#Function to destroy a widget
def destroy(widget):
    widget.destroy()

#Function to end game
def end(root):
    root.destroy()

#Starts new game
def createGame(root):

    #start0 is the welcome and rules text, start1 asks how they'd like to play
    clear(root)
    start0 = Label(root, text="Welcome to the House Game!\nThere are 10 turns\nYou'll start with 10 dollars\nEach turn you can buy as many houses as you want at 5 dollars each\nEvery turn each houses you own makes you 3 dollars\nThe goal is to have as much money as possible at the end of the game")
    start0.pack()
    start1 = Label(root, text="Would you like to play with these default rules or make custom rules?", height=2)
    start1.pack()

    #Default and Custom buttons
    default = Button(root, text="Default", width = 7, command=lambda: dcClicked("Default", root))
    default.pack()
    defcusspacer = Label(root, text="")
    defcusspacer.pack()
    custom = Button(root, text="Custom", width = 7, command=lambda: dcClicked("Custom", root))
    custom.pack()

#Clicks on default or custom button
def dcClicked(clicked, root):
    clear(root)
    global houseEntry
    houseEntry = ""

    if clicked == "Default":
        #Sets rules for a default game
        global turns
        global houses
        global money
        global houseRevenue
        global houseCost
        global badTurn
        turns = 10
        money = 10
        houses = 0
        houseCost = 5
        houseRevenue = 3
        badTurn = False

        beginspace0 = Label(root, text="")
        beginspace0.pack()

        #Start Button to go to play()
        begin0 = Button(root, text="Start", width=15, height=5, command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue, houseEntry, badTurn))
        begin0.pack()

        #Makes turnNumber variable globally
        global turnNumber
        turnNumber = 0
    else:
        #Gets rules for custom game from user
        cusinfo = Label(root, text="Custom\nGame")
        cusinfo.grid(row=0, column=3)

        space0 = Label(root, text="    ")
        space0.grid(row=1, column=0)

        #Make an entry and label for every rule in the game, then confirmation button that goes to customconfirmClicked() with necessary variables
        #turns
        turnsE = Entry(root)
        turnsE.insert(0, 10)
        turnsE.grid(row=1, column=1)
        turnsL = Label(root, text="Turns", width = 12)
        turnsL.grid(row=1, column=2)

        space1 = Label(root, text="                  ")
        space1.grid(row=1, column=3)

        #starting money
        startmoneyE = Entry(root)
        startmoneyE.insert(0, 10)
        startmoneyE.grid(row=1, column=4)
        startmoneyL = Label(root, text="Starting Money", width = 15)
        startmoneyL.grid(row=1, column=5)

        space2 = Label(root, text="    ")
        space2.grid(row=2, column=0)

        #house cost
        housecostE = Entry(root)
        housecostE.insert(0, 5)
        housecostE.grid(row=3, column=1)
        housecostL = Label(root, text="House Cost")
        housecostL.grid(row=3, column=2)

        space3 = Label(root, text="                  ")
        space3.grid(row=3, column=3)

        #starting houses
        starthousesE = Entry(root)
        starthousesE.insert(0, 0)
        starthousesE.grid(row=3, column=4)
        starthousesL = Label(root, text="Starting Houses")
        starthousesL.grid(row=3, column=5)

        space4 = Label(root, text="    ")
        space4.grid(row=4, column=0)

        #house revenue
        houserevenueE = Entry(root)
        houserevenueE.insert(0, 3)
        houserevenueE.grid(row=5, column=1)
        houserevenueL = Label(root, text="House Cost")
        houserevenueL.grid(row=5, column=2)

        #confirm button
        customconfirm = Button(root, text="Use these settings", command=lambda: customconfirmClick(root, turnsE, starthousesE, startmoneyE, houserevenueE, housecostE, houseEntry))
        customconfirm.grid(row=5, column=4, columnspan=2)

#Verify everything inputed in custom setup works
def customconfirmClick(root, t, h, m, hr, hc, he):
    #Makes important variables globally and grabs info
    global turns
    global houses
    global money
    global houseRevenue
    global houseCost
    turns = t.get()
    houses = h.get()
    money = m.get()
    houseRevenue = hr.get()
    houseCost = hc.get()
    clear(root)
    #Tries to turn inputs to variables. If it fails it makes the user retry, or if any numbers are negative or turn is 0
    try:
        turns = int(turns)
        houses = int(houses)
        money = int(money)
        houseRevenue = int(houseRevenue)
        houseCost = int(houseCost)
        if turns < 1 or houses < 0 or money < 0 or houseRevenue < 0 or houseCost < 0:
            raise ValueError
        badInput = False
    except ValueError:
        #Tells user why and lets them retry
        print("One or more invalid inputs")
        error = Label(root, text="\nOne or more invalid inputs. Turns must be at least 1 and the rest must be at least 0\n")
        error.pack()
        ok = Button(root, text="Ok", command=lambda: dcClicked("Custom", root))
        ok.pack()
        badInput = True
    if badInput != True:
        #badInput is set to true if the input is bad. If it's good, it allows them to click start to go to play()
        beginspace1 = Label(root, text="")
        beginspace1.pack()
        begin1 = Button(root, text="Start", width=15, height=5, command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue, he, badTurn))
        begin1.pack()
        global turnNumber
        turnNumber = 0
        global badTurn
        badTurn = False

#Play the game
def play(root, turnNumber, turns, money, houses, houseCost, houseRevenue, houseEntry, badTurn):
    if turnNumber != 0:
        try:
            newHouses = int(houseEntry.get())
            price = newHouses*houseCost
            if price > money:
                #Text to appear if it costs too much, disappears after 3 seconds, sets badTurn to true
                tooMuch = Label(root, text="That would cost $" + str(price) + " but you only have $" + str(money))
                tooMuch.pack()
                root.after(3000, destroy, tooMuch)
                badTurn = True
            elif price < 0:
                #Text to appear if they put less than 0, disappears after 3 seconds, sets badTurn to true
                zero = Label(root, text="Please put 0 or more")
                zero.pack()
                root.after(3000, destroy, zero)
                badTurn = True
            else:
                #Input was good, updates houses and money and depending on turn does the next step
                houses += newHouses
                money = money - price
                money += houses*houseRevenue
                badTurn = False
        except ValueError:
            #Text to appear if input is not a number, disappears after 3 seconds, sets badTurn to true
            invalid = Label(root, text="Not a number")
            invalid.pack()
            root.after(3000, destroy, invalid)
            badTurn = True
    #If it's a good turn increase turnNumber by 1, give them information and ask how many houses to buy with and entry field. Sent to doTurn() when button is clicked
    if badTurn != True:
        turnNumber += 1
        clear(root)
        print("turns", turns, "money", money, "houses", houses, "houseCost", houseCost, "houseRevenue", houseRevenue)
        turnDisp = Label(root, text="Turn " + str(turnNumber) + "               \n\n$" + str(money) + "               \n\n" + str(houses) + " houses               \n")
        turnDisp.pack(side="right")
        hespace = Label(root, text="\n\n\n\n")
        hespace.pack()
        houseEntry = Entry(root)
        houseEntry.focus_set()
        houseEntry.pack()
        if turnNumber != turns:
            purchase = Button(root, text="Buy Houses", command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue, houseEntry, badTurn))
            purchase.pack()
        else:
            lastPurchase = Button(root, text="Buy Houses\nand Finish", command=lambda: endGame(root, turns, money, houses, houseEntry, houseCost, houseRevenue, badTurn))
            lastPurchase.pack()

#Shows results and asks to play again
def endGame(root, turns, money, houses, houseEntry, houseCost, houseRevenue, badTurn):
    try:
        newHouses = int(houseEntry.get())
        price = newHouses*houseCost
        if price > money:
            #Text to appear if it costs too much, disappears after 3 seconds, sets badTurn to true
            tooMuch = Label(root, text="That would cost $" + str(price) + " but you only have $" + str(money))
            tooMuch.pack()
            root.after(3000, destroy, tooMuch)
            badTurn = True
        elif price < 0:
            #Text to appear if they put less than 0, disappears after 3 seconds, sets badTurn to true
            zero = Label(root, text="Please put 0 or more")
            zero.pack()
            root.after(3000, destroy, zero)
            badTurn = True
        else:
            #Input was good, updates houses and money and depending on turn does the next step
            houses += newHouses
            money = money - price
            money += houses*houseRevenue
            badTurn = False
    except ValueError:
        #Text to appear if input is not a number, disappears after 3 seconds, sets badTurn to true
        invalid = Label(root, text="Not a number")
        invalid.pack()
        root.after(3000, destroy, invalid)
        badTurn = True
    if badTurn != True:
        clear(root)
        results = Label(root, text="\nYou've Completed The Game\nYou ended with " + str(money) + " dollars!\nYou also had " + str(houses) + " houses\n")
        results.pack()
        #First button goes to createGame(), other button goes to end()
        again = Button(root, text="Play Again", width=8, command=lambda: createGame(root))
        again.pack()
        quit = Button(root, text="Quit", width=7, command=lambda: end(root))
        quit.pack()

#Makes window
root = Tk()
root.title("House Game")
root.resizable(width=False, height=False)
root.geometry("530x220")

createGame(root)

root.mainloop()