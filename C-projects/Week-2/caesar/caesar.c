#include <cs50.h>
#include <stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int main(int argc, string argv[])
{
    //if condition to end if argc not 2
    if (argc != 2)
    {
        //end programm
        return 1;
    }
    //make sure that argument is digit = number
    for (int i = 0 ; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            //end programm
            return 1;
        }

    }
    // variable for key number = argument inputed
    string key_number = argv[1];
    // turn key_number to int type
    int number = atoi(key_number);
    // get input from user (text)
    string plaintext = get_string("plaintext: ");
    //print cipher text
    printf("ciphertext: ");

    for (int i = 0 ; i < strlen(plaintext) ; i++)
    {
        // if condition if the letter is uppercase
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
        {
            //variable for cipher letter
            int cipherletter = (plaintext[i] + (number) % 26);
            if (cipherletter > 'Z')
            {
                //print cipher letter -26 (no. of English letters)
                printf("%c", cipherletter - 26);
            }
            else
            {
                //print key as it written
                printf("%c", cipherletter);
            }
        }
        // if condition if the letter is lowercase
        else if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
        {
            // variable for cipher letter
            int cipherlettera = (plaintext[i] + (number) % 26);
            //if conditon if the cipher letter is more than z
            if (cipherlettera > 'z')
            {
                //print cipher letter -26 (no. of English letters)
                printf("%c", cipherlettera - 26);
            }
            else
            {
                //print key as it written
                printf("%c", cipherlettera);
            }
        }
        else
        {
            //print key as it written
            printf("%c", plaintext[i]);
        }
    }
    //break
    printf("\n");
}
