from domain.cell import Cell


class GameBoard:

    def __init__(self):
        # constants
        self.__CELL_HEIGHT = 50
        self.__CELL_HEIGHT = 50
        self.__rows = 8
        self.__columns = 8

        self.clear_board()

    def clear_board(self):
        """sets all cells to be empty"""

        self.__board = [[], [], [], [], [], [], [], []]
        for row in range(8):
            for column in range(8):
                cell = Cell(0 * self.__CELL_HEIGHT, 0 * self.__CELL_HEIGHT, "free")
                self.__board[row].append(cell)

    def board(self):
        return self.__board

    def get_cell(self, row, column):
        return self.__board[row][column]

    def get_cell_state(self, row, column):
        return self.__board[row][column].state

    def set_cell(self, row, column, new_cell):
        self.__board[row][column] = new_cell

    def update_cell_state(self, row, column, new_state):
        self.__board[row][column].state = new_state

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    def cell_state(self, row, column):
        return str(self.__board[row][column].state)

    def __getitem__(self, row, column):
        return self.__board[row][column]
