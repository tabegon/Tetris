import tkinter as tk
from tkinter import messagebox

class UltimateTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Tic Tac Toe")
        self.current_player = "X"
        self.boards = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(9)]
        self.board_wins = [" " for _ in range(9)]
        self.active_board = None  # None = libre
        self.buttons = []
        self.frames = []  # stocke les frames pour changer le style
        self.create_ui()

    def create_ui(self):
        for big_row in range(3):
            for big_col in range(3):
                frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
                self.frames.append(frame)
                frame.grid(row=big_row, column=big_col, padx=2, pady=2)
                board_buttons = []
                for small_row in range(3):
                    for small_col in range(3):
                        index = 3 * small_row + small_col
                        btn = tk.Button(frame, text=" ", width=4, height=2,
                                        command=lambda br=big_row, bc=big_col, sr=small_row, sc=small_col: self.play(br, bc, sr, sc))
                        btn.grid(row=small_row, column=small_col)
                        board_buttons.append(btn)
                self.buttons.append(board_buttons)

    def play(self, big_row, big_col, small_row, small_col):
        board_index = 3 * big_row + big_col
        
        # Vérifier si le plateau a déjà été gagné
        if self.board_wins[board_index] != " ":
            messagebox.showwarning("Plateau terminé", "Ce morpion a déjà été gagné.")
            return

        cell_index = 3 * small_row + small_col

        # Vérifier zone valide
        if self.active_board is not None and self.active_board != board_index:
            messagebox.showwarning("Zone invalide", f"Vous devez jouer dans la zone {self.active_board}")
            return

        # Vérifier case vide
        if self.boards[board_index][small_row][small_col] != " ":
            return

        # Jouer
        self.boards[board_index][small_row][small_col] = self.current_player
        self.buttons[board_index][cell_index]["text"] = self.current_player
        self.buttons[board_index][cell_index]["state"] = "disabled"

        # Vérifier victoire locale
        if self.check_win(self.boards[board_index]):
            self.board_wins[board_index] = self.current_player
            self.color_board_win(board_index, self.current_player)
        elif self.board_full(self.boards[board_index]):
            # Égalité → on reset le plateau
            self.reset_board(board_index)


        # Vérifier victoire globale
        if self.check_global_win():
            messagebox.showinfo("Victoire", f"Le joueur {self.current_player} a gagné !")
            self.root.quit()
            return

        # Déterminer prochain plateau
        self.active_board = 3 * small_row + small_col
        if self.board_wins[self.active_board] != " " or self.board_full(self.boards[self.active_board]):
            self.active_board = None  # Libre

        self.highlight_active_board()

        # Changer joueur
        self.current_player = "O" if self.current_player == "X" else "X"

    def board_full(self, board):
        return all(cell != " " for row in board for cell in row)

    def check_win(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

    def check_global_win(self):
        board = [[self.board_wins[3 * i + j] for j in range(3)] for i in range(3)]
        return self.check_win(board)

    def color_board_win(self, board_index, player):
        for btn in self.buttons[board_index]:
            btn.configure(bg="lightgreen" if player == "X" else "lightblue")
    
    def reset_board(self, board_index):
        self.boards[board_index] = [[" " for _ in range(3)] for _ in range(3)]
        self.board_wins[board_index] = " "
        for i in range(9):
            btn = self.buttons[board_index][i]
            btn["text"] = " "
            btn["state"] = "normal"
            btn["bg"] = "SystemButtonFace"

    def highlight_active_board(self):
        for i, frame in enumerate(self.frames):
            if self.active_board is None or self.board_wins[i] != " ":
                frame.configure(highlightbackground="black", highlightthickness=1)
            elif i == self.active_board:
                frame.configure(highlightbackground="darkblue", highlightthickness=3)
            else:
                frame.configure(highlightbackground="black", highlightthickness=1)



# Lancer le jeu
if __name__ == "__main__":
    root = tk.Tk()
    game = UltimateTicTacToe(root)
    root.mainloop()