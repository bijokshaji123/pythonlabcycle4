class rectangle:
  def __init__(self):
     self._length=int(input("Enter the length:"))
     self._breadth=int(input("Enter the breadth:"))
     self.area=self._length*self._breadth
  def greaterThan(self,rectangle):
    if self.area<rectangle.area:
        print("Area of rectanglre 1 is greater")
    else:
        print("Area of rectangle 2 is greater")
print("Rectangle 1:")
r1 = rectangle()
print("Rectangle 2:")
r2 = rectangle()
print("comparing rectangles:")
r2.greaterThan(r1)
