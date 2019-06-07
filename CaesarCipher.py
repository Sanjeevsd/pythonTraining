from caesarcipher import CaesarCipher  # importing caesar library from caesarcipher folder
import CaeserCipher  # importing caesar function from  other program
import random  # importing random function


def generate_random_string(counter):  # defining function for generating random string from random integer values
    concatenated_string = ""  # initialize empty variable for concatenated string
    for integer in range(1, 10):  # loop for integer where integer is from 1 to 10
        random_number = (random.randint(65, 90)) or (random.randint(96, 122))  # generating random number using random
        str_int = chr(random_number)  # converting random number to character and assigning it to variable
        concatenated_string = concatenated_string + str_int  # adding the converted strings
    cipher = CaesarCipher(concatenated_string, offset=counter)  # calling library function and passing variables
    encoded_cipher = cipher.encoded  # calling encoded function and assigning it to a variable
    own_cipher = CaeserCipher.caesar_cipher(concatenated_string,
                                            counter)  # calling own function and passing variables(arguments)
    print(
        "The Caesar Function Result::" + encoded_cipher + " And the written caesar Result::" + own_cipher)  # printing the result
    if encoded_cipher == own_cipher:  # comparing both outputs from library function and own function
        return True  # returning true
    else:  # else
        return False  # returning false


match_count = 0  # initialing variable for counter
total_values = 0  # initializing value
for times in range(0, 10):  # loop for times from 0-10
    checkCode = generate_random_string(times)  # calling function by passing arguments and assigning it to a variable
    if checkCode:  # checking if check code is true or not
        match_count = match_count + 1  # increasing match_count
    total_values = total_values+1     # adding all the loop values
percent_error = ((total_values-match_count)/total_values)*100  # assigning percentage error
print("The Correctness percentage is:: ", 100-percent_error, "%")  # printing the result
