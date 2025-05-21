import tkinter
import time 

class Tic_Tac_Boom:
    def __init__(self):
        """
        Initialisation de la classe avec leurs variable
        """
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
        self.create_ui()

    def create_ui(self):
        """
        Crée l'interface utilisateur du jeu
        Cette fonction ne retourne rien car elle créer seulement l'interface à l'intérieur de la fonction
        """
        # Grille principale
        for big_row in range(3):
            for big_col in range(3):
                # Frames de l'interface graphique
                frame = tkinter.Frame(self.fenetre, highlightbackground="black", highlightthickness=2)
                # Sauvegarder dans la variable pour pouvoir changer sa highlightthickness
                self.frames.append(frame)
                # Placement de la frame
                frame.grid(row=big_row, column=big_col, padx=8, pady=4)
                board_buttons = []
                # Grilles secondaires
                for small_row in range(3):
                    for small_col in range(3):
                        # Placement de la grille
                        index = 3 * small_row + small_col
                        btn = tkinter.Button(frame, text=" ", width=8, height=4,
                                        command=lambda: self.play(big_row, big_col, small_row, small_col))
                        btn.grid(row=small_row, column=small_col)
                        # Sauvegarde du boutton dans la variable
                        board_buttons.append(btn)
                self.buttons.append(board_buttons)
        self.active_case()
    
    def active_case(self):
        """
        Surligne la bordure de la case où l’on doit jouer
        """
        for i, frame in enumerate(self.frames):
            if self.active_board is None or self.board_wins[i] != " ":
                frame.configure(highlightbackground="black", highlightthickness=2)
            elif i == self.active_board:
                frame.configure(highlightbackground="darkblue", highlightthickness=4)
            else:
                frame.configure(highlightbackground="black", highlightthickness=2)

    def case_color_win():
        pass
        

    def play(self, big_row, big_col, small_row, small_col):

        pass

    def check_win(self, board):
        if board[0][0] == board[1][1] == board[2][2] != '' :
            return True
        if board[2][0] == board[1][1] == board[0][2] != '' :
            return True
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '' :
                return True
            if board[0][i] == board[1][i] == board[2][i] != '' :
                return True


    def check_draw(self, board_index): 
        
        for i in range(3):
            for j in range(3) :
                if board[board_index][i][j] == ' ' :
                    return False
        return True

    def check_global_win(self):

        pass

    def reset_board(self, board_index):

        pass

    def temps_1mn(self):
        #activation
        clockX = 60 
        while self.current_player == 'X' :
            time.sleep(1) 
            clockX -= 1
        clockX += 2 
        while self.current_player == 'O' :
            time.sleep(1)
            clockO -= 1
        clockO += 2 
        return clockO, clockX

                

    def temps_5mn(self):
        clockO = 300
        clockX = 300
        while self.current_player == 'X' :
            time.sleep(1)
            clockX -= 1
        clockX += 3 
        while self.current_player == 'O' :
            time.sleep(1)
            clock0 -= 1
        clock0 += 3 
        return clockO, clockX

    def temps_10mn(self):
        clockO = 600
        clockX = 600
        while self.current_player == 'X' :
            time.sleep(1)
            clockX -= 1 
        while self.current_player == '0' :
            time.sleep(1)
            clock0 -= 1
        return clockO, clockX
    
    def temps_perso(self, tps, incrementation):
        clockO = tps*60
        clockX = tps*60
        while clock0 <= 0 or clockX <= 0:
            while self.current_player == 'X' :
                time.sleep(1)
                clockX -= 1
            clockX += incrementation
            while self.current_player == 'O' :
                time.sleep(1)
                clock0 -= 1
            clock0 += incrementation
        return clockO, clockX
        



partie = Tic_Tac_Boom()
partie.fenetre.mainloop()