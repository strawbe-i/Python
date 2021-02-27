from tkinter import *
import time

def clear(root):
    for widget in root.winfo_children():
        widget.destroy()

def destroy(widget):
    widget.destroy()

def end(root):
    root.destroy()

def dcClicked(clicked, root):
    clear(root)

    if clicked == "Default":
        global turns
        global houses
        global money
        global houseRevenue
        global houseCost
        turns = 10
        money = 10
        houses = 0
        houseCost = 5
        houseRevenue = 3

        beginspace0 = Label(root, text="")
        beginspace0.pack()

        begin0 = Button(root, text="Start", width=15, height=5, command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue))
        begin0.pack()

        global turnNumber
        turnNumber = 0
    else:
        cusinfo = Label(root, text="Custom\nGame")
        cusinfo.grid(row=0, column=3)

        space0 = Label(root, text="    ")
        space0.grid(row=1, column=0)

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
        customconfirm = Button(root, text="Use these settings", command=lambda: customconfirmClick(root, turnsE, starthousesE, startmoneyE, houserevenueE, housecostE))
        customconfirm.grid(row=5, column=4, columnspan=2)

def customconfirmClick(root, t, h, m, hr, hc):
    #makes important variables globally and grabs info
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
        print("One or more invalid inputs")
        error = Label(root, text="One or more invalid inputs. Turns must be at least 1 and the rest must be at least 0")
        error.pack()
        ok = Button(root, text="Ok", command=lambda: dcClicked("Custom", root))
        ok.pack()
        badInput = True
    if badInput != True:
        beginspace1 = Label(root, text="")
        beginspace1.pack()
        begin1 = Button(root, text="Start", width=15, height=5, command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue))
        begin1.pack()
        global turnNumber
        turnNumber = 0
        global badTurn
        badTurn = False

def play(root, turnNumber, turns, money, houses, houseCost, houseRevenue):
    turnNumber += 1
    clear(root)
    print("turns", turns, "money", money, "houses", houses, "houseCost", houseCost, "houseRevenue", houseRevenue)
    #start turns
    turnDisp = Label(root, text="Turn " + str(turnNumber) + "\n\nYou currently have " + str(money) + " dollars and " + str(houses) + " houses\n")
    turnDisp.pack()
    houseEntry = Entry(root)
    houseEntry.focus_set()
    houseEntry.pack()
    purchase = Button(root, text="Buy Houses", command=lambda: doTurn(root, turnNumber, houseEntry, turns, money, houses, houseCost, houseRevenue))
    purchase.pack()

def doTurn(root, turnNumber, he, turns, money, houses, houseCost, houseRevenue):
    try:
        newHouses = int(he.get())
        price = newHouses*houseCost
        if price > money:
            tooMuch = Label(root, text="That would cost " + str(price) + " dollars but you only have " + str(money))
            tooMuch.pack()
            root.after(3000, destroy, tooMuch)
        elif price < 0:
            zero = Label(root, text="Please put 0 or more")
            zero.pack()
            root.after(3000, destroy, zero)
        else:
            clear(root)
            houses += newHouses
            money = money - price
            money += houses*houseRevenue
            turnSummary = Label(root, text="\nYou bought " + str(newHouses) + " houses for " + str(price) + " dollars\nYou've made " + str(houses*houseRevenue) + " dollars this turn leaving you with a total of " + str(money) + " dollars\n\n")
            turnSummary.pack()
            if turnNumber != turns:
                next = Button(root, text="Next Turn", command=lambda: play(root, turnNumber, turns, money, houses, houseCost, houseRevenue))
                next.pack()
            else:
                finish = Button(root, text="Finish", command=lambda: endGame(root, turns, money, houses))
                finish.pack()
    except ValueError:
        invalid = Label(root, text="Not a number")
        invalid.pack()
        root.after(3000, destroy, invalid)

def endGame(root, turns, money, houses):
    clear(root)
    results = Label(root, text="\nYou've Completed The Game\nYou ended with " + str(money) + " dollars!\nYou also had " + str(houses) + " houses\n")
    results.pack()
    again = Button(root, text="Play Again", width=8, command=lambda: createGame(root))
    again.pack()
    quit = Button(root, text="Quit", width=7, command=lambda: end(root))
    quit.pack()

def createGame(root):
    clear(root)
    start0 = Label(root, text="Welcome to the House Game!\nThere are 10 turns\nYou'll start with 10 dollars\nEach turn you can buy as many houses as you want at 5 dollars each\nEvery turn each houses you own makes you 3 dollars\nThe goal is to have as much money as possible at the end of the game")
    start0.pack()
    start1 = Label(root, text="Would you like to play with these default rules or make custom rules?", height=2)
    start1.pack()

    default = Button(root, text="Default", width = 7, command=lambda: dcClicked("Default", root))
    default.pack()
    defcusspacer = Label(root, text="")
    defcusspacer.pack()
    custom = Button(root, text="Custom", width = 7, command=lambda: dcClicked("Custom", root))
    custom.pack()

root = Tk()
root.title("House Game")
root.geometry("530x220")

#start0 is the welcome and rules text, start1 asks how they'd like to play
start0 = Label(root, text="Welcome to the House Game!\nThere are 10 turns\nYou'll start with 10 dollars\nEach turn you can buy as many houses as you want at 5 dollars each\nEvery turn each houses you own makes you 3 dollars\nThe goal is to have as much money as possible at the end of the game")
start0.pack()
start1 = Label(root, text="Would you like to play with these default rules or make custom rules?", height=2)
start1.pack()

#default and custom buttons
default = Button(root, text="Default", width = 7, command=lambda: dcClicked("Default", root))
default.pack()
defcusspacer = Label(root, text="")
defcusspacer.pack()
custom = Button(root, text="Custom", width = 7, command=lambda: dcClicked("Custom", root))
custom.pack()

root.mainloop()