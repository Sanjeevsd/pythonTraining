import os

inputSearchWord = input("Enter word to search::")
inputSearchWordCapital = inputSearchWord.upper()


def search_word(file_content, file_name):
    lines_counter = 1

    for words in file_content:
        words_capitalize = words[:-1].upper()
        if words_capitalize == inputSearchWordCapital:
            print("The word {} found in the file {} on line:".format(words_capitalize, file_name), lines_counter)
        elif inputSearchWordCapital in words_capitalize:
            print("The word is {} found in the file {} on line:".format(words_capitalize, file_name), lines_counter)
        '''elif inputStringCapitalize == countries_capitalize[:inputStringCapitalizeLength]:      
            print("The word is {} found on line:".format(countries_capitalize),lines_counter)'''
        lines_counter = lines_counter + 1


for files in os.listdir(path="."):
    if files.endswith(".txt"):
        try:
            openFile = open(files, "r")
            readFile = openFile.readlines()
            search_word(readFile, files)
        except Exception:
            print("exception")
