from random import randrange
import piece as p

class Board(object):
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.clicked_squares = 0
        self.finished = False

    # Create A Board In 2D Array
    def setBoard(self):
        self.board = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                piece = p.Piece()
                row.append(piece)
            self.board.append(row)

    # Select Random Mine Locations And Assign Them
    def setMines(self, r, c):
        firstNine = [(r, c)]
        firstNine += self.getNeighbors(r, c)
        self.mine_pos = set()
        while len(self.mine_pos) < self.mines:
            row = randrange(0, self.rows)
            col = randrange(0, self.cols)

            if (row, col) in self.mine_pos or ((row, col) in firstNine):
                continue

            self.mine_pos.add((row, col))
            self.board[row][col].mine = True

    # Count The Mines Around A Square
    # And Store Them In A List
    def getNeighbors(self, row, col):
        neighbors = []

        if row > 0: # TOP
            neighbors.append((row - 1, col))
        if row < self.rows - 1: # BOTTOM
            neighbors.append((row + 1, col))
        if col > 0: # LEFT
            neighbors.append((row, col - 1))
        if col < self.cols - 1: # RIGHT
            neighbors.append((row, col + 1))

        if row > 0 and col > 0: # TOP LEFT
            neighbors.append((row - 1, col - 1))
        if row > 0 and col < self.cols - 1: # TOP RIGHT
            neighbors.append((row - 1, col + 1))
        if row < self.rows - 1 and col > 0: # BOTTOM LEFT
            neighbors.append((row + 1, col - 1))
        if row < self.rows - 1 and col < self.cols - 1: # BOTTOM RIGHT
            neighbors.append((row + 1, col + 1))

        return neighbors

    # Click A Square On The Board
    def click(self, row, col):
        if self.board[row][col].clicked: # Check If The Square Is Already Clicked
            return None
        self.board[row][col].clicked = True # Mark The Square Clicked
        if self.board[row][col].mine: # Check If Clicked Square Has A Mine
            for r, c in self.mine_pos:
                self.board[r][c].clicked = True
                self.board[r][c].flagged = False
            print("Lost")
            self.finished = True
            return None
        
        self.clicked_squares += 1
        # Count The Mines Around The Square
        neighbors = self.getNeighbors(row, col)
        for r, c in neighbors:
            if self.board[r][c].mine == True:
                self.board[row][col].mine_count += 1

        # If Mine Count Is 0 Check The Neighbors
        if self.board[row][col].mine_count == 0:
            for r, c in neighbors:
                self.click(r, c)
    
    # Check If All The Squares Are Clicked
    def checkWin(self):
        if self.clicked_squares == (self.rows * self.cols) - self.mines:
            self.finished = True
            print("Won")