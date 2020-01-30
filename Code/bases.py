#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# Variables for string constants
HEXDIGITS = string.hexdigits
DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase 
NUM = string.printable

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    """
    # exp = exponent  (name of variable)
    # dec = decimal  (name of variable)
    if base == 2:
        exp = 0
        dec = 0
        for i in digits[::-1]:
            dec += int(digits) * 2**exp
            exp += 1
        return dec

    # TODO: Decode digits from hexadecimal (base 16)
    # exp = exponent  (name of variable)
    # dec = decimal  (name of variable)
    elif base == 16:
        exp = 0 
        dec = 0
        for i in digits[::-1]:
            dec += HEXDIGITS.index(i) * 16**exp
            exp += 1
        return dec
    """
    # TODO: Decode digits from any base (2 up to 36)
    # dec = decimal  (name of variable)
    dec, index = 0, 0
    for digit in reversed(digits):
        dec += NUM.find(digit) * pow(base, index)
        index += 1
    return dec

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    """
    # TODO: Encode number in binary (base 2)
    if base == 2:
        if number > 1:
            return encode(number//2, base) + str(number % 2)
        else:
            return '1'

    # TODO: Encode number in hexadecimal (base 16)
    elif base == 16:
        hexdecimal = HEXDIGITS[:16]
        if number <= 16:
            return hexdecimal[number]
        else:
            return encode(number//16, base) + hexdecimal[number % 16]
"""
    # TODO: Encode number in any base (2 up to 36)
    """BASE 2-36"""
    base_digits = (DIGITS + LOWER)[:base]
    if number < base:
        return base_digits[number]
    else:
        return encode(number//base, base) + base_digits[number % base]

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
