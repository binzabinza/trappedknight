import sys
import matplotlib.pyplot as plt

#class definitions

class Point:
    #point object, defaults to origin
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y

class Piece:
    #piece object, defaults to standard knight
    def __init__(self, di=1, dj=2, p=Point()):
        self.di = di
        self.dj = dj
        self.current = p
        self.visited = {p}


#general methods

def spiral_cell(x,y):
    #determines value at a given point
    n    = max(abs(x), abs(y))   #square number 
    c_n1 = (2*n+1)*(2*n+1)       #largest value in the given square, c_n,1

    if x == n:
        return c_n1 - (n + y)
    elif y == n:
        return c_n1 - 2*n - (n - x)
    elif x == -n:
        return c_n1 - 4*n - (n - y)
    elif y == -n:
        return c_n1 - 6*n - (n + x)

def move_coord(piece):
    #returns coordinates of possible moves
    moves  = {Point(piece.current.x + piece.di, piece.current.y + piece.dj), 
              Point(piece.current.x + piece.dj, piece.current.y + piece.di), 
              Point(piece.current.x - piece.di, piece.current.y + piece.dj),
              Point(piece.current.x - piece.dj, piece.current.y + piece.di),
              Point(piece.current.x + piece.di, piece.current.y - piece.dj),
              Point(piece.current.x + piece.dj, piece.current.y - piece.di),
              Point(piece.current.x - piece.di, piece.current.y - piece.dj),
              Point(piece.current.x - piece.dj, piece.current.y - piece.di)}
    return moves

def move_values(moves):
    #takes move coordinates and returns the values of the squares
    values = {spiral_cell(p.x, p.y) for p in moves}
    return values

def move(piece):
    #takes a piece
    #returns the point the piece moves to as defined: lowest value of a square not visited
    movec = move_coord(piece)
    #set operations are fast as fuck!
    valid = movec - movec.intersection(piece.visited) #valid contains only coordinates that have not been visited
    
    values = [(j, spiral_cell(j.x, j.y)) for j in valid]
    lv =  sorted(values, key=lambda e : e[1]) [0]
    return lv

def simulate(piece):
    try:
        next_move = move(piece)
        piece.current = next_move[0]
        piece.visited.add(next_move[0])
        return True
    except IndexError:
        return False

#testing spiral grid
def test_spiral_grid():
    square = sys.argv[1]
    u,v = -int(square), int(square)+1

    dl_board = [[spiral_cell(x,-y)   for x in range(u, v, 1)] for y in range(u, v, 1)]
    #dr_board = [[spiral_cell(-x, -y) for x in range(u, v, 1)] for y in range(u, v, 1)]
    #ul_board = [[spiral_cell(x,y)    for x in range(u, v, 1)] for y in range(u, v, 1)]
    #lu_board = [[spiral_cell(x,y)    for y in range(u, v, 1)] for x in range(u, v, 1)]
    #ld_board = [[spiral_cell(-x,y)   for y in range(u, v, 1)] for x in range(u, v, 1)]

    for row in dl_board:
        print "\t".join(str(i) for i in row)


#testing simulation

#starting values

di, dj = int(sys.argv[1]), int(sys.argv[2])
k = Piece(di=di, dj=dj)
N=0

progress = [(k.current.x, k.current.y)]

print N, k.current, spiral_cell(k.current.x, k.current.y)

#loop until knight is trapped
while simulate(k):
    N+=1
    progress.append((k.current.x, k.current.y))
    print N, k.current, spiral_cell(k.current.x, k.current.y)

#create plot
progress = zip(*progress)
x, y = progress[0], progress[1]
lx = len(x)

ax = plt.subplot(111)
colors = [i*1.0/lx for i in range(lx)]

#ax.set_prop_cycle('color', [i*1.0/lx for i in range(lx)])
ax.plot(x, y)
plt.show()
