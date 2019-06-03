from caesarcipher import CaesarCipher
import CaeserCipher
import random

def generateRandomString(counter):
    ConcatenatedString = ""
    for integer in range(1, 10):
        randomnumber = (random.randint(65, 90)) or (random.randint(96, 122))  # '90-96 contains characters'
        strint = chr(randomnumber)
        ConcatenatedString = ConcatenatedString + strint
    cipherr = CaesarCipher(ConcatenatedString, offset=counter)
    encodedCipher = cipherr.encoded
    owncipher = CaeserCipher.CaeserCipher(ConcatenatedString, counter)
    print( "The Caesar Function Result::"+cipherr.encoded+" And the written caesar Result::"+owncipher)
    if(encodedCipher==owncipher):
        return True
    else:
        return False

match_count=0
for time in range (0,100):
    checkCode = generateRandomString(time)
    if checkCode:
        match_count = match_count+1
    percent_error = 100-match_count
print("The Correctness is:: ",match_count,"%")
