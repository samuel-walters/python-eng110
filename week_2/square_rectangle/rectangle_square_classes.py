class Rectangle:
    def __init__(self, width, height):
        if width <= 0:
            self.width = 1
        else:
            self.width = width
        if height <= 0:
            self.height = 1
        else:
            self.height = height    
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return self.width + self.width + self.height + self.height

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)