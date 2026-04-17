from abc import ABC, abstractmethod
import math


class Figure(ABC):
    side:int

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass






class Circle(Figure):
    def __init__(self, side):
        self.side = side

    def square(self):
        s = math.pi * 2 ** self.side
        return s
    
    def perimeter(self):
        s = math.pi * 2 * self.side
        return s
    


class Triangle(Figure):
    def __init__(self, side):
        self.side = side

    def square(self):
        s = math.pi * 2 ** self.side
        return s
    
    def perimeter(self):
        s = math.pi * 2 * self.side
        return s
    


class Trapezoid(Figure):
    def __init__(self, side):
        self.side = side

    def square(self):
        s = math.pi * 2 ** self.side
        return s
    
    def perimeter(self):
        s = math.pi * 2 * self.side
        return s
    


class Rectangle(Figure):
    def __init__(self, side, width):
        self.side = side
        self.width = width

    def square(self):
        s = self.width * self.side
        return s
    
    def perimeter(self):
        s = 2 * (self.side + self.width)
        return s



# cir = Circle(5)
# tri = Triangle(6)
# tra = Trapezoid(7)
rec = Rectangle(8, 5)


# def func_1(a,b,c,d):
#     summa = a.square() + b.square() + c.square() + d.square()
#     return summa

# def func_2(a,b,c,d):
#     summa = a.perimeter() + b.perimeter() + c.perimeter() + d.perimeter()
#     return summa



# a_1 = func_1(cir, cir, cir, cir)
# a_2 = func_1(cir, rec, cir, tri)
# b = func_2(cir, tri, tra, rec)

# print(a_1)
# print(a_2)
# print(b)