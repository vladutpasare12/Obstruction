from domain.board import GameBoard


class Service:
    def __init__(self, board: GameBoard):
        self.__board = board

    def get_board(self):
        # change self.board.board, it doesn't look good
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

    def no_free_cell(self):
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if self.__board.get_cell_state(row, column) == "free":
                    return False
        return True

    def reset_game_board(self):
        self.__board.clear_board()
