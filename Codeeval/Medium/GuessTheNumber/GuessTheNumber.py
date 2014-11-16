__author__ = 'Sean'

import fileinput
import math

def main():
    for line in fileinput.input():
        arr = line.split()
        my_max = int(arr[0])
        my_min = 0

        for x in range(1, len(arr)):
            diff = my_max - my_min

            guess = my_min + int(diff / 2)

            if diff % 2 == 1:
                guess += 1

            if arr[x] == 'Lower':
                my_max = guess - 1
            elif arr[x] == 'Higher':
                my_min = guess + 1
            else:
                print(int(guess))
                break

main()