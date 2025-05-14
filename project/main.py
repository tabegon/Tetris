import tkinter

class Tic_Tac_Boom:
    def __init__(self):
        # Les joueurs
        self.players = ['O', 'X']
        # Le joueur qui commence
        self.current_player = "X"
        # Créations des grilles
        self.boards = [[[" " for i in range(3)] for i in range(3)] for i in range(9)]
        # Création de la grille principale
        self.board_wins = [" " for i in range(9)]
        # Faire commencer dans le morpion du milieu
        self.active_board = 4

        # Initialisation des boutons et des frames
        self.buttons = []
        self.frames = []


        self.fenetre = tkinter.Tk()

    def create_ui(self):
        # Grille principale
        for big_row in range(3):
            for big_col in range(3):
                # Frames de l'interface graphique
                frame = tkinter.Frame(self.root, highlightbackground="black", highlightthickness=2)
                # Sauvegarder dans la variable pour pouvoir changer sa highlightthickness
                self.frames.append(frame)
                # Placement de la frame
                frame.grid(row=big_row, column=big_col, padx=2, pady=2)
                board_buttons = []
                # Grilles secondaires
                for small_row in range(3):
                    for small_col in range(3):
                        # Placement de la grille
                        index = 3 * small_row + small_col
                        btn = tkinter.Button(frame, text=" ", width=8, height=4,
                                        command=lambda br=big_row, bc=big_col, sr=small_row, sc=small_col: self.play(br, bc, sr, sc))
                        btn.grid(row=small_row, column=small_col)
                        # Sauvegarde du boutton dans la variable
                        board_buttons.append(btn)
                self.buttons.append(board_buttons)
        self.highlight_active_board()
    
    def highlight_active_board(self):
        for i, frame in enumerate(self.frames):
            if self.active_board is None or self.board_wins[i] != " ":
                frame.configure(highlightbackground="black", highlightthickness=2)
            elif i == self.active_board:
                frame.configure(highlightbackground="darkblue", highlightthickness=4)
            else:
                frame.configure(highlightbackground="black", highlightthickness=2)

    def couleur_case():
        pass
        

    def play(self, big_row, big_col, small_row, small_col):

        pass

    def check_win(self, board):
        
        pass

    def check_global_win(self):

        pass

    def reset_board(self, board_index):

        pass

partie = Tic_Tac_Boom()

