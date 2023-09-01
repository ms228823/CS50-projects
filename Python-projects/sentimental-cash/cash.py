# TODO
from cs50 import get_float
from math import floor


def get_cents():

    # make variable for cents
    # use do loop
    while True:
        # get an input from user
        cents = get_float("Change owed:")
        cents = floor(cents * 100)
        if cents > 0:
            break
    # to get positive value
    return cents


def calculate_dimes(cents):
    # initial value
    dimes = 0
    # while loop if value equal to or more than ten cents
    while cents >= 10:

        cents = cents - 10
        # add value one
        dimes += 1
    # return added value to the variable(dimes)
    return dimes


def calculate_nickels(cents):

    # initial value
    nickels = 0
    # while loop if value equal to or more than five cents
    while cents >= 5:
        cents -= 5
        # add value one
        nickels += 1
    # return added value to the variable(nickels)
    return nickels


def calculate_pennies(cents):

    # initial value
    pennies = 0
    # while loop if value equal to or more than one cent
    while cents >= 1:

        cents -= 1
        # add value one
        pennies += 1
    # return added value to the variable(pennies)
    return pennies


def calculate_quarters(cents):

    # initial value
    quarters = 0
    # while loop if value equal to or more than twenty-five cents
    while cents >= 25:
        cents -= 25
        # add value one
        quarters += 1

    # return added value to the variable(quarters)
    return quarters


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)


main()