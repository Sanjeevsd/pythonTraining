

inputString = input("Enter a country to search::")
inputStringCapitalize = inputString.upper()
inputFilename = input("Enter filename:")
inputStringCapitalizeLength = len(inputStringCapitalize)

def search_countries(countries_list):
    lines_counter = 1
    found_result = False
    for countries in countries_list:
        countries_capitalize = countries[:-1].upper()
        if countries_capitalize == inputStringCapitalize:
            found_result = True
            print("The country {} found on line:".format(countries_capitalize), lines_counter)
        elif inputStringCapitalize in countries_capitalize:
            print("The country is {} found on line:".format(countries_capitalize),lines_counter)
            found_result = True
        '''elif inputStringCapitalize == countries_capitalize[:inputStringCapitalizeLength]:      
            print("The country is {} found on line:".format(countries_capitalize),lines_counter)'''
        lines_counter = lines_counter+1
    if not found_result:
        print("No matching countries found")

try:
    openFile = open(inputFilename, "r")
    readCountries = openFile.readlines()
    search_countries(readCountries)

except Exception:
    print("Exception")