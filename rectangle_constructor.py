class Rectangle:
    def __init__(self,l,w):
         self.length = l 
         self.width = w
    def Rectangle_area(self):
        return self.length*self.width 
newRectangle = Rectangle(10 , 12)
print(newRectangle.Rectangle_area())