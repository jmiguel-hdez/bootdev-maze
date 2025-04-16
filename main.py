from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze"
        self.canvas = Canvas(master=self.__root, height=height, width=width)
        self.canvas.pack()
        self._running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self._running = True
        while(self._running):
            self.redraw()
    
    def close(self):
        self._running = False

def main():
    win = Window(800,600)
    win.wait_for_close()


if __name__ == "__main__":
    main()