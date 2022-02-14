"""Template for Caesar Cipher

The following code was written by Amor
"""

import string

def preprocessing(a_message):
    a_message = a_message.replace(" ", "")
    a_message = a_message.lower()
    return a_message

def letter_to_number(a_message):
    a_message = preprocessing(a_message)
    ascii_values = []
    for char in a_message:
        ascii_values.append(ord(char))
    return ascii_values


def number_to_letter(code):
    numbers = []
    for element in code:
        numbers.append(chr(element))

    return numbers


def encryption(a_message, key):
    message_in_numbers = letter_to_number(a_message)
    code = [element + key for element in message_in_numbers]
    ciphertext = number_to_letter(code)
    return ciphertext


def decryption(ciphertext, key):
    code = letter_to_number(ciphertext)
    message_in_numbers = [number - key for number in code]
    message = number_to_letter(message_in_numbers)
    return message


def main():
    message = "Bill ran from the giraffe toward the dolphin"
    key = 4
    print("Original message:  " + message)
    ciphertext = encryption(message, key)
    print("Encrypted message: " + str(ciphertext))

    message_to_be_decrypted = ''.join(ciphertext)
    message_2 = decryption(message_to_be_decrypted, key)
    print("decrypted message: " + str(message_2))


if __name__ == "__main__":
    main()