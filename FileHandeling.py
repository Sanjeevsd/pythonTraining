

def search_countries(countries_list,name):
    lines_counter = 1
    found_result = False
    inputStringCapitalizeLength = len (name)
    found_country=[]
    for countries in countries_list:
        countries_capitalize = countries[:-1].upper()
        if countries_capitalize == name:
            found_result = True
            #print("The country {} found on line:".format(countries_capitalize), lines_counter)
            found_country.append(countries_capitalize)
        # elif inputStringCapitalize in countries_capitalize:
        #     # print("The country is {} found on line:".format(countries_capitalize),lines_counter)
        #     found_result = True
        #     found_country.append(countries_capitalize)
        elif name == countries_capitalize[:inputStringCapitalizeLength]:
            # print("The country is {} found on line:".format(countries_capitalize),lines_counter)
            found_country.append(countries_capitalize)
            found_result=True
        lines_counter = lines_counter+1
    if not found_result:
        # print("No matching countries found")
        found_country.append("Not found")
    return found_country

if __name__=="__main__":

    inputString = input ("Enter a country to search::")
    inputStringCapitalize = inputString.upper ()
    inputFilename = input ("Enter filename:")

    try:
        openFile = open(inputFilename, "r",encoding="utf8")
        readCountries = openFile.readlines()
        print(search_countries(readCountries,inputStringCapitalize))

    except Exception:
        print("Exception")
