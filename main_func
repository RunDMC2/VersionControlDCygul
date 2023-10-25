def main():
    password = None

    while True:
        # menu
        print("Menu \n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = int(input("Please enter your password to encode: "))
            password = encode(password)

            print("Your password has been encoded and stored!")
            print()

        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")

        else:
            break
