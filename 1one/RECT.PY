class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.breadth + other.breadth)

    def __str__(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"

    def compare(self, other):
        if self.length == other.length and self.breadth == other.breadth:
            print("Rectangles are equal")
        elif self.length * self.breadth < other.length * other.breadth:
            print("r1 is smaller than r2")
        else:
            print("r1 is greater than r2")


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 6)

# Adding two rectangles
r3 = r1 + r2

# Printing the result
print(r3)

# Comparing dimensions
r1.compare(r2)
