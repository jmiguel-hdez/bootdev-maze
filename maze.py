from cell import Cell
from typing import List
from graphics import Window
import time
import random

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
            seed = None,
    ):
        if num_rows < 1 or num_cols < 1:
            raise ValueError("need at least one row and col for maze")
        
        if seed:
            random.seed(seed)

        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window = win
        self._cells: List[List[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
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
    
    def _break_entrance_and_exit(self):
        entry_col = 0
        entry_row = 0
        self._cells[entry_col][entry_row].has_top_wall = False
        self._draw_cell(entry_col,entry_row)

        exit_col = self._num_cols - 1
        exit_row = self._num_rows - 1
        self._cells[exit_col][exit_row].has_bottom_wall = False
        self._draw_cell(exit_col,exit_row)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while(True):
            to_visit = []
            if i >= 1:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1,j))
            if i < self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1,j))
            if j >= 1:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i,j-1))
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i,j+1))
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            cell_to_visit_index = random.randrange(0,len(to_visit))
            cell_to_visit = to_visit[cell_to_visit_index]
            if cell_to_visit == (i-1,j):
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif cell_to_visit == (i+1,j):
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif cell_to_visit == (i,j-1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            else:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._break_walls_r(cell_to_visit[0],cell_to_visit[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self,i:int, j:int) -> bool:
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows - 1:
            return True
        
        #left
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            ret = self._solve_r(i-1,j)
            if ret:
                return True
            #Draw undo
            self._cells[i][j].draw_move(self._cells[i-1][j],True)
        #right 
        if  i < self._num_cols - 1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            ret = self._solve_r(i+1,j)
            if ret:
                return True
            #Draw undo
            self._cells[i][j].draw_move(self._cells[i+1][j],True)

        #Up
        if  j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            ret = self._solve_r(i,j-1)
            if ret:
                return True
            #Draw undo
            self._cells[i][j].draw_move(self._cells[i][j-1],True)

        #Down
        if  j < self._num_rows - 1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            ret = self._solve_r(i,j+1)
            if ret:
                return True
            #Draw undo
            self._cells[i][j].draw_move(self._cells[i][j+1],True)

        
        return False







