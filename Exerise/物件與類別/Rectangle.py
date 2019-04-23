class Rectangle:
    def __init__(self,width=1,height=1):
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return 2*(self.width+self.height)
    
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

def main():
    rec1 = Rectangle()
    print("寬度",rec1.width,"高度",rec1.height,"面積",rec1.getArea(),
    "周長",rec1.getPerimeter())
    
    rec2 = Rectangle(4,40)
    print("寬度",rec2.getWidth(),"高度",rec2.getHeight(),"面積",rec2.getArea(),
    "周長",rec2.getPerimeter())

    rec3 = Rectangle(3.5,35.7)
    print("寬度",rec3.getWidth(),"高度",rec3.getHeight(),"面積",rec3.getArea(),
    "周長",rec3.getPerimeter())

if __name__ == "__main__":
    main()