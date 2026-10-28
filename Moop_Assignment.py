class square:
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length * self.side_length
    def perimeter (self):
        return self.side_length * 4 

my_square = square int(input("Enter Sidelength"))
print ("The area of the square is", my_square.area ())
print ("The perimeter of the square is" my_square.perimeter ())