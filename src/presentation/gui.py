import pygame
from services.service import Service
from presentation.board_gui import BoardGUI
from pygame.locals import *


class GUI:
    BACKGROUND_COLOR = (255, 255, 255)
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    WINDOW_CAPTION = "Obstruction"
    NEIGHBOUR_ROW_DIFFERENCE = [-1, -1, -1, 0, 0, 1, 1, 1]
    NEIGHBOUR_COLUMN_DIFFERENCE = [-1, 0, 1, -1, 1, -1, 0, 1]

    def __init__(self, board: BoardGUI, services: Service):
        """window initialization"""
        pygame.init()
        pygame.display.set_caption(self.WINDOW_CAPTION)
        self.__window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.__window.fill(self.BACKGROUND_COLOR)
        self.__board = board
        self.__score = 4
        self.__services = services
        self.__font = pygame.font.SysFont("newyork", 20)
        self.__score_text_color = (0, 0, 0)
        self.__score_background_color = (255, 255, 255)

    def __call__(self):

        running = True
        turn = "player1"

        while running:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("intraaaaa")
                        self.__services.reset_game_board()
                if event.type == pygame.QUIT:
                    running = False
                self.__text = self.__font.render(f'Score: {self.__score}', True, self.__score_text_color,
                                                 self.__score_background_color)

                if event.type == MOUSEBUTTONDOWN:
                    y, x = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

                    if self.__services.click_on_game_board(x, y, self.__board.board_top, self.__board.height, self.__board.board_left, self.__board.width):
                        row = self.__services.get_row(x, self.__board.board_top)
                        column = self.__services.get_column(y, self.__board.board_left)
                        if self.__services.get_cell_state(row, column) == "free":
                            if turn == "player1":
                                self.__services.update_cell_state(row, column, "x")
                                turn = "player2"
                            else:
                                self.__services.update_cell_state(row, column, "o")
                                turn = "player1"

                            for i in range(8):
                                neighbor_row = row + self.NEIGHBOUR_ROW_DIFFERENCE[i]
                                neighbor_column = column + self.NEIGHBOUR_COLUMN_DIFFERENCE[i]
                                if 0 <= neighbor_row <= 7 and 0 <= neighbor_column <= 7 and self.__services.get_cell_state(neighbor_row, neighbor_column) == "free":
                                    self.__services.update_cell_state(neighbor_row, neighbor_column, "block")
                            if self.__services.no_free_cell():
                                if turn == "player1":
                                    self.__score -= 2
                                    print(self.__score)
                                    win_message = pygame.image.load("assets/you_lost_message.png")
                                    self.__window.blit(win_message, (180, 60))
                                else:
                                    self.__score += 1
                                    win_message = pygame.image.load("assets/win_message.png")
                                    self.__window.blit(win_message, (180, 60))
                self.__window.blit(self.__text, (500, 20))
                self.__board.draw(self.__window)
                pygame.display.update()

        pygame.quit()