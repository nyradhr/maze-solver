from window import Window
from geometry import Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    #add some cells and draw them
    cell_1 = Cell(win)
    cell_1.has_bottom_wall = False
    cell_1.draw(30, 30, 70, 70)
    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.draw(55, 55, 130, 130)
    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.draw(350, 350, 600, 600)

    win.wait_for_close()

main()