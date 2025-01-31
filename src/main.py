from window import Window
#from geometry import Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    #add some cells and draw them
    cell_1 = Cell(win)
    cell_1.has_bottom_wall = False
    cell_1.draw(30, 30, 70, 70)
    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.draw(155, 155, 230, 230)
    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.draw(150, 350, 400, 600)

    cell_4 = Cell(win)
    cell_4.draw(350, 200, 650, 500)

    #let's try drawing a line from a cell to another
    cell_1.draw_move(cell_3, True) 

    cell_2.draw_move(cell_4) #undo=False as default

    win.wait_for_close()

main()