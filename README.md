# 🎰 Slot Machine Game in Python

This project is a text-based slot machine game built using Python. It simulates a classic slot machine experience, allowing players to deposit money, place bets, and spin the machine to win or lose based on randomly generated outcomes. The game incorporates features like multi-line betting, partial wins, bonus rounds, and a dynamic balance that updates with each spin.

## 🌟 Features

- **Multi-Line Betting**: Players can place bets on 1 to 3 lines, increasing their chances of winning.
- **Randomized Slot Machine**: The slot machine uses different symbols, each with specific frequencies, to create a randomized outcome for each spin.
- **Partial Wins**: After playing several rounds, players can unlock the potential for partial wins, where they win a portion of their bet if certain conditions are met.
- **Bonus Rounds**: Players have a chance to unlock a bonus round that significantly multiplies their winnings after multiple plays.
- **Dynamic Balance Management**: The player's balance updates in real-time, reflecting wins, partial wins, and losses after each spin.
- **Replay Option**: After each round, players can choose to play again or quit the game.

## 🛠️ How It Works

### 1. **Deposit Money**
   - The game begins by asking the player to deposit an initial amount. This balance is used to place bets on the slot machine.
   - The deposited amount must be greater than zero.

### 2. **Choose Number of Lines**
   - The player selects how many lines they want to bet on. They can choose between 1, 2, or 3 lines.
   - The number of lines chosen impacts the total amount bet per round.

### 3. **Place a Bet**
   - The player enters the amount they wish to bet on each line. The total bet is calculated as the bet per line multiplied by the number of lines.
   - The bet amount must be a positive integer and must not exceed the player's remaining balance.

### 4. **Spin the Slot Machine**
   - The slot machine consists of a 3x3 grid filled with symbols. These symbols (`~`, `#`, `$`) appear with different frequencies.
   - The grid is populated randomly each time the player spins, ensuring a unique outcome for every round.

### 5. **Check for Wins**
   - The game checks each row of the slot machine grid for matching symbols.
   - If all symbols in a row match, the player wins an amount calculated based on the symbol type and the total bet.
   - **Partial Wins**: If only some of the lines match and the player has played a certain number of times, they may still win a portion of their bet.
   - **Bonus Round**: If a special condition is met (based on a random number and the number of plays), the player can unlock a bonus round that multiplies their winnings significantly.

### 6. **Update Balance and Replay**
   - The player’s balance is updated based on the result of the spin. If the player wins, their balance increases; if they lose, the bet amount is deducted.
   - The player is then given the option to play again or to quit. If they choose to play again and have a positive balance, the process repeats.

## 🔍 Code Overview

### `deposit()`
- Prompts the player to enter an initial deposit amount. The amount must be a positive integer.

### `getNumberOfLines()`
- Asks the player to choose the number of lines (1-3) they want to bet on. Ensures the input is valid and within the allowed range.

### `bettingFunc(lines)`
- Prompts the player to place a bet per line. Calculates the total bet based on the number of lines selected and validates that the player’s balance is sufficient.

### `multiplier(bet_amt, lines)`
- Calculates the total bet by multiplying the bet amount by the number of lines.

### `get_slot_machine(rows, cols, symbols)`
- Randomly generates the slot machine grid (3x3) using the provided symbols and their frequencies.

### `print_m_values(machine_vals)`
- Displays the generated slot machine grid in a readable format.

### `checkWin(lines, total_bet, machine_vals)`
- Evaluates the slot machine grid to determine if the player has won, partially won, or lost. Updates the player’s balance accordingly and handles partial wins and bonus rounds.

### `playAgain()`
- Asks the player if they want to continue playing. Updates the game state based on the player's choice.

## 🎮 How to Play

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/slot-machine-game.git
   cd slot-machine-game
   ```

2. **Run the Game**:
   ```bash
   python slot_machine.py
   ```

3. **Deposit Money**:
   - The game will prompt you to enter an amount to deposit. This balance is used for placing bets.

4. **Select Number of Lines**:
   - Choose between 1, 2, or 3 lines to bet on.

5. **Place Your Bet**:
   - Enter the amount you want to bet on each line. The game will calculate the total bet for you.

6. **Spin the Slot Machine**:
   - The game will generate a 3x3 grid of symbols and display the results.

7. **Check Your Winnings**:
   - The game will evaluate the grid and update your balance based on the outcome.

8. **Play Again or Quit**:
   - After the results are displayed, choose whether to play another round or quit the game.

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** is required to run this game.

### Installing
1. Clone the repository using the command:
   ```bash
   git clone https://github.com/yourusername/slot-machine-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd slot-machine-game
   ```

3. Run the Python script:
   ```bash
   python slot_machine.py
   ```

## 📋 Requirements

- **Python 3.x**: The game is built using standard Python libraries and requires Python 3.x to run.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request. You can also open an issue if you find any bugs or have questions.
