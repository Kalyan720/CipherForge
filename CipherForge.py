import random
import itertools

def main():
    recipient_info = RecipientInfo()
    Temp = PermComb(recipient_info)
    for i in Temp:
        print(i)

def PermComb(recipient_info):
    first_name, middle_name, last_name, dob, phone_num, _, _ = recipient_info
    passwords = []
    #Length of the passwords
    def LengthPass():
        C = int(input("Enter the minimum length of the password that you want to generate: "))
        B = int(input("Enter the maximum length of the password that you want to generate: "))
        return C,B
    #Combination of FirstName MidlleName and LastName
    def NameComb():
        name_tuple = (first_name, middle_name, last_name)
        name_combinations = itertools.permutations(name_tuple)
        for name_combo in name_combinations:
            passwords.append(''.join(name_combo))
            passwords.append(' '.join(name_combo))
    #Combination of Name and Date of Birth
    def NameDOB():
        passwords.append(first_name + dob)
        passwords.append(middle_name + dob)
        passwords.append(last_name + dob)
        passwords.append(dob + first_name)
        passwords.append(dob + middle_name)
        passwords.append(dob + last_name)
    #Combination of Name and Phone Number
    #the length of the phone number is equal to length of first_name subtracted from the length of password that is going to be generated
    #the phone number should be passed to a list and for every iteration slice the list accoringly
    def NameNumber():
        phone_num_TC = str(phone_num)
        phone_num_list = [int(digit) for digit in phone_num_TC]
        print(phone_num_list)
        T = len(first_name)
        passwords.append(first_name + phone_num)
        passwords.append(middle_name + phone_num)
        passwords.append(last_name + phone_num)
    #this is the Hero section
    def Herosection():
        for v in (8, 13):
            special_chars = tuple('!@#$%^&*')
            digits = tuple('0123456789')
            t = len(last_name)
            x = v - t - 1
            for i in special_chars:
                passwords.append(last_name + i + str(x))
                passwords.append(first_name + i + str(x))
                passwords.append(first_name + last_name + i + str(x))
    #calling the sub-function that are described above
    LengthPass()
    NameComb()
    NameDOB()
    NameNumber()
    Herosection()

    return passwords

def RecipientInfo():
    #Input for Name
    first_name = input("Enter the First name of the Target: ")
    middle_name = input("Enter the Second name of the Target: ")
    last_name = input("Enter the Last name of the Target: ")
    print(first_name + " " + middle_name + " " + last_name)
    #Input for Date Of Birth
    dob = input("Enter the Date of Birth in the format specified ddmmyyyy: ")
    print(dob)
    #Input for Phone Number
    phone_num = input("Enter the number +91: ")
    print(phone_num)
    #Input for Keywords
    keywords = input("Enter the keywords: ")
    #Input for Previous passwords you remember
    previous_pass = input("Enter the passwords you know: ")
    #return all the variables
    return first_name, middle_name, last_name, dob, phone_num, keywords, previous_pass

if __name__ == "__main__":
    main()
