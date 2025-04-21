from cell import Cell
from typing import List
from graphics import Window
import time

class Maze():
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window = None,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window = win
        self._cells: List[List[Cell]] = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i: int, j: int):
        if self._win is None:
            return

        if i >= self._num_cols or j >= self._num_rows:
            raise IndexError(f"The provide indices(i:{i} j:{j}) are outside the maze area")

        cell: Cell = self._cells[i][j]
        #Since i represent the column index, when we iterate we increase the x
        x1 = (i * self._cell_size_x) + self._x1
        #Since j represent the row index, when we iterate we increase the y
        y1 = (j * self._cell_size_y) + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

