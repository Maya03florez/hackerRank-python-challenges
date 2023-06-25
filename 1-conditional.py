#!/bin/python3

import math
import os
import random
import re
import sys

#python if-else

if __name__ == '__main__':
    # Read input from the user
    n = int(input().strip())
    
    # Check if n is even
    if n % 2 == 0:
        # n is even
        if 2 <= n <= 5:
            # n is even and in the range [2, 5]
            print('Not Weird')  # n is even and not weird
        elif 6 <= n <= 20:
            # n is even and in the range [6, 20]
            print('Weird')  # n is even and weird
        else:
            # n is even and greater than 20
            print('Not Weird')  # n is even and not weird
    else:
        # n is odd
        print('Weird')  # n is odd and weird
