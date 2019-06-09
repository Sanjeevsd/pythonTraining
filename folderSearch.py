import os


def search_word(file_content, folder_file_name, input_word_capitalized):
    lines_counter = 1

    for words in file_content:
        words_capitalize = words[:-1].upper()
        if words_capitalize == input_word_capitalized:
            print("The word {} found in the file {}\\{} on line:".format(words_capitalize, os.path.basename(os.getcwd()), folder_file_name), lines_counter)
        elif input_word_capitalized in words_capitalize:
            print("The word is {} found in the file {}\\{} on line:".format(words_capitalize, os.path.basename(os.getcwd()), folder_file_name), lines_counter)
        '''elif input_word_capitalized == countries_capitalize[:inputStringCapitalizeLength]:      
            print("The word is {} found on line:".format(countries_capitalize),lines_counter)'''
        lines_counter = lines_counter + 1


def search_folders(input_capitalized):
    folders = os.listdir()
    for folder in folders:
        if os.path.isfile(folder) and folder.endswith(".txt"):
            try:
                open_file = open(folder, "r")
                read_file = open_file.readlines()
                search_word(read_file, folder, input_capitalized)
            except Exception:
                print("exception")
        elif os.path.isdir(folder):
            os.chdir(folder)
            search_folders(input_capitalized)
            os.chdir("../")


inputSearchWord = input("Enter word to search::")
inputSearchWordCapital = inputSearchWord.upper()
search_folders(inputSearchWordCapital)