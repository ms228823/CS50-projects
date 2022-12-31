#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    //make variable for cents
    int cents;
    //use do loop
    do
    {
        // get an input from user
        cents = get_int("What is the change for customers?: ");

    }
    //to get positive value
    while (cents < 0);
    return cents;
}

int calculate_quarters(int cents)
{
    // initial value
    int quarters = 0 ;
    //while loop if value equal to or more than twenty-five cents
    while (cents >= 25)
    {
        cents = cents - 25;
        // add value one
        quarters++;
    }
    //return added value to the variable(quarters)
    return quarters;
}

int calculate_dimes(int cents)
{
    // initial value
    int dimes = 0 ;
    //while loop if value equal to or more than ten cents
    while (cents >= 10)
    {
        cents = cents - 10;
        // add value one
        dimes++;
    }
    //return added value to the variable(dimes)
    return dimes;
}

int calculate_nickels(int cents)
{
    // initial value
    int nickels = 0 ;
    //while loop if value equal to or more than five cents
    while (cents >= 5)
    {
        cents = cents - 5;
        // add value one
        nickels++;
    }
    //return added value to the variable(nickels)
    return nickels;
}

int calculate_pennies(int cents)
{
    // initial value
    int pennies = 0 ;
    //while loop if value equal to or more than one cent
    while (cents >= 1)
    {
        cents = cents - 1;
        // add value one
        pennies++;
    }
    //return added value to the variable(pennies)
    return pennies;
}
