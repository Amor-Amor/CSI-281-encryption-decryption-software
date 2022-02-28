"""Implementing different ways to create an encryption/decryption key."""

import random
import secrets


def rand_int_key():
    """Create a key with the random int function."""
    # Determines how far to shift the alphabet
    encryption_key = random.randint(0, 26)

    # Determines whether to shift left or right
    # 0 = left and 1 = right
    direction_key = random.randint(0, 1)
    if direction_key == 0:
        key = encryption_key * -1
    else:
        key = encryption_key

    return key


def prime_num_key():
    """Create a key that's a prime number, choose at random."""
    # Creates a list of prime numbers and chooses one at random
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    index = random.randint(0, 8)

    # Returns the prime number at the given index
    return prime_list[index]


def secrets_key():
    """Create a key using secrets."""
    # The module provides access to secure source of randomness
    encryption_key = secrets.randbelow(27)
    return encryption_key


def create_key(int_key):
    """Create an alphabetic key using the keys generated above."""
    encryption_key = int_key
    # Create format for key style
    key = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": ""
    }

    # Create string of alphabet to use to assign to elements in dictionary
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in key:
        if encryption_key >= len(alphabet):
            encryption_key = 0

        key[letter] = alphabet[encryption_key]
        encryption_key += 1

    for letter in key:
        print(letter + " = " + key[letter])


def main():
    # print(rand_int_key())
    # print(prime_num_key())
    # print(secrets_key())

    int_key = secrets_key()
    print("Integer key is: " + str(int_key))
    create_key(int_key)


if __name__ == '__main__':
    main()
