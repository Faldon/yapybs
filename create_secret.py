from __future__ import print_function
import random
import string
import sys

if int(sys.version[0]) == 3:
    print("".join(
        [random.SystemRandom().choice(string.digits + string.ascii_letters) for i in range(100)]
    ))
if int(sys.version[0]) == 2:
    print("".join(
        [random.SystemRandom().choice(string.digits + string.letters) for i in range(100)]
    ))
