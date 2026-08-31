"""
This Module tests if a number will reach 1 using the Collatz Conjecture
"""
def steps(number):
    """
    run each number through the Collatz Conjecture until it reaches 1.
    
    input int: number to be tested
    return int: the number of steps it takes
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1
    return count
