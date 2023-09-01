# TODO
from cs50 import get_int


def main():
    # variable of heigth
    # int heigth;
    # do while loop
    while True:
        # get a heigth input from user
        heigth = get_int("Heigth: \n")
        # heigth input variable must be from 1 to 8
        if (heigth >= 1 and heigth <= 8):
            break
    # w must be less than in for loop and check for this condition after increasing w with 1
    for w in range(heigth):
        # h must be less than in for loop and check for this condition after increasing h with 1
        for h in range(heigth):
            # if the sum of w and h less than heigth-1
            y = w + h
            a = heigth - 1
            if y < a:
                # print blank space
                print(" ", end="")
            # otherwise
            elif y >= a:
                # print
                print("#", end="")
                # inserting a newline (break)
            else:
                return 0
        print("")


main()