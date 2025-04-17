from graphics import Window
from graphics import Line,Point

def main():
    win = Window(800,600)
    p1 = Point(0,0)
    p2 = Point(800,600)
    line = Line(p1, p2)
    win.draw_line(line,"red")
    p1 = Point(0,600)
    p2 = Point(800,0)
    line = Line(p1, p2)
    win.draw_line(line,"black")
    win.wait_for_close()


if __name__ == "__main__":
    main()