"""
Solution for raindrops, a more complicated fizz/buzz. 
"""

DROPS = ("i", 3), ("a", 5), ("o", 7)

def convert(number):
    """
    Convert a number to the matching string value
    """
    return "".join(f"Pl{i}ng" for i, v in DROPS if not number % v) or str(number)
    # pling = 'Pling'
    # plang = 'Plang'
    # plong = 'Plong'
    # result = ""
    
    # if number % 3 == 0:
    #     result += pling

    # if number % 5 == 0:
    #     result += plang

    # if number % 7 == 0:
    #     result += plong

    # if result == "":
    #     result += str(number)

    # return result"""