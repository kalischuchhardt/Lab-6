# Kali Schuchhardt
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
    return result

def decode(password):
    result = ""
    for index in password:
        num = int(index) - 
        result += str(num)
    return result 

keep_running = True

while keep_running == True:
    main_menu()
    print()
    user_input = int(input("Please enter an option:"))

    if user_input == 1:
        password = input("Please enter your password to encode:")
        encoded = encode(password)
        print("Your password has been encoded and stored!\n")
    if user_input == 2:
       decoded = decode(encoded)
       print(f"The encoded password is {encoded}, and the original password is {decoded}.") 
    if user_input == 3:
        keep_running = False
        break
