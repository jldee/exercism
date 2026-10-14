"""
An application to make sure brackets are all closed
"""
def is_paired(input_string):
    """
    input(str): input string
    return(bool): are the brackets all closed?
    """
    bracket_map = {')' : '(', '}' : '{', ']' : '['}
    stack = []

    for char in input_string:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
    if stack:
        return False
    else:
        return True
