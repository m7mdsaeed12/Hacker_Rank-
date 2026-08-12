import math
import os
import random
import re
import sys
def solve(s):
    words = [word.capitalize() for word in s.split(' ')]
    return ' '.join(words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
