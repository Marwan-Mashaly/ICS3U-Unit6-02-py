#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program rounds decimal numbers to a decimal point

import random


def sum_of_numbers(list_of_numbers):
    # this functions add up all the numbers in the list

    largest = list_of_numbers[0]
    for single_number_in_list in range(0, len(list_of_numbers)):
        if list_of_numbers[single_number_in_list] > largest:
            largest = list_of_numbers[single_number_in_list]

    return largest


def main():
    # this function uses a list

    random_numbers = []
    largest = 0

    # input
    print("The numbers are: ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    largest = sum_of_numbers(random_numbers)

    print("The largest number is: {0} ".format(largest))


if __name__ == "__main__":
    main()
