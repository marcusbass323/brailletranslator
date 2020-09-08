brailleArray = []
plaintext = 'The quick brown fox jumps over the lazy dog'

def solution(plaintext):
    for i in plaintext:
        if i == " ":
            brailleArray.append('000000')
        if i == "a":
            brailleArray.append('100000')
        elif i =="a".upper():
            brailleArray.append('000001100000')
        if i == "b":
            brailleArray.append('110000')
        elif i =="b".upper():
            brailleArray.append('000001110000')
        if i == "c":
            brailleArray.append('100100')
        elif i =="c".upper():
            brailleArray.append('000001100100')
        if i == "d":
            brailleArray.append('100110')
        elif i =="d".upper():
            brailleArray.append('000001100110')
        if i == "e":
            brailleArray.append('100010')
        elif i =="e".upper():
            brailleArray.append('000001100010')
        if i == "f":
            brailleArray.append('110100')
        elif i =="f".upper():
            brailleArray.append('000001110100')
        if i == "g":
            brailleArray.append('110110')
        elif i =="g".upper():
            brailleArray.append('000001110110')
        if i == "h":
            brailleArray.append('110010')
        elif i =="h".upper():
            brailleArray.append('000001110010')
        if i == "i":
            brailleArray.append('010100')
        elif i =="I".upper():
            brailleArray.append('000001010100')
        if i == "j":
            brailleArray.append('010110')
        elif i =="J".upper():
            brailleArray.append('000001010110')
        if i == "k":
            brailleArray.append('101000')
        elif i =="K".upper():
            brailleArray.append('000001101000')
        if i == "l":
            brailleArray.append('111000')
        elif i =="L".upper():
            brailleArray.append('000001111000')
        if i == "m":
            brailleArray.append('101100')
        elif i =="M".upper():
            brailleArray.append('000001101100')
        if i == "n":
            brailleArray.append('101110')
        elif i =="N".upper():
            brailleArray.append('000001101110')
        if i == "o":
            brailleArray.append('101010')
        elif i =="O".upper():
            brailleArray.append('000001101010')
        if i == "p":
            brailleArray.append('111100')
        elif i =="P".upper():
            brailleArray.append('000001111100')
        if i == "q":
            brailleArray.append('111110')
        elif i =="Q".upper():
            brailleArray.append('000001111110')
        if i == "r":
            brailleArray.append('111010')
        elif i =="R".upper():
            brailleArray.append('000001111010')
        if i == "s":
            brailleArray.append('011100')
        elif i =="S".upper():
            brailleArray.append('000001011100')
        if i == "t":
            brailleArray.append('011110')
        elif i =="T".upper():
            brailleArray.append('000001011110')
        if i == "u":
            brailleArray.append('101001')
        elif i =="U".upper():
            brailleArray.append('000001101001')
        if i == "v":
            brailleArray.append('111001')
        elif i =="V".upper():
            brailleArray.append('000001111001')
        if i == "w":
            brailleArray.append('010111')
        elif i =="W".upper():
            brailleArray.append('000001010111')
        if i == "x":
            brailleArray.append('101101')
        elif i =="X".upper():
            brailleArray.append('000001101101')
        if i == "y":
            brailleArray.append('101111')
        elif i =="Y".upper():
            brailleArray.append('000001101111')
        if i == "z":
            brailleArray.append('101011')
        elif i =="Z".upper():
            brailleArray.append('000001101011')
    str1 = ''.join(str(e) for e in brailleArray)
    print(str1)
    print('000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110')
    return str1
solution(plaintext)
