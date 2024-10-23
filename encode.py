# Ryan Dennler

original_password = ''
encoded_password = ''


def encode(password):
    return ''.join(map(lambda x: str((int(x) + 3) % 10), password))


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def get_option():
    return input('Please enter an option: ')


def process_encode():
    global original_password, encoded_password
    original_password = input('Please enter your password to encode: ')
    encoded_password = encode(original_password)
    print('Your password has been encoded and stored!')


def main():
    options = {
        '1': process_encode, '2':process_decode
    }

    while True:
        print_menu()
        choice = get_option()
        if choice == '3':
            break
        elif choice in options:
            options[choice]()
        print()


def decode(password):
    decode = ""
    for num in password:
        num = int(num)
        num -= 3
        num = str(num)
        decode += num
    return decode

def process_decode():
    global encoded_password
    print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")


if __name__ == "__main__":
    main()
