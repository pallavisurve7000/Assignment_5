# square numbers & their sums

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self.x **= 2
        self.y **= 2
        self.z **= 2
        return(self.x+self.y+self.z)

x = int(input("square sum of first number :"))
y = int(input("square sum of second number :"))
z = int(input("square sum of third number :"))
point = Point(x,y,z)
res = point.sqSum()
print(f"The sum of square is : {res}")