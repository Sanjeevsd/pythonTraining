
def CaeserCipher(inputString,inputDisplacement):
    if inputDisplacement>26:
        inputDisplacement=inputDisplacement-26
    elif inputDisplacement<-26:
        inputDisplacement=inputDisplacement+26
    finalString=""
    coded=""
    for characters in inputString:
        asciicode=ord(characters)
        if(characters.isupper()):
           coded= Uppercaseconversion(asciicode,inputDisplacement)
        elif(characters.islower()):
            coded=Lowercaseconversion(asciicode,inputDisplacement)

        finalString=finalString+chr(coded)
    print("the coded word is::"+finalString)


def Uppercaseconversion(AsciiCode,iDisplacement):
    todisp = AsciiCode + iDisplacement
    if todisp > 90:
        todisplace = (todisp - 90)
        coded = 64 + todisplace
        print(coded)
        print(chr(coded))
    else:
        coded = todisp
    return coded


def Lowercaseconversion(lascii, ldisplacement):
    todisp = lascii + ldisplacement
    if (todisp > 122):
        tod = todisp - 122
        coded = 96 + tod
        print(chr(coded))
    else:
        coded = todisp
    return  coded

CaeserCipher("",30)