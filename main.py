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


def main():
    print(rand_int_key())
    print(prime_num_key())
    print(secrets_key())


if __name__ == '__main__':
    main()
