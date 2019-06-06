

def check_length(input_displacement_parent):
    input_displacement = input_displacement_parent
    if input_displacement_parent > 26:
        input_displacement = input_displacement_parent-26
        if input_displacement > 26:
            input_displacement = check_length(input_displacement)
    elif input_displacement_parent < -26:
        input_displacement = input_displacement_parent+26
        if input_displacement < -26:
            input_displacement = check_length(input_displacement)
    return input_displacement


def caesar_cipher(input_string, input_displacement):
    check_length_input_displacement = check_length(input_displacement)
    final_string = ""
    coded = ""
    for characters in input_string:
        ascii_code = ord(characters)
        if characters.isupper():
            coded = uppercase_conversion(ascii_code, check_length_input_displacement)
        elif characters.islower():
            coded=lowercase_conversion(ascii_code, check_length_input_displacement)

        final_string = final_string+chr(coded)
    return final_string


def uppercase_conversion(ascii_code, i_displacement):
    to_displace = ascii_code + i_displacement
    if to_displace > 90:
        to_displace = (to_displace - 90)
        coded = 64 + to_displace
    else:
        coded = to_displace
    return coded


def lowercase_conversion(l_ascii, l_displacement):
    to_displace = l_ascii + l_displacement
    if to_displace > 122:
        tod = to_displace - 122
        coded = 96 + tod
    else:
        coded = to_displace
    return coded

