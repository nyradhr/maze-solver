class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
class Line:

    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    #fill_color is a string (e.g. "black" or "red")
    def draw(self, canvas, fill_color):
        x1 = self.__point_1.x
        y1 = self.__point_1.y
        x2 = self.__point_2.x
        y2 = self.__point_2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

    