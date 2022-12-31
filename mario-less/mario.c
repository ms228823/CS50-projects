#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // variable of heigth
    int heigth;
    // do while loop
    do
    {
        //get a heigth input from user
        heigth = get_int("Heigth: \n");
    }
    // heigth input variable must be from 1 to 8
    while (heigth < 1 || heigth > 8);
    // w must be less than in for loop and check for this condition after increasing w with 1
    for (int w = 0; w < heigth; w++)
    {
        // h must be less than in for loop and check for this condition after increasing h with 1
        for (int  h = 0; h < heigth; h++)
        {
            //if the sum of w and h less than heigth-1
            if (w + h < heigth - 1)
            {
                //print blank space
                printf(" ");
            }
            //otherwise
            else if (w + h >= heigth - 1)
            {
                //print
                printf("#");
                //inserting a newline (break)
            }
            else
            {
                return 0 ;
            }
        }
        printf("\n");
    }

}