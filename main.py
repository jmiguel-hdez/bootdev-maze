from graphics import Window
from graphics import Line,Point,Cell

def main():
    win = Window(800,600)
    c1 = Cell(2, 2, 20, 20, win)
    c1.draw()
    c2 = Cell(50,50, 100, 100, win)
    c2.draw()
    c3 = Cell(150, 150, 200, 200, win)
    c3.has_bottom_wall = False
    c3.draw()
    c4 = Cell(210, 210, 260, 260, win)
    c4.has_top_wall = False
    c4.draw()
    c5 = Cell(270, 270, 300, 300, win)
    c5.has_left_wall = False
    c5.draw()
    c5 = Cell(310, 310, 360, 360, win)
    c5.has_right_wall = False
    c5.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()