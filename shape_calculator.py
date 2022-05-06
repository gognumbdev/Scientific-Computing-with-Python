class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,size):
        self.width = size

    def set_height(self,size):
        self.height = size

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*self.width+2*self.height
    
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5
    
    def get_picture(self):
        width = self.width
        height = self.height
        if width > 50 or height > 50 :
            return "Too big for picture."
        lines = [ ("*"*width)+"\n" for i in range(height)]
        return "".join(lines)

    def get_amount_inside(self,another_shape):
        return self.get_area() // (another_shape.get_area())

    def __str__(self):
        return "Rectangle(width={width}, height={height})".format(width=self.width,height=self.height)

class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)

    def set_side(self,size):
        self.width = size
        self.height = size
    
    def set_width(self,size):
        self.width = size
        self.height = size

    def set_height(self,size):
        self.width = size
        self.height = size

    def __str__(self):
        return "Square(side={size})".format(size=self.width)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))