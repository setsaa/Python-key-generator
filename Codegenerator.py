import string
import random

keys = 'keys.txt'

def key_generator(size=15, n_keys=1, chars=string.ascii_uppercase + string.digits):
    """
    Generates a unique key that can be used to identify a purchase.
    """
    key = ''.join(random.choice(chars) for x in range(size))
    with open('keys.txt', 'a') as output_file:
        output_file.write(key + '\n')
    n_keys -= 1
    return key

def key_printer(key=False):
    """
    Transforms key into printable layout.
    Key template:
    xxxxx-xxxxx-xxxxx
    """
    print_key = ''
    if key == False:
        key = key_generator()
    for n, c in enumerate(key):
        if n % 5 == 0 and n != 0:
            print_key += '-'
        print_key += c
    print(print_key)

def key_stripper(key):
    """
    Strips keys of their printed state in order to store them properly.
    """
    key = key.replace('-', '')
    return key

def key_checker(key):
    """
    Checks if key is in list(keys).
    """
    key = key_stripper(key).strip()
    with open('keys.txt', 'r') as input_file:
        for line in input_file:
            if line == key:
                print(True)
                break
        print(False)

key_printer()