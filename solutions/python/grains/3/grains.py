def square(number):
    """Function that returns the value of a geometric doubling series"""
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    doubling = 2 ** (number - 1)
    return doubling

def total():
    """Function that returns the total value of a geometric doubling series that contains 64 values"""
    total_doubled = 2 ** 64 - 1
    return total_doubled  
