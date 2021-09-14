### Original Point classes
class Point:
    color = 'blue'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def str(self):
        return '(x=%d, y=%d)' % (self.x, self.y)

    def prt(self):
        print(self.str())

    def shift(self, number):
        self.x += number
        self.y += number

    def eq(self, other):
        return self.x == other.x  and  self.y == other.y

class ColorPoint(Point):
    color = 'red'

    def str(self):
        return Point.str(self) + ' [color = %s]' % self.color

p = Point(1, 2)
q = ColorPoint(3, 4)
q2 = ColorPoint(5, 6)
p.prt()
q.prt()
p.shift(3)
p.prt()
print(q.eq(q))
q.color = 'green'
q.prt()
q2.prt()
