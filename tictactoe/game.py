# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *

# declaring the global variables
from abc import ABC


class Player(ABC):

    def __init__(self):
        super().__init__()

    def next_move(self):
        pass


class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def next_move(self):
        # get coordinates of mouse click
        x, y = pg.mouse.get_pos()

        return x, y


class TicTacToe():

    def __init__(self, x_player: Player, o_player: Player):
        super().__init__()

        # for storing the 'x' or 'o'
        # value as character
        self.XO = 'x'

        self.x_player = x_player
        self.o_player = o_player

        # storing the self.winner's value at
        # any instant of code
        self.winner = None

        # to check if the game is a self.draw
        self.draw = None

        # to set self.width of the game window
        self.width = 400

        # to set self.height of the game window
        self.height = 400

        # to set background color of the
        # game window
        self.white = (255, 255, 255)

        # color of the straightlines on that
        # self.white game self.board, dividing self.board
        # into 9 parts
        self.line_color = (0, 0, 0)

        # setting up a 3 * 3 self.board in canvas
        self.board = [[None]*3, [None]*3, [None]*3]

        # initializing the pygame window
        pg.init()

        # setting self.fps manually
        self.fps = 30

        # this is used to track time
        self.clock = pg.time.Clock()

        # this method is used to build the
        # infrastructure of the display
        self.screen = pg.display.set_mode(
            (self.width, self.height + 100), 0, 32)

        # setting up a nametag for the
        # game window
        pg.display.set_caption("My Tic Tac Toe")

        # loading the images as python object
        self.initiating_window = pg.image.load(
            "tictactoe/assets/modified_cover.png")
        self.x_img = pg.image.load("tictactoe/assets/X_modified.png")
        self.o_img = pg.image.load("tictactoe/assets/o_modified.png")

        # resizing images
        self.initiating_window = pg.transform.scale(
            self.initiating_window, (self.width, self.height + 100))
        self.x_img = pg.transform.scale(self.x_img, (80, 80))
        self.o_img = pg.transform.scale(self.o_img, (80, 80))

    def start_game(self):

        # displaying over the self.screen
        self.screen.blit(self.initiating_window, (0, 0))

        # updating the display
        pg.display.update()
        time.sleep(3)
        self.screen.fill(self.white)

        # self.drawing vertical lines
        pg.draw.line(self.screen, self.line_color,
                     (self.width / 3, 0), (self.width / 3, self.height), 7)
        pg.draw.line(self.screen, self.line_color, (self.width /
                                                    3 * 2, 0), (self.width / 3 * 2, self.height), 7)

        # self.drawing horizontal lines
        pg.draw.line(self.screen, self.line_color,
                     (0, self.height / 3), (self.width, self.height / 3), 7)
        pg.draw.line(self.screen, self.line_color, (0, self.height /
                                                    3 * 2), (self.width, self.height / 3 * 2), 7)
        self.draw_status()

    def draw_status(self):

        # getting the global variable self.draw
        # into action

        if self.winner is None:
            message = self.XO.upper() + "'s Turn"
        else:
            message = self.winner.upper() + " won !"
        if self.draw:
            message = "Game draw !"

        # setting a font object
        font = pg.font.Font(None, 30)

        # setting the font properties like
        # color and self.width of the text
        text = font.render(message, 1, (255, 255, 255))

        # copy the rendered message onto the self.board
        # creating a small block at the bottom of the main display
        self.screen.fill((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(self.width / 2, 500-50))
        self.screen.blit(text, text_rect)
        pg.display.update()

    def check_win(self):

        # checking for winning rows
        for row in range(0, 3):
            if((self.board[row][0] == self.board[row][1] == self.board[row][2]) and (self.board[row][0] is not None)):
                self.winner = self.board[row][0]
                pg.draw.line(self.screen, (250, 0, 0),
                             (0, (row + 1)*self.height / 3 - self.height / 6),
                             (self.width, (row + 1) *
                              self.height / 3 - self.height / 6),
                             4)
                break

        # checking for winning columns
        for col in range(0, 3):
            if((self.board[0][col] == self.board[1][col] == self.board[2][col]) and (self.board[0][col] is not None)):
                self.winner = self.board[0][col]
                pg.draw.line(self.screen, (250, 0, 0), ((col + 1) * self.width / 3 - self.width / 6, 0),
                             ((col + 1) * self.width / 3 - self.width / 6, self.height), 4)
                break

        # check for diagonal self.winners
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] is not None):

            # game won diagonally left to right
            self.winner = self.board[0][0]
            pg.draw.line(self.screen, (250, 70, 70),
                         (50, 50), (350, 350), 4)

        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] is not None):

            # game won diagonally right to left
            self.winner = self.board[0][2]
            pg.draw.line(self.screen, (250, 70, 70),
                         (350, 50), (50, 350), 4)

        if(all([all(row) for row in self.board]) and self.winner is None):
            self.draw = True
        self.draw_status()

    def drawXO(self, row, col):

        posy, posx = 0, 0
        # for the first row, the image
        # should be pasted at a x coordinate
        # of 30 from the left margin
        if row == 1:
            posx = 30

        # for the second row, the image
        # should be pasted at a x coordinate
        # of 30 from the game line
        if row == 2:

            # margin or self.width / 3 + 30 from
            # the left margin of the window
            posx = self.width / 3 + 30

        if row == 3:
            posx = self.width / 3 * 2 + 30

        if col == 1:
            posy = 30

        if col == 2:
            posy = self.height / 3 + 30

        if col == 3:
            posy = self.height / 3 * 2 + 30

        # setting up the required self.board
        # value to display
        self.board[row-1][col-1] = self.XO

        if(self.XO == 'x'):

            # pasting x_img over the self.screen
            # at a coordinate position of
            # (pos_y, posx) defined in the
            # above code
            self.screen.blit(self.x_img, (posy, posx))
            self.XO = 'o'

        else:
            self.screen.blit(self.o_img, (posy, posx))
            self.XO = 'x'
        pg.display.update()

    def user_click(self):
        # get coordinates of mouse click
        x, y = self.x_player.next_move() if self.XO == "x" else self.o_player.next_move()

        # get column of mouse click (1-3)
        if(x < self.width / 3):
            col = 1

        elif (x < self.width / 3 * 2):
            col = 2

        elif(x < self.width):
            col = 3

        else:
            col = None

        # get row of mouse click (1-3)
        if(y < self.height / 3):
            row = 1

        elif (y < self.height / 3 * 2):
            row = 2

        elif(y < self.height):
            row = 3

        else:
            row = None

        # after getting the row and col,
        # we need to self.draw the images at
        # the desired positions
        if(row and col and self.board[row-1][col-1] is None):
            self.drawXO(row, col)
            self.check_win()

    def reset_game(self):
        time.sleep(3)
        self.XO = 'x'
        self.draw = False
        self.start_game()
        self.winner = None
        self.board = [[None]*3, [None]*3, [None]*3]


if __name__ == "__main__":

    player_1 = HumanPlayer()
    player_2 = HumanPlayer()
    tictactoe = TicTacToe(player_1, player_2)
    tictactoe.start_game()

    while(True):
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                tictactoe.user_click()
                if(tictactoe.winner or tictactoe.draw):
                    tictactoe.reset_game()
            elif event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
        tictactoe.clock.tick(tictactoe.fps)
