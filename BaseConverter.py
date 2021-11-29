isconverted = False
while not isconverted:
    converttype = input("enter '1' to convert binary to base 10, or '2' to convert base 10 to binary.")
    if converttype == ("1"):
        toconvert = input("enter a binary number to convert into base 10")
        converted = int(toconvert,2)
        print(converted)
        isconverted = True
    elif converttype == ("2"):
        toconvert = input("enter a base 10 number to convert to binary")
        toconverti = int(toconvert)
        converted = bin(toconverti).replace('0b','')
        x = converted[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        print(converted)
        isconverted = True
    else:
        print("please enter either '1' or '2'.")