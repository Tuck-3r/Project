from tkinter import *

window = Tk()
window.title("O-X Game")
players = ["X", "O"]
current_player = players[0]
board = [["" for _ in range(3)] for _ in range(3)]
game_over = False
scores = {"X": 0, "O": 0}

def handle_click(row, col):
    global current_player, game_over
    
    if board[row][col] == "" and not game_over:
        buttons[row][col]["text"] = current_player
        buttons[row][col]["state"] = DISABLED
        
        board[row][col] = current_player
        
        if check_win() or check_draw():
            game_over = True
            if check_win():
                scores[current_player] += 1
                messagebox.showinfo("Game Over", f"{current_player} wins!")
            else:
                messagebox.showinfo("Game Over", "It's a draw!")
            
            score_label_x.config(text=f"X: {scores['X']}")
            score_label_o.config(text=f"O: {scores['O']}")
        else:
            current_player = players[1] if current_player == players[0] else players[0]
            label.config(text=f"{current_player}'s turn")

def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            highlight_winner(0, col, 1, col, 2, col)
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        return True
    
    return False

def highlight_winner(row1, col1, row2, col2, row3, col3):
    buttons[row1][col1].config(bg="lightgreen")
    buttons[row2][col2].config(bg="lightgreen")
    buttons[row3][col3].config(bg="lightgreen")

def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

def reset_game():
    global current_player, game_over, board
    
    current_player = players[0]
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]
    
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["state"] = NORMAL
            buttons[row][col].config(bg="white" if (row + col) % 2 == 0 else "black")

    label.config(text=f"{current_player}'s turn")
    
    score_label_x.config(text=f"X: {scores['X']}")
    score_label_o.config(text=f"O: {scores['O']}")

window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
window.columnconfigure([0, 1, 2], weight=1)

label = Label(window, text=f"{current_player}'s turn", font=('Arial', 20), pady=10)
label.grid(row=0, column=0, columnspan=3)

reset_button = Button(window, text="Reset", font=('Arial', 14), padx=10, pady=5, command=reset_game)
reset_button.grid(row=1, column=0, columnspan=3)

buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = Button(window, text="", font=('Arial', 40), width=4, height=2,
                        command=lambda row=row, col=col: handle_click(row, col),
                        bg="white" if (row + col) % 2 == 0 else "lightgray")
        button.grid(row=row+2, column=col, padx=5, pady=5, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)

score_label_x = Label(window, text=f"X: {scores['X']}", font=('Arial', 16))
score_label_x.grid(row=5, column=0)

score_label_o = Label(window, text=f"O: {scores['O']}", font=('Arial', 16))
score_label_o.grid(row=5, column=2)

window.mainloop()
