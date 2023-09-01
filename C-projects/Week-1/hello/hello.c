#include <stdio.h>
#include <cs50.h>
int main(void)
{
    //take input name from user
    string name = get_string("What is your name: \n");
    //print hello and the name
    printf("hello, %s!\n", name);

}