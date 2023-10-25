
def encode(password):
    pass_to_return = ""
    password = [int(x) for x in str(password)]

    for ind, num in enumerate(password):
        password[ind] = num + 3

        if password[ind] > 9:
            password[ind] = password[ind] - 10

        pass_to_return = f"{pass_to_return}{password[ind]}"

    return pass_to_return



def decode(password):
    pass


def main():
    password = None
    encoded_password = None

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
            encoded_password = encode(password)

            print("Your password has been encoded and stored!")
            print()

        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        else:
            break


if __name__ == "__main__":
    main()