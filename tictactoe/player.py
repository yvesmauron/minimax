from abc import ABC
import pygame as pg


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
