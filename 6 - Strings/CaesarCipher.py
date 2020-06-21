def caesarCipher(s, k):

    #   Time:   O(N)
    #   Space:  O(N)

    if (s == None or len(s) == 0):
        return s

    newString = []

    for char in s:
        
        #   for lower cases and upper cases => char will change
        if (char.islower()):
            newChar = chr ( ( ord(char) - ord('a') + k ) % 26 + ord('a'))
        elif (char.isupper()):
            newChar = chr ( ( ord(char) - ord('A') + k ) % 26 + ord('A'))
        else:
            newChar = char

        newString.append(newChar)

    return ''.join(newString)