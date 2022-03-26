#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program prompts a user to enter a number
# and tells them if it is positive, negative, or zero.


def main():
    # this function gets a number and checks if it's positive, negative, or zero.

    # input
    user_number = int(input("Enter an integer: "))

    # process
    if user_number > 0:
        # output
        print("{} is a positive number.".format(user_number))
        print("\nDone.")
    elif user_number < 0:
        print("{} is a negative number.".format(user_number))
        print("\nDone.")
    elif user_number == 0:
        print("Your number is just zero.")
        print("\nDone.")
    else:
        print("Something went wrong.")
        print("\nDone.")


if __name__ == "__main__":
    main()
