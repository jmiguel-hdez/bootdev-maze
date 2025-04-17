from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(master=self.__root,bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self._running = True
        while(self._running):
            self.redraw()
        print("window closed...")
    
    def close(self):
        self._running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color=fill_color)
    

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width = 2)

class Cell():
    def __init__(self, x1, y1, x2, y2, win:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
    
    def draw(self):
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)))
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)))



