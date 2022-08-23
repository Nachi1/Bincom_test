# for task number 8
import random
import string

# generating 4 random numbers of binary
temp = random.randint(9, 15)

CHAR_LOOKUP = list(string.digits + string.ascii_uppercase)


def numeral(n):
    global CHAR_LOOKUP
    return CHAR_LOOKUP[n]


# function to convert generated base 2 number to base 10
def convert_base(number, base):
    if base < 2 or base > 36:
        return False
    mods = []
    while number > 0:
        mods.append(numeral(number % base))
        number //= base
    mods.reverse()
    return ''.join(mods)


base2 = convert_base(temp, 2)  # 11111111
print(convert_base(int(base2), 10))
# can't seem to get it right
