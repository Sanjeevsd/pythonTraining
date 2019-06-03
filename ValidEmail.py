
for numbers in range(1,10):
    Email_input=input("Enter a email to be verified: ")
    First_portion_invalidity = False
    Second_portion_invalidity = False
    if len(Email_input)>=6:
        if "@" in Email_input :
            Splitted_email = Email_input.split("@")
            First_Portion_Email = Splitted_email[0]
            Second_Portion_Email = Splitted_email[1]
            if First_Portion_Email[0].isalpha():
                for characters in First_Portion_Email:
                    if characters.isalnum():
                        First_portion_validity = True
                    elif "_" in characters or "-" in characters or "." in characters:
                        First_portion_validity = True
                    else:
                        print("The emails contains invalid characters in its name, Hence is is invalid.")
                        First_portion_invalidity = True
                        continue
            else:
                print("The emails cannot start with invalid characters, Hence is is invalid.")
                First_portion_invalidity = True
                continue
            for Characters in Second_Portion_Email:
                if Characters.isalnum():
                    Second_portion_validity = True
                elif "." in Characters:
                    Second_portion_validity = True
                else:
                    print("The email contains invalid characters in its domain, Hence it is Invalid.")
                    Second_portion_invalidity = True
                    continue

            if First_portion_invalidity == False and Second_portion_invalidity == False:
                print("The Email is Valid.")
        else:
            print("The Email Does not contain @ splitter,Hence the Email is invalid email")
    else:
        print("The email is not long enough, Invalid Email")









