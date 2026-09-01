"""
This module contains 3 functions to determine if a triangle is equilateral,
isosceles, or scalene.

The first approach was a true brute force. It was not very pythonic. There were multiple chains of conditions and one-off edge case handling. This led me to create the is_triangle helper function. This was also brute force at first. Then I did some research and found out I could define a, b, c then iterate through them in a list comprehension. 

After this I kept getting tripped up on isosceles and scalene edge cases. I googled, "python scalene triangle" and it mentioned using a set. I couldn't do that with my first version because I was defining the sides like this:
a = sides[0]
b = sides[1]
c = sides[2]

nothing to see here, just programming python like it's java or c. 

I recently took Harvard CS50 where I used sets to store unique values. The scalene answer made sense. If the triangle is valid and the length of the set is 3 then it must be scalene. 
"""
def is_triangle(sides):
    """
    helper function to identify valid triangles
    """
    a, b, c = sides

    return all(side > 0 for side in sides) and (
        a + b > c and a + c > b and b + c > a
    )
    
def equilateral(sides):
    """
    function to determine if a triangle is equilateral
    """
    side_count = len(set(sides))
    if not is_triangle(sides):
        return False
        
    if side_count == 1:
        return True
    return False

def isosceles(sides):
    """
    function to determine if a triangle is isosceles
    """
    side_count = len(set(sides))
    if not is_triangle(sides):
        return False
        
    if side_count == 2 or equilateral(sides):
        return True
    return False

def scalene(sides):
    """
    function to determine if a triangle is scalene
    """    
    side_count = len(set(sides))

    if side_count == 3 and is_triangle(sides):
        return True
    return False
