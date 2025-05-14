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

        self.buttons = []
        self.frames = []  # stocke les frames pour changer le style

        self.fenetre = tkinter.Tk()

def couleur_case():
    pass
    if self.check_win(self.boards[board_index]):

def play(self, big_row, big_col, small_row, small_col):

    pass

def check_win(self, board):
    
    pass

def check_global_win(self):

    pass

def reset_board(self, board_index):

    pass