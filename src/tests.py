import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    
    def test_maze_create_cells_no_win(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_with_win(self): #this opens a window and draws the maze
        win = Window(400, 300)
        num_cols = 15
        num_rows = 15
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()