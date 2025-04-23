import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells_num_rows_cols(self):
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

    def test_maze_create_cells_num_rows_cols_0(self):
        num_cols = 0
        num_rows = 0
        create_maze = lambda: Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertRaises(
            ValueError,
            create_maze,
        )

    def test_maze_create_cells_coordinates(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 10, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._x1,
            20,
        )
        self.assertEqual(
            m1._y1,
            10,
        )

    def test_maze_create_cells_size(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 10, num_rows, num_cols, 10, 20)
        self.assertEqual(
            m1._cell_size_x,
            10,
        )
        self.assertEqual(
            m1._cell_size_y,
            20,
        )

    def test_maze_create_cells_win_default(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 10, num_rows, num_cols, 10, 20)
        self.assertEqual(
            m1._win,
            None,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 10, num_rows, num_cols, 10, 20)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 10, num_rows, num_cols, 10, 20)
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                m1._cells[i][j].visited = True
        m1._reset_cells_visited()

        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()
