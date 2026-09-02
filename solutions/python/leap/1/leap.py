"""
Method to determine if a year is a leap year
"""
def leap_year(year):
    """
    Function to determine if a year is a leap year.

    input (int): year
    return (bool)
    """
    if year < 4:
        raise ValueError("We need more time...")

    return (
        True if (year % 400 == 0 and year % 100 == 0) 
        else True if (year % 4 == 0 and year % 100 != 0) 
        else False 
    )
