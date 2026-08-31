def is_armstrong_number(number):
    """
    A function to determine if a number is an armstrong number.
    
    Input: int
    
    Return: bool
    
    Check if a number is an Armstrong number by summing each digit raised to the power of         the length of the number. 
    """
    if number < 0:
        raise ValueError("Number must be an integer")
    string_num = str(number)
    length = len(string_num)
    total = 0
    for char in string_num:
        digit = int(char)
        total += digit ** length
    if total == number:
        return True
    return False
