def main():
    def menu():
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

    menu()
    input = input("Please enter an option: ")

    def encode():
        global password
        password = input("Please enter your password to encode: ")
        global encoded_password
        encoded_password = ""
        for num in password:
            new_num = int(num) + 3
            if new_num > 10:
                new_num -= 10
            encoded_password += str(new_num)


    if input == "1":
        encode()
        print("Your password has been encoded and stored!")

    elif input == "2":

        print(f"The encoded password is {encoded_password}, and the original password is {password}.")

    elif input == "3":
