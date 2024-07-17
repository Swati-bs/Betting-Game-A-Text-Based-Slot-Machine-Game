#This is a betting game that lets u bet on MAX 3 lines. You can bet specific amount for one line same will be
#considered for remaining lines.The deposit amount entered in the beginning should be greater than your total_bet
#whenever you lose, the bet amount will be reduced from your deposit and whenever you win, You earn double of your bet amount
#You can play the game repeatatively until you run out of money or as per your wish

import random
MAX_LINES = 3           #declaring global object/constant to prevent changing the variable everywhere used when we want to change the value

def deposit():
    while True:
        amount = input("How much would you like to Deposit? $ ")            #amount to keep track of deposit amount
        if amount.isdigit():        #this function doesn't consider negative values as digit
            amount = int(amount)        #Convert it into int as it's string in default form
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")
    return amount

def multiplier(bet_amt, lines):
    total_bet = bet_amt * lines
    return total_bet
    

def bettingFunc(balance,lines):
    while True:
        bet_amt = input("Enter the amount you want to bet on each line: \n$ ")
        if bet_amt.isdigit():        #this function doesn't consider negative values as digit
            bet_amt = int(bet_amt)
            total_bet = multiplier(bet_amt,lines)
            if bet_amt > 0 and total_bet <= balance:
                print(f"You're betting ${bet_amt} on {lines} lines. The total betting amount will be ${total_bet}")
                break
            else:
                print(f"You don't have enough amount to bet that, Your balance is :${balance}")
        else:
            print("Please enter a number")
    return total_bet

def getNumberOfLines(balance):
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINES}):\n ")
        if lines.isdigit():        #this function doesn't consider negative values as digit
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                total_bet = bettingFunc(balance,lines)      #total_bet refers to total bet amount
                break
            else:
                print(f"The number of lines should range between 1-{MAX_LINES}")
        else:
            print("Please enter a number")
            getNumberOfLines(balance)
    return total_bet

def playAgain():
    if balance > 0:
        choice = input("Do you want to play again ? Y or N ^_^ :\n ")
        if choice == 'y' or 'Y':
            print(f"Now your total balance is {balance}")
            main(balance)
        elif choice == 'n' or 'N':
            print("Thank you for playing!")
        else:
            print("Thank YOu")
    else:
        print("You ran out of your deposit!Please refresh to play again")


def checkGuess(yourGuess,realGuess,balance,total_bet):              #to check if the guess is right
    if yourGuess == realGuess:
        balance = balance + total_bet                           #if guess is correct add the bet amount to balance
        print(f"Congratulations!! You Won! Your Total balance is now : ${balance}")
        playAgain()
    else:
        balance = balance - total_bet                           #if guess is wrong reduce the balance by bet amount
        print(f"Sorry! You lost! Better Luck Next Time\nNow Your total balance is: ${balance}")
        playAgain()                                             #to ask if player wants to play again
    return balance

def generateNum(balance,total_bet):                         
    realGuess = random.randint(1,10)                #generates a number in the given range
    #print(realGuess)                                #only for functionality check
    yourGuess = input("Enter your guess(1-10):\n ")          #to store the guess value of user
    if yourGuess.isdigit():
        yourGuess = int(yourGuess)
        if yourGuess < 11 and yourGuess > 0 :
            balance = checkGuess(yourGuess,realGuess,balance,total_bet)
        else:
            yourGuess = print("Please enter a number in the range (1-10):\n ")
            balance = checkGuess(yourGuess,realGuess)
    else:
        yourGuess = print("Please Enter a number(1-10):\n ")
        balance = checkGuess(yourGuess,realGuess)
    return balance

def main(balance):
    total_bet = getNumberOfLines(balance)           #total_bet is the total amount considering number of lines
    balance = generateNum(balance,total_bet)        # balance is the amount left in deposit
    return balance,total_bet

balance  = deposit()
balance, total_bet = main(balance)

def playAgain():                #to play again and again without refreshing
    if balance > 0:
        choice = input("Do you want to play again ? Y or N ^_^ :\n ")
        if choice == 'y' or 'Y':
            print(f"Now your total balance is {balance}")
            main(balance)
        else:
            print("Thank you for playing!")
    else:
        print("You ran out of your deposit!Please refresh to play again")