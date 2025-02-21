from cell import Cell
from time import sleep
from random import seed, randrange


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed_num=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window
        if seed_num:
            seed(seed_num)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
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
        x2 = ((col + 1) * self.cell_size_x) + self.x1
        y2 = ((row + 1) * self.cell_size_y) + self.y1
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

    def _get_available_directions(self, col, row):
        directions = []
        if row + 1 < self.num_rows:
            if not self._cells[col][row + 1].visited:
                directions.append((col, row + 1)) #down
        if col + 1 < self.num_cols:
            if not self._cells[col + 1][row].visited:
                directions.append((col + 1, row)) #right
        if row > 0:
            if not self._cells[col][row - 1].visited:
                directions.append((col, row - 1)) #up
        if col > 0:
            if not self._cells[col - 1][row].visited:
                directions.append((col - 1, row)) #left
        return directions

    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        to_visit = self._get_available_directions(col, row)
        while(to_visit):
            visit_index = randrange(0, len(to_visit))
            direction = to_visit[visit_index]
            if direction[1] > row:
                self._cells[col][row].has_bottom_wall = False
                self._cells[col][row + 1].has_top_wall = False
            elif direction[0] > col:
                self._cells[col][row].has_right_wall = False
                self._cells[col + 1][row].has_left_wall = False
            elif direction[1] < row:
                self._cells[col][row].has_top_wall = False
                self._cells[col][row - 1].has_bottom_wall = False
            elif direction[0] < col:
                self._cells[col][row].has_left_wall = False
                self._cells[col - 1][row].has_right_wall = False
            self._break_walls_r(direction[0], direction[1])
            to_visit = self._get_available_directions(col, row)
        self._draw_cell(col, row)

    def _reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._cells[col][row].visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, col, row):
        self._animate()
        self._cells[col][row].visited = True
        if col == self.num_cols-1 and row == self.num_rows - 1:
            return True
        directions = self._get_available_directions(col, row)
        for direction in directions:
            if (self._has_path_between(col, row, direction[0], direction[1])):
                self._cells[col][row].draw_move(self._cells[direction[0]][direction[1]])
                solved = self._solve_r(direction[0], direction[1])
                if solved:
                    return True
                else:
                    self._cells[col][row].draw_move(self._cells[direction[0]][direction[1]], True) #undo
        return False
    
    def _has_path_between(self, current_col, current_row, next_col, next_row):
            if next_row > current_row:
                return not self._cells[current_col][current_row].has_bottom_wall
            elif next_col > current_col:
                return not self._cells[current_col][current_row].has_right_wall
            elif next_row < current_row:
                return not self._cells[current_col][current_row].has_top_wall
            elif next_col < current_col:
                return not self._cells[current_col][current_row].has_left_wall