def convert(number):
    pling = 'Pling'
    plang = 'Plang'
    plong = 'Plong'
    result = ""
    
    if number % 3 == 0:
        result += pling

    if number % 5 == 0:
        result += plang

    if number % 7 == 0:
        result += plong

    if result == "":
        result += str(number)

    return result