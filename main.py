from cell import Cell
from graphics import Window
from graphics import Line,Point
from maze import Maze

def main():
    win = Window(800,600)

    m = Maze(10,10,10,10,20,20,win)
    m._create_cells()
    m._break_entrance_and_exit()

    c5 = Cell(win)
    c5.has_left_wall = False
    c5.draw(300, 300, 500, 500)

    c6 = Cell(win)
    c6.has_right_wall = False
    c6.draw(510, 510, 600, 600)

    c5.draw_move(c6,False)

    win.wait_for_close()


if __name__ == "__main__":
    main()