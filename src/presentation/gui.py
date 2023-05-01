import pygame
from services.service import Service
from presentation.board_gui import BoardGUI
from pygame.locals import *
import time


class GUI:
    BACKGROUND_COLOR = (255, 255, 255)
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    WINDOW_CAPTION = "Obstruction"

    def __init__(self, board: BoardGUI, services: Service):
        """window initialization"""
        pygame.init()
        pygame.display.set_caption(self.WINDOW_CAPTION)
        self.__window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.__window.fill(self.BACKGROUND_COLOR)
        self.__board = board
        self.__score = 0
        self.__services = services
        self.__font = pygame.font.SysFont("newyork", 20)
        self.__score_text_color = (0, 0, 0)
        self.__score_background_color = (255, 255, 255)

    def __call__(self):

        running = True
        turn = "player"

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                self.__text = self.__font.render(f'Score: {self.__score}', True, self.__score_text_color,
                                                 self.__score_background_color)

                if self.__services.no_free_cell():
                    if turn == "player":
                        if self.__score > 0:
                            self.__score -= 1
                        win_message = pygame.image.load("assets/you_lost_message.png")
                        self.__window.blit(win_message, (180, 60))
                        self.__board.draw(self.__window)

                    else:
                        self.__score += 1
                        win_message = pygame.image.load("assets/win_message.png")
                        self.__window.blit(win_message, (180, 60))
                        self.__board.draw(self.__window)
                        
                    pygame.display.update()
                    time.sleep(1)
                    color = (255, 255, 255)
                    
                    pygame.draw.rect(self.__window, color, (180, 60, 250, 80))
                    self.__services.reset_game_board()

                elif turn == "computer":
                    self.__services.computer_move()
                    turn = "player"

                else:
                    if event.type == MOUSEBUTTONDOWN:
                        y, x = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

                        if self.__services.click_on_game_board(x, y, self.__board.board_top, self.__board.height, self.__board.board_left, self.__board.width):
                            row = self.__services.get_row(x, self.__board.board_top)
                            column = self.__services.get_column(y, self.__board.board_left)

                            if self.__services.get_cell_state(row, column) == "free":
                                self.__services.update_cell_state(row, column, "x")
                                self.__services.set_blocks(row, column)
                                turn = "computer"

                self.__window.blit(self.__text, (500, 20))
                self.__board.draw(self.__window)
                pygame.display.update()

        pygame.quit()
