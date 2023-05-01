from domain.board import GameBoard
import random


class Service:

    NEIGHBOUR_ROW_DIFFERENCE = [-1, -1, -1, 0, 0, 1, 1, 1]
    NEIGHBOUR_COLUMN_DIFFERENCE = [-1, 0, 1, -1, 1, -1, 0, 1]

    def __init__(self, board: GameBoard):
        self.__board = board

    def get_board(self):
        return self.__board.board

    def get_cell_state(self, row, column):
        return self.__board.get_cell_state(row, column)

    def update_cell_state(self, row, column, new_state):
        self.__board.update_cell_state(row, column, new_state)

    @staticmethod
    def click_on_game_board(x, y, board_top, board_height, board_left, board_width):
        if board_top <= x <= board_top + board_height and board_left <= y <= board_left + board_width:
            return True
        return False

    @staticmethod
    def get_row(x, board_top):
        return (x - board_top) // 50

    @staticmethod
    def get_column(y, board_left):
        return (y - board_left) // 50

    def set_blocks(self, row, column):

        for i in range(8):
            neighbor_row = row + self.NEIGHBOUR_ROW_DIFFERENCE[i]
            neighbor_column = column + self.NEIGHBOUR_COLUMN_DIFFERENCE[i]
            if 0 <= neighbor_row <= 7 and 0 <= neighbor_column <= 7 and self.get_cell_state(neighbor_row,
                                                                                                       neighbor_column) == "free":
                self.update_cell_state(neighbor_row, neighbor_column, "block")

    def no_free_cell(self):
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if self.__board.get_cell_state(row, column) == "free":
                    return False
        return True

    def reset_game_board(self):
        self.__board.clear_board()

    def computer_move(self):

        free_cells = []

        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if self.__board.get_cell_state(row, column) == "free":
                    free_cells.append((row, column))

        if not free_cells:
            return False

        cell = random.choice(free_cells)
        self.update_cell_state(cell[0], cell[1], "o")
        self.set_blocks(cell[0], cell[1])
        return True
