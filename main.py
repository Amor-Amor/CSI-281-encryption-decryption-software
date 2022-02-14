"""Implementing different ways to create an encryption/decryption key."""

import random


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
    key = prime_list[index]
    return key


def main():
    print(rand_int_key())
    print(prime_num_key())


if __name__ == '__main__':
    main()
