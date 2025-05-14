import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog, colorchooser


class UltimateTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Tic Tac Toe")
        self.current_player = "X"
        self.boards = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(9)]
        self.board_wins = [" " for _ in range(9)]
        self.active_board = 4
        self.buttons = []
        self.frames = []  # stocke les frames pour changer le style
        self.symbols = {"X": "X", "O": "O"}
        self.colors = {"X": "lightgreen", "O": "lightblue"}
        self.create_ui()
        self.create_menu()


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
                        btn = tk.Button(frame, text=" ", width=8, height=4,
                                        command=lambda br=big_row, bc=big_col, sr=small_row, sc=small_col: self.play(br, bc, sr, sc))
                        btn.grid(row=small_row, column=small_col)
                        board_buttons.append(btn)
                self.buttons.append(board_buttons)
        self.highlight_active_board()


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
        self.buttons[board_index][cell_index]["text"] = self.symbols[self.current_player]
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
        self.print_terminal_board()


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
            btn.configure(bg=self.colors[player])
    
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
                frame.configure(highlightbackground="darkblue", highlightthickness=5)
            else:
                frame.configure(highlightbackground="black", highlightthickness=1)
    
    def print_terminal_board(self):
        def board_to_char(index):
            return self.board_wins[index] if self.board_wins[index] != " " else str(index)

        print("\n" + "=" * 30)
        print("État du plateau global :")
        for big_row in range(3):
            for small_row in range(3):
                row = []
                for big_col in range(3):
                    board_index = 3 * big_row + big_col
                    cells = self.boards[board_index][small_row]
                    row.append(" ".join(cells))
                print(" || ".join(row))
            print("-" * 24)
        print("\nProchain joueur :", self.current_player)
        if self.active_board is None:
            print("Zone libre")
        else:
            print("Jouez dans la zone :", self.active_board)
        print("=" * 24)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        options_menu = tk.Menu(menubar, tearoff=0)

        options_menu.add_command(label="Changer symbole joueur X", command=self.change_symbol_x)
        options_menu.add_command(label="Changer symbole joueur O", command=self.change_symbol_o)
        options_menu.add_separator()
        options_menu.add_command(label="Changer couleur joueur X", command=self.change_color_x)
        options_menu.add_command(label="Changer couleur joueur O", command=self.change_color_o)

        menubar.add_cascade(label="Options", menu=options_menu)
        self.root.config(menu=menubar)

    def change_symbol_x(self):
        new_symbol = simpledialog.askstring("Symbole Joueur X", "Entrez un nouveau symbole pour le joueur X :")
        if new_symbol:
            self.symbols["X"] = new_symbol

    def change_symbol_o(self):
        new_symbol = simpledialog.askstring("Symbole Joueur O", "Entrez un nouveau symbole pour le joueur O :")
        if new_symbol:
            self.symbols["O"] = new_symbol

    def change_color_x(self):
        color = colorchooser.askcolor(title="Choisir la couleur du joueur X")[1]
        if color:
            self.colors["X"] = color

    def change_color_o(self):
        color = colorchooser.askcolor(title="Choisir la couleur du joueur O")[1]
        if color:
            self.colors["O"] = color





# Lancer le jeu
root = tk.Tk()
game = UltimateTicTacToe(root)
root.mainloop()