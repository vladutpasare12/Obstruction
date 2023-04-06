from presentation.gui import GUI
from services.service import Service
from domain.board import GameBoard
from presentation.board_gui import BoardGUI

if __name__ == '__main__':
    game_board = GameBoard()
    services = Service(game_board)
    board_ui = BoardGUI(0, 0, 400, 400, services)
    gui = GUI(board_ui, services)
    gui()


