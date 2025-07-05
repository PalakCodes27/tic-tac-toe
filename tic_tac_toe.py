from tkinter import *
from tkinter import messagebox
import random

# Function called on each turn
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        winner = check_winner()
        if not winner:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + "'s Turn"))
        elif winner == "Tie":
            label.config(text="It's a Tie!")
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            label.config(text=(player + " Wins!"))
            messagebox.showinfo("Game Over", player + " Wins!")

# Function to check winner
def check_winner():
    # Horizontal
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_buttons([(row, 0), (row, 1), (row, 2)])
            return True

    # Vertical
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            highlight_buttons([(0, col), (1, col), (2, col)])
            return True

    # Diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_buttons([(0, 0), (1, 1), (2, 2)])
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_buttons([(0, 2), (1, 1), (2, 0)])
        return True

    # Tie
    if not empty_spaces():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="cyan")
        return "Tie"

    return False

# Highlight winning buttons
def highlight_buttons(coords):
    for row, col in coords:
        buttons[row][col].config(bg="lightgreen")

# Check for empty spaces
def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return True
    return False

# Restart game
def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + "'s Turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

# Initialize game
window = Tk()
window.title("🎮 Tic Tac Toe")
window.resizable(False, False)

players = ["X", "O"]
player = random.choice(players)

label = Label(window, text=player + "'s Turn", font=('consolas', 30))
label.pack(pady=10)

reset_button = Button(window, text="Restart", font=('consolas', 20), command=new_game, bg="orange", fg="white")
reset_button.pack(pady=5)

frame = Frame(window)
frame.pack()

# 3x3 Buttons Grid
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(
            frame,
            text="",
            font=('consolas', 40),
            width=5,
            height=2,
            command=lambda row=row, col=col: next_turn(row, col)
        )
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
