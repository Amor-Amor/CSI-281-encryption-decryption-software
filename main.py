import random

"""creating a key with the random int function"""
# determines how far to shift the alphabet
encryption_key = random.randint(0, 26)

# determines whether to shift left or right
# 0 = left and 1 = right
direction_key = random.randint(0, 1)
if direction_key == 0:
    key = encryption_key * -1
else:
    key = encryption_key


""""""
