#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 7, 2022
# This program allows a user to enter a positive number and then see
# the factorial of that number


def main():

    number_counter = 0
    total = 1

    # Print introduction message and get user input
    print("This program will calculate the factorial of any positive number.")
    print(" ")
    user_num = input("Enter a positive number: ")
    print(" ")

    try:
        # Make sure user input is an integer
        user_num_int = int(user_num)

        # Makes sure that user number is positive
        if user_num_int >= 0:
            # Loop that calculates the factorial of the chosen number
            while True:
                number_counter = number_counter + 1
                total = total * number_counter
                print("Tracking {} times through the".format(number_counter) +
                      " loop")
                if number_counter >= user_num_int:
                    break

            # Print final result
            print(" ")
            print("The factorial of {}".format(user_num)
                  + " is {}.".format(total))
        else:
            print("{} is not a positive number.".format(user_num_int))

    except Exception:
        # Prevent crash by displaying error message if user
        # input is not an integer
        print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
