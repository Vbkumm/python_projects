class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1)**2 + (y1 - y2)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())

class Cylinder:

    def __init__(self, height=1, radius=1, pi = 3.14):
        self.height = height
        self.radius = radius
        self.pi = pi

    
    def volume(self):
        radius = self.radius
        height = self.height
        pi = self.pi
        return pi * radius * radius * height
    
    def surface_area(self):
        radius = self.radius
        height = self.height
        pi = self.pi
        return 2 * pi * radius * (radius + height)
    

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())