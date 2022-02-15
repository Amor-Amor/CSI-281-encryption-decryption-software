import random


class KeyObj:
    def __init__(self, key):
        self.key = key

    def alg_caesar(self):
        """Uses caesar cipher to perform encryption"""
        # TODO

    def encode(self, message):
        """Encodes a message based on the desired key"""
        # TODO

    def decode(self, encoded_message):
        """Decodes the message based on the key that initialized the object"""
        # TODO


def main():
    print("Enter message: ")
    message = input()
    print("Enter algorithm style: ")
    alg = input()
    print("Enter desired key: ")
    key = input()
    KeyObj(key)


if __name__ == "__main__":
    main()
