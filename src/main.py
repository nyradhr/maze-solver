from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(30, 30, 8, 10, 30, 30, win)
    maze.solve()
    win.wait_for_close()

main()