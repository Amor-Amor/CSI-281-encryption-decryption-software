import random
import secrets


def permutation_key():
    """Generate key for permutation cypher"""
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

    print(key)
    return key


def substitution_key():
    """Generate key for substitution cypher"""

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
        # Pick random character in alphabet string and assign it to its place in key
        index = secrets.randbelow(len(alphabet))
        key[element] = alphabet[index]

        # Loop to make sure we don't repeat characters
        # EX: 'q': 'q' or 'a': 'q' AND 'b': 'q'
        while alphabet[index] == element:
            index = secrets.randbelow(len(alphabet))
            key[element] = alphabet[index]

        # Remove used character from alphabet string
        alphabet = alphabet.replace(alphabet[index], '')

    print(key)
    return key


def main():
    print("PERMUTATION KEY: ")
    p_key = permutation_key()
    print("")

    print("SUBSTITUTION KEY: ")
    s_key = substitution_key()
    print("")


if __name__ == "__main__":
    main()
