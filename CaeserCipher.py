
def check_length(input_displacement_parent):        # function declaration for checking length of displacement
    input_displacement = input_displacement_parent  # assigning one variable to another
    if input_displacement_parent > 26:              # comparing input displacement with 26, if input is greater below statements are executed
        input_displacement = input_displacement_parent - 26        # subtracting 26 with displacement so that if input s 27 we get displacement 1
        if input_displacement > 26:                              # comparing again with 26 for when the parent displacement is greater then 52
            input_displacement = check_length(input_displacement)   # recursively calling check length function by passing the changed displacement
    elif input_displacement_parent < -26:           # checking if the displacement is less than -26 and similar as that of positive >26
        input_displacement = input_displacement_parent +26   # adding 26 to get numbers between 1-26
        if input_displacement < -26:                         # again checking if displacement is still -<26(for when parent <-57)
            input_displacement = check_length(input_displacement)  # recursively calling check_length function to calculate displacement
    return input_displacement      # finally the calculated displacement is returned
    # the above function executes until the resulting displacement is between 1-26


def caesar_cipher(input_string, input_displacement):        # caesar_cypher function declaration with parameters string and displacement
    check_length_input_displacement = check_length(input_displacement)  # calling check length function with parameters parent displacement to get displacement between 1-26
    final_string = ""   # initializing variable for final string
    coded = ""           # initialing variable for encoded characters
    for characters in input_string:     # loop for each characters in input string
        ascii_code = ord(characters)     # turning each characters in ascii code
        if characters.isupper():        # checking if the character is uppercase
            coded = uppercase_conversion(ascii_code, check_length_input_displacement)   # calling uppercase conversion function and passing parameters
        elif characters.islower():         # else if the characters is not upper
            coded = lowercase_conversion(ascii_code, check_length_input_displacement)     # calling lowercase conversion function with parameters
        final_string = final_string + chr(coded)   # adding all encoded characters to get a string
    return final_string         # returning final encoded string


def uppercase_conversion(ascii_code, u_displacement):  # function declaration for uppercase conversion with two parameters
    to_displace = ascii_code + u_displacement          # initializing variable for  displacing the characters
    if to_displace > 90:                            # checking if to displace variable value is greater then 90
        to_displace = (to_displace - 90)            # changing to displace variable value to less thea 90
        coded = 64 + to_displace                    # adding 64 to to displace value to get encoded value because
# 90+any value should start with  "A"
    else:                                           # else if the to displace value is nto less than 90
        coded = to_displace                         # encoded value is to displace value
    return coded                                     # returning the encoded value


def lowercase_conversion(l_ascii, l_displacement):  # function declaration for lowercase string conversion
    to_displace = l_ascii + l_displacement          # calculation to displace value by adding ascii code the displacement value
    if to_displace > 122:                           # checking if to displace value is greater then 122
        tod = to_displace - 122                      # to displace value gets subtracted with 122 to get values less than 122
        coded = 96 + tod                            # encode value is calculated adding 96 to to displace value because 122+any value should start with "a" ie 96+
    else:                                   # else if the to displace value is nt greater than 122
        coded = to_displace                 # encoded value is to displace value
    return coded                            # return encoded value
