import tkinter as tk
from tkinter import messagebox

class Tictactoes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tictactoe")

        self.current_player = "A"
        self.board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            self.board.append(row)


        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 30), width=10, height=4,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                
    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.update_button_text(row, col)
            
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "B" if self.current_player == "A" else "A"

    def update_button_text(self, row, col):
        self.root.grid_slaves(row=row, column=col)[0]["text"] = self.current_player

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "A"
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(text=" ")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Tictactoes()
    game.run()
