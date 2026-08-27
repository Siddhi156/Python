class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        print("Area:",self.length * self.breadth)

r = rectangle = Area(5,10)
r.calculate_area()
