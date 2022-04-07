import random
import secrets


def secrets_key():
    """Create an integer key using secrets."""
    # The module provides access to secure source of randomness
    encryption_key = secrets.randbelow(27)
    return encryption_key


def permutation_key():
    """Generate key for permutation cypher."""
    # Import SystemRandom class through secrets
    secrets_generator = secrets.SystemRandom()

    # Create a random size for the list from 3 to 10
    size = secrets_generator.randrange(3, 10)

    key = []
    count = 0

    # Loops over each element in the list
    for i in range(0, size, 1):
        # Assigns the element to it's index
        i = count
        key.append(i)
        count += 1

    # Randomly shuffles the list
    random.shuffle(key)

    return key


def substitution_key():
    """Generate key for substitution cypher."""

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

    # Loop over each element in key
    for element in key:
        # Pick random character in alphabet string and set to its place in key
        index = secrets.randbelow(len(alphabet))
        key[element] = alphabet[index]

        # Loop to make sure we don't repeat characters
        # EX: 'q': 'q' or 'a': 'q' AND 'b': 'q'
        while alphabet[index] == element:
            index = secrets.randbelow(len(alphabet))
            key[element] = alphabet[index]

        # Remove used character from alphabet string
        alphabet = alphabet.replace(alphabet[index], '')

    return key


def caesar_key(int_key):
    """Generate key for caesar cypher using a given integer."""
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

    # for letter in key:
    #     print(letter + " = " + key[letter])

    print(key)
    return key


def main():
    p_key = permutation_key()
    print("PERMUTATION KEY:", p_key)

    s_key = substitution_key()
    print("SUBSTITUTION KEY:", s_key)

    print("CAESAR KEY: ")
    c_key = caesar_key(secrets_key())
    print("")


if __name__ == "__main__":
    main()
