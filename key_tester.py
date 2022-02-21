import random


def permutation_key():
    """Generate key for permutation cypher"""
    size = random.randint(3, 10)
    key = []
    count = 0
    for i in range(0, size, 1):
        i = count
        key.append(i)
        count += 1
    print(key)
    # TODO random shuffle

    return key


def string_const_key():
    """Takes in key based solely on input as a single string"""
    # TODO


def array_const_key():
    """Takes in key based solely on input as an array"""
    # TODO


def string_rand_key():
    """Generates a random key as a single string"""
    # TODO


def array_rand_key():
    """Generates random key as an array"""
    # TODO


# https://www.ssh.com/academy/ssh/keygen
def rsa():
    """Uses standard rsa key style"""
    # TODO


def dsa():
    """Uses standard dsa key style"""
    # TODO


def ecdsa():
    """Uses standard ecdsa key style"""
    # TODO


def alg_caesar():
    """Uses caesar cipher to perform encryption"""
    # TODO


def encode(message):
    """Encodes a message based on the desired key"""
    # TODO


def decode(encoded_message):
    """Decodes the message based on the key that initialized the object"""
    # TODO


def main():
    key = permutation_key()


if __name__ == "__main__":
    main()