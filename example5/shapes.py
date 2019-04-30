class Circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        return (self.r**2)*3.14
    
    def perimeter(self):
        return (2*self.r)*3.14

class Square:

    def __init__(self,s):
        self.s=s

    def area(self):
        return self.area(s*s)

    def perimeter(self):
        return self.perimeter(s+s+s+s)


class Rectangle:

    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.area(l*w)

    def perimeter(self):
        return 2*self.perimeter(l+w)


class Sphere:

    def __init__(self,r):
        self.r=r


    def area(self):
        return self.r**3.14*4

    def volume(self):
        return self.r**3.14*4/3











    