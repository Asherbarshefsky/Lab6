def encode(password):
    encoded = ""
    for i in password:
        new_number = int(i) + 3
        if (new_number >= 10):
            new_number -= 10
        encoded += str(new_number)
    return encoded


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_option = input("Please enter an option: ")

        if user_option == 1:
            user_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_option == 3:
            break