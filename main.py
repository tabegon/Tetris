class Morpion() : 
    def __init__(self) : 
        self.matrice = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.accessibility = 0
        self.coordonees = None
    
    def write_on_button(self) :
        pass
    
def next_turn() : 
    
    pass



a = Morpion()
b = Morpion()
c = Morpion()
d = Morpion()
e = Morpion()
f = Morpion()
g = Morpion()
h = Morpion()
i = Morpion()

players = ['X', 'O']
player = random.choice(players)

tictactoe = [[a.matrice, b.matrice, c.matrice],
            [d.matrice, e.matrice, f.matrice],
            [g.matrice, h.matrice, i.matrice]]

print(tictactoe)