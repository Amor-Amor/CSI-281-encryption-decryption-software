""" Visualization for encryption/decryption. """

import time

def caesar_encode(sentence, key):
    len_of_sen = len(sentence)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Create the table and data that goes inside of it
    table = "+"
    inside = "|"

    # Initialize the table to the correct size
    table += "---+" * len_of_sen

    # Fill the table with the sentence
    for j in range(len_of_sen):
        inside += (" " + sentence[j] + " |")

    # Print the finished table
    print(table)
    print(inside)
    print(table)

    time.sleep(1)

    # Start filling in with the encoded letter
    word_list = sentence.split(" ")
    counter = 2

    for word in word_list:
        for char in word:
            curr_num = alphabet.index(char)
            curr_num += key

            if curr_num > len(alphabet):
                curr_num -= 26

            inside = inside[:counter] + alphabet[curr_num] +\
                                        inside[counter + 1:]

            time.sleep(1)
            print(table)
            print(inside)
            print(table)

            counter += 4

        counter += 4


def caesar_decode(sentence, key):
    len_of_sen = len(sentence)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Create the table and data that goes inside of it
    table = "+"
    inside = "|"

    # Initialize the table to the correct size
    table += "---+" * len_of_sen

    # Fill the table with the sentence
    for j in range(len_of_sen):
        inside += (" " + sentence[j] + " |")

    # Print the finished table
    print(table)
    print(inside)
    print(table)

    time.sleep(1)

    # Start filling in with the encoded letter
    word_list = sentence.split(" ")
    counter = 2

    for word in word_list:
        for char in word:
            curr_num = alphabet.index(char)
            curr_num -= key

            if curr_num < 0:
                curr_num += 26

            inside = inside[:counter] + alphabet[curr_num] +\
                                        inside[counter + 1:]

            time.sleep(1)
            print(table)
            print(inside)
            print(table)

            counter += 4

        counter += 4


def main():
    print("Encoding: ")
    caesar_encode("hello world", 14)

    print("Decoding: ")
    caesar_decode("vszzc kcfzr", 14)


if __name__ == "__main__":
    main()