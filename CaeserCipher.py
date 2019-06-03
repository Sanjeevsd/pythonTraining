def check_length(input_displacement_parent):
    input_displacement=input_displacement_parent
    if input_displacement_parent > 26:
        input_displacement = input_displacement_parent-26
        if input_displacement > 26:
            input_displacement = check_length(input_displacement)
    elif input_displacement_parent < -26:
        input_displacement = input_displacement_parent+26
        if input_displacement < -26:
            input_displacement = check_length(input_displacement)
    return input_displacement



def CaeserCipher(inputString,inputDisplacement):
    check_length_input_disp = check_length(inputDisplacement)
    finalString=""
    coded=""
    for characters in inputString:
        asciicode=ord(characters)
        if(characters.isupper()):
           coded= Uppercaseconversion(asciicode,check_length_input_disp)
        elif(characters.islower()):
            coded=Lowercaseconversion(asciicode,check_length_input_disp)

        finalString=finalString+chr(coded)
    return finalString


def Uppercaseconversion(AsciiCode,iDisplacement):
    todisp = AsciiCode + iDisplacement
    if todisp > 90:
        todisplace = (todisp - 90)
        coded = 64 + todisplace
    else:
        coded = todisp
    return coded


def Lowercaseconversion(lascii, ldisplacement):
    todisp = lascii + ldisplacement
    if (todisp > 122):
        tod = todisp - 122
        coded = 96 + tod
    else:
        coded = todisp
    return  coded

