from geometry import Point, Line

class Cell:

    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2): #(x1, y1) is top left, (x2, y2) is bottom right
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        self._draw_wall(line, self.has_left_wall)
        line = Line(Point(x2, y1), Point(x2, y2))
        self._draw_wall(line, self.has_right_wall)
        line = Line(Point(x1, y1), Point(x2, y1))
        self._draw_wall(line, self.has_top_wall)
        line = Line(Point(x1, y2), Point(x2, y2))
        self._draw_wall(line, self.has_bottom_wall)

    def _draw_wall(self, line, has_wall):
        self._win.draw_line(line) if has_wall else self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        from_center = Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)
        to_center = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        line = Line(from_center, to_center)
        self._win.draw_line(line, color)