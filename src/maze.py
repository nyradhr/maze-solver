from cell import Cell
from time import sleep


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        self._cells = [[Cell(self.win) for j in range(self.num_rows)] for i in range(self.num_cols)]
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self.win is None:
            return
        x1 = (col * self.cell_size_x) + self.x1
        y1 = (row * self.cell_size_y) + self.y1
        x2 = ((col+1) * self.cell_size_x) + self.x1
        y2 = ((row+1) * self.cell_size_y) + self.y1
        self._cells[col][row].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        #entrance is always at the top of the top-left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        #exit is always at the bottom of the bottom-right cell
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)