def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    doubling = 2 ** (number - 1)
    return doubling

def total():
    total_doubled = 2 ** 64 - 1
    return total_doubled  

"""
1 1
2 2
3 4
4 8
5 16
6 32
7 64
8 128
9 256



"""