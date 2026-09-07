""" 
Method to describe how Bob responds using conditionals.
"""
def response(hey_bob):
    sure = "Sure."
    chill = "Whoa, chill out!"
    calm = "Calm down, I know what I'm doing!"
    fine = "Fine. Be that way!"
    wtvr = "Whatever."
    odd_spacing = ['\r', '\t']

    if hey_bob == "" or hey_bob == None or (hey_bob[0] == " " and hey_bob[-1] == " ") or any(space in hey_bob for space in odd_spacing):
        return fine
    elif hey_bob[-1] == '?' and hey_bob == hey_bob.upper() and hey_bob[0].isalpha():
        return calm        
    elif hey_bob == hey_bob.upper() and hey_bob[-1] != '?' and any(char.isalpha() for char in hey_bob): 
        return chill
    elif hey_bob[-1] == '?' or (hey_bob[-1] == " " and "?" in hey_bob):
        return sure
    else: 
        return wtvr