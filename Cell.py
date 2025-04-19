from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            )
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            )

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        c1_center_x = ((self._x2 - self._x1) / 2) + self._x1
        c1_center_y = ((self._y2 - self._y1) / 2) + self._y1
        c1_center = Point(c1_center_x,c1_center_y)

        c2_center_x = ((to_cell._x2 - to_cell._x1) / 2) + to_cell._x1
        c2_center_y = ((to_cell._y2 - to_cell._y1) / 2) + to_cell._y1
        c2_center = Point(c2_center_x,c2_center_y)
        line = Line(c1_center, c2_center)
        self._win.draw_line(line,color)


