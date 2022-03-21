"""Python class named Circle constructed by a radius and two methods that will compute the area and the perimeter of a circle."""
from math import pi

class Circle :
    def __init__(self, radius):
        assert radius > 0, 'Radius must be greater than 0'
        self.radius = radius
    def area(self):
        """Returns the area of this circle, which is PI x RADIUS^2."""
        return pi*(self.radius)**2
    def perimeter(self):
        """Returns the perimeter of this circle, which is 2 x PI x RADIUS."""
        return 2*pi*self.radius

# Test
cercle=Circle(8)
print(cercle.perimeter())
print(cercle.area())

#Test Result
# 50.26548245743669
# 201.06192982974676
