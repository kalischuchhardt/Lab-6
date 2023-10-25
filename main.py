def main_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
def encode(password):
    result = ""
    for i in password:
        number = int(i) + 3
        result += str(number)

    print("Your password has been encoded and stored!\n")
    return result

keep_running = True

while keep_running == True:
    main_menu()
    print()
    user_input = int(input("Please enter an option:"))

    if user_input == 1:
        password = input("Please enter your password to encode:")
        encode(password)

    if user_input == 3:
        keep_running = False
