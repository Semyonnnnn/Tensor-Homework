from math import pi

class Rectangle():
    def area(self, a, b):
        result = a * b
        return result
    
    
class Circle():
    def area(self, r):
        result = pi * (r^2)
        return result


class Triangle():
    def area(self, h, b):
        result = (h*b)/2
        return result


# Класс с наследованием 
class Parallelepiped(Rectangle):
    def area3d(self, a, b, c):
        result3d = self.area(a, b) * c
        return result3d

class Sphere(Circle):
    def area3d(self, r):
        result3d = self.area(r) * 4
        return result3d
