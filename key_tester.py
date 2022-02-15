import random


class KeyObj:
    def __init__(self, key, style):
        self.key = key
        self.style = style

    def string_const_key()
        """Takes in key based solely on input as a single string"""
        # TODO
        
     def array_const_key()
        """Takes in key based solely on input as an array"""
        # TODO
        
    def string_rand_key()
        """Generates a random key as a single string"""
        # TODO
        
     def array_rand_key()
        """Generates random key as an array"""
        # TODO
     
    # https://www.ssh.com/academy/ssh/keygen
    def rsa()
        """Uses standard rsa key style"""
        # TODO
        
    def dsa()
        """Uses standard rsa key style"""
        # TODO
    
    def ecdsa()
        """Uses standard rsa key style"""
        # TODO
    
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
    print("Enter key style: ")
    alg = input()
    print("Enter desired key: ")
    key = input()
    KeyObj(key)


if __name__ == "__main__":
    main()
