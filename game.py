import pygame
import spritesheet as ss
import board as b

class Game(object):
    def __init__(self, width, height, row, col, mines, sprite_sheet):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.mines = mines
        self.sprite_sheet = ss.SpriteSheet(sprite_sheet)

    # Get Sprites From The Sprite Sheet
    def get_sprites(self):
        self.sprites = []
        for frame in range(12):
            self.sprites.append(self.sprite_sheet.get_sprite(frame, 16, 16, 2))

    # Draw And Update The Window
    def draw(self):
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                # Checking And Drawing All Squares
                if self.board.board[r][c].clicked and self.board.board[r][c].mine:
                    self.window.blit(self.sprites[2], (c * 32, r * 32))
                elif self.board.board[r][c].flagged:
                    self.window.blit(self.sprites[1], (c * 32, r * 32))
                elif not self.board.board[r][c].clicked:
                    self.window.blit(self.sprites[0], (c * 32, r * 32))
                elif self.board.board[r][c].clicked:
                    self.window.blit(self.sprites[self.board.board[r][c].mine_count + 3], (c * 32, r * 32))
                
        pygame.display.update() # Update Window

    # Mainloop
    def mainloop(self):
        self.board = b.Board(self.row, self.col, self.mines)
        self.board.setBoard()

        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("MineSweeper")

        # Event Handler
        running = True
        fclicked = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit The Game
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and (not self.board.finished):
                    # Detect Row And Column
                    crow = pygame.mouse.get_pos()[1] // 32
                    ccol = pygame.mouse.get_pos()[0] // 32
                    # Pick First Square And Generate Mines
                    if not fclicked:
                        self.board.setMines(crow, ccol)
                        fclicked = True
                    # Pick A Square
                    if pygame.mouse.get_pressed()[0] and not self.board.board[crow][ccol].flagged and not self.board.board[crow][ccol].clicked:
                        self.board.click(crow, ccol)
                        self.board.checkWin()
                    # Flag Square
                    elif pygame.mouse.get_pressed()[2] and not self.board.board[crow][ccol].clicked:
                        self.board.board[crow][ccol].flagged = not self.board.board[crow][ccol].flagged
                    
            self.draw()
        pygame.quit()

game = Game(288, 288, 9, 9, 10, pygame.image.load("spritesheet.png"))
game.get_sprites()
game.mainloop()