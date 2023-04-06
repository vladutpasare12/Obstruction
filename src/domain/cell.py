import pygame


class Cell:

    def __init__(self, row, column, current_state):

        self.__row = row
        self.__column = column
        self.__state = current_state

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    @property
    def state(self):
        return str(self.__state)

    @state.setter
    def state(self, new_state: str):
        self.__state = new_state
