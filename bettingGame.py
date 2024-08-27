import random

# Constants
MAX_LINES = 3  # Maximum lines a player can bet on
ROWS = 3       # Number of rows in the slot machine
COLS = 3       # Number of columns in the slot machine
BALANCE = 0    # Player's balance initialized to 0
PLAYINGAGAIN = True  # Flag to control if the player wants to play again
AGAINCOUNT = 0  # Count of how many times the player has played
BONUSAMT = 5    # Bonus amount awarded under certain conditions

# Symbols and their counts
symbol_count = {
    "~": 6,
    "#": 6,
    "$": 7,
}

# Function to prompt the user to deposit an initial amount and validate it
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():  # Check if the input is a valid positive number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount

# Main function to start the betting process
def main():
    lines = getNumberOfLines()  # Get the number of lines to bet on
    total_bet = bettingFunc(lines)  # Calculate the total bet amount
    return lines, total_bet

# Function to prompt the user to choose the number of lines to bet on and validate it
def getNumberOfLines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINES}):\n")
        if lines.isdigit():  # Check if the input is a valid number within the allowed range
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f"The number of lines should range between 1-{MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines


# Function to prompt the user to place a bet and validate if the balance is sufficient
def bettingFunc(lines):
    while True:
        print(f"You have a balance of ${BALANCE} left from your deposit.")
        bet_amt = input("Enter the amount you want to bet on each line: \n$ ")
        if bet_amt.isdigit():  # Check if the input is a valid positive number
            bet_amt = int(bet_amt)
            total_bet = multiplier(bet_amt, lines)  # Calculate the total bet amount
            if bet_amt > 0 and total_bet <= BALANCE:  # Ensure the total bet amount does not exceed the player's balance
                print(f"You're betting ${bet_amt} on {lines} lines. The total betting amount will be ${total_bet}.")
                break
            else:
                print(f"You don't have enough balance to place this bet. Your balance is: ${BALANCE}.")
        else:
            print("Please enter a valid number.")
    return total_bet

# Function to calculate the total bet amount based on the bet per line and the number of lines
def multiplier(bet_amt, lines):
    total_bet = bet_amt * lines
    return total_bet
 
# Function to generate random symbols for the slot machine based on the available symbols
def get_slot_machine(rows, cols, symbols):         
    all_symbols = []
    for symbol,symbol_cnt in symbols.items():
        for _ in range(symbol_cnt):
            all_symbols.append(symbol)          # Create a list of all symbols based on their frequency
    
    columns = []                                 # nested list for columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]                 #Copying the list to avoid modifying the original
        for _ in range(rows):
            value = random.choice(current_symbols)       #randomly choose the symbol out of all the symbols 
            current_symbols.remove(value)
            column.append(value)                         # Generate each column with random symbols
        columns.append(column)          #add all the column lists into main columns list
    return columns

# Function to display the slot machine values in a readable format
def print_m_values(machine_vals):              
    for row in machine_vals:
        for i in range(len(row)):
            if i == len(row) - 1:
                 print(row[i] , end=" ")
            else:
                print(row[i] , end=" | ")
        print("\n")

# Function to check if the player has won, update their balance, and handle partial wins after a condition is met   
def checkWin(lines,total_bet,machine_vals):
    global BALANCE,AGAINCOUNT
    flag = 0                        #flag bit to check how many rows have met condition
    betMul = 0                      #To decide by how much the total_bet amount should be multiplied with
    for sublist in machine_vals:          # Check each row of the slot machine for matching symbols    
        if all(s_element == sublist[0] for s_element in sublist):  #each values of a row
            flag = flag + 1                 
            for symbol,symbol_cnt in symbol_count.items():  
                if sublist[0] == symbol:
                    betMul = betMul + symbol_cnt        # Calculate the multiplier based on the symbol
        else:
            pass

    # Determine if the player has won or partially won
    if flag == lines:                                   #complete win
        BALANCE += total_bet * betMul                   #if guess is correct add the bet amount to BALANCE
        print(f"Congratulations!! You Won!")
    elif flag != 0 and AGAINCOUNT > 15:                  #partial win 
        print("You've unlocked Partial win level! Keep playing \n")
        print(f"Don't give up!! You Won Partially by {flag} lines \n")
        if flag == (lines - (lines - 1)):
            BALANCE += total_bet * betMul * 2
        elif flag == 1:                                 # One row matches
            BALANCE += total_bet * betMul                           
    else:
        BALANCE = BALANCE - total_bet                     #Deduct the bet amount if the player loses
        print(f"Sorry! You lost! Better Luck Next Time\n")
    print(f"Now Your total BALANCE is: ${BALANCE}\n")
    playAgain()
    return BALANCE

# Function to ask the player if they want to play again and update the game state
def playAgain():                
    global PLAYINGAGAIN,AGAINCOUNT
    while True:
        if BALANCE > 0:
            choice = str(input("Do you want to play again ? Y or N  :\n "))
            if choice == 'n' or choice =='N':
                print("Thank you for playing")
                PLAYINGAGAIN = False
                break
            else:
                AGAINCOUNT += 1
                print(f"Now your total BALANCE is {BALANCE}")
                PLAYINGAGAIN = True
                break
        else:
            print("You ran out of your deposit! Please refresh to play again")


BALANCE  = deposit()        # Prompt the player to deposit money
# Game loop
while PLAYINGAGAIN == True:
    lines, total_bet = main()       # Start the betting process
    machine_vals = get_slot_machine(ROWS,COLS,symbol_count)        # Generate the slot machine values
    print_m_values(machine_vals)            # Display the slot machine values
    ranNum = random.randint(1,5)            # Generate a random number to check for bonus
    if ranNum == lines and AGAINCOUNT >= 2:     # Check if the player wins a bonus
        print("Hurray! You unlocked the BONUS!!")
        print(f"You won 3x the amount you bet on {total_bet * BONUSAMT}\n")
        BALANCE += total_bet * BONUSAMT
    BALANCE = checkWin(lines, total_bet, machine_vals)       #Check if the player wins and update their balance
