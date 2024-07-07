import itertools

def main():
    # Print creative text for "Cipher Forge"
    print_cipher_forge()
    
    # Collect recipient information and generate passwords
    recipient_info = RecipientInfo()
    passwords = PermComb(recipient_info)
    
    # Print generated passwords
    for password in passwords:
        print(password)

def print_cipher_forge():
    # Creative display for "Cipher Forge"
    text = """
     ____ _       _               
    / ___(_)_ __ | |__   ___ _ __ 
   | |   | | '_ \| '_ \ / _ \ '__|
   | |___| | |_) | | | |  __/ |   
    \____|_| .__/|_| |_|\___|_|   
           |_|                    
    """
    print(text)

def PermComb(recipient_info):
    # Unpack recipient information
    first_name, middle_name, last_name, dob, phone_num, _, _ = recipient_info
    passwords = []

    def LengthPass():
        # Get the minimum and maximum length for passwords
        min_length = int(input("Enter the minimum length of the password that you want to generate: "))
        max_length = int(input("Enter the maximum length of the password that you want to generate: "))
        return min_length, max_length

    def NameComb():
        # Generate permutations of the name components
        name_tuple = (first_name, middle_name, last_name)
        name_combinations = itertools.permutations(name_tuple)
        for name_combo in name_combinations:
            passwords.append(''.join(name_combo))
            passwords.append(' '.join(name_combo))

    def NameDOB():
        # Combine name components with date of birth
        passwords.extend([
            first_name + dob,
            middle_name + dob,
            last_name + dob,
            dob + first_name,
            dob + middle_name,
            dob + last_name
        ])

    def NameNumber():
        # Combine name components with phone number
        phone_num_str = str(phone_num)
        passwords.extend([
            first_name + phone_num_str,
            middle_name + phone_num_str,
            last_name + phone_num_str
        ])

    def Herosection():
        # Generate passwords with special characters and digits
        special_chars = '!@#$%^&*'
        for v in (8, 13):
            t = len(last_name)
            x = v - t - 1
            for char in special_chars:
                passwords.extend([
                    last_name + char + str(x),
                    first_name + char + str(x),
                    first_name + last_name + char + str(x)
                ])

