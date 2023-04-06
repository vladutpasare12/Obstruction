import pygame
from services.service import Service


class BoardGUI:
    def __init__(self, position_x, position_y, height, width, service: Service):
        self.__position_x = position_x
        self.__position_y = position_y
        self.__height = height
        self.__width = width
        self.__service = service
        self.__board = service.get_board()
        self.__board_top = 160
        self.__board_left = 100

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__height

    @property
    def board_top(self):
        return self.__board_top

    @property
    def board_left(self):
        return self.__board_left

    def draw(self, window):

        for row in range(8):
            for column in range(8):
                cell_state = self. __service.get_cell_state(row, column)
                cell_image = cell_image = pygame.image.load("assets/free_cell.png")
                if cell_state == "x":
                    cell_image = pygame.image.load("assets/player_cell.png")
                if cell_state == "o":
                    cell_image = pygame.image.load("assets/computer_cell.png")
                if cell_state == "block":
                    cell_image = pygame.image.load("assets/blocked_cell.png")

                window.blit(cell_image, (self.__board_left + column * 50, self.__board_top + row * 50))
