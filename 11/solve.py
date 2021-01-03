import re


def has_increasing_sequence(password):
    current_run = 0
    expected_character = None
    for char in password:
        if char == expected_character:
            expected_character = chr(ord(char) + 1)
            current_run += 1
            if current_run == 3:
                return True
        else:
            expected_character = chr(ord(char) + 1)
            current_run = 1
    return False


def is_valid(password):
    return re.search(r'([a-z])\1.*([a-z])\2', password) and re.match(r'^[^iol]+$', password) and has_increasing_sequence(password)


def increment_password(password_list):
    for idx in range(len(password_list) - 1, -1, -1):
        if password_list[idx] != 25:
            password_list[idx] += 1
            return password_list
        else:
            password_list[idx] = 0
    return password_list


def convert_to_list(password):
    return [ord(c) - ord('a') for c in password]


def convert_to_str(password_list):
    return ''.join(chr(ord('a') + i) for i in password_list)


with open('input') as infile:
    santa_password = infile.read().strip()

password_list = convert_to_list(santa_password)

increment_password(password_list)
while not is_valid(convert_to_str(password_list)):
    increment_password(password_list)
print(convert_to_str(password_list))

increment_password(password_list)
while not is_valid(convert_to_str(password_list)):
    increment_password(password_list)
print(convert_to_str(password_list))
