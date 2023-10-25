# Dylan Cygul
def encode(password):
    pass_to_return = ""
    password = [int(x) for x in str(password)]

    for ind, num in enumerate(password):
        password[ind] = num + 3

        if password[ind] > 9:
            password[ind] = password[ind] - 10

        pass_to_return = f"{pass_to_return}{password[ind]}"

    return pass_to_return
