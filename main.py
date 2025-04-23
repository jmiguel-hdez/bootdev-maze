from cell import Cell
from graphics import Window
from graphics import Line,Point
from maze import Maze

def main():
    win = Window(800,600)

    m = Maze(10,10,10,10,20,20,win)
    m._create_cells()
    m.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()