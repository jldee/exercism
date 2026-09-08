"""
Translate
"""
def translate(text):
    """translate function
    Pig Latin translation
    """
    vowels = 'aeiou'
    xryt_strings = ['xr', 'yt']

    def translate_word(word):
        if word[0] in vowels or word[:2] in xryt_strings:
            return word + 'ay'
        i = 0
        
        while i < len(word) and word[i] not in vowels:
            if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                i += 2
            elif word[i] == 'y' and i > 0:
                break
            else:
                i += 1
        return word[i:] + word[:i] + 'ay'

    return ' '.join(translate_word(word) for word in text.split())
