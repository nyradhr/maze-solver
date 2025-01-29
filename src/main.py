from window import Window
from geometry import Point, Line

def main():
    win = Window(800, 600)
    #drawing some lines to test newly created Point and Line classes
    line_1 = Line(Point(0,0), Point(30,60))
    line_2 = Line(Point(50,0), Point(50,100))
    win.draw_line(line_1, "blue")
    win.draw_line(line_2, "red")
    win.wait_for_close()

main()