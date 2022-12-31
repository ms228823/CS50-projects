#include <stdio.h>
#include <math.h>
#include<cs50.h>
//make variable card type long
long card;
int card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16;
//main
int main(void)
{
    //loop to ask
    do
    {
        //take the input to card
        card = get_long("Card No: ");
    }
    while (card < 0);

    // make variables for digits and make each is a single digit

    int card16x = card16 * 1;
    int card15x = card15 * 10;
    int card14x = card14 * 100;
    int card13x = card13 * 1000;
    int card12x = card12 * 10000;
    int card11x = card11 * 100000;
    int card10x = card10 * 1000000;
    int card9x = card9 * 10000000;
    int card8x = card8 * 100000000;
    int card7x = card7 * 1000000000;
    int card6x = card6 * 10000000000;
    int card5x = card5 * 100000000000;
    int card4x = card4 * 1000000000000;
    int card3x = card3 * 10000000000000;
    int card2x = card2 * 100000000000000;

    int card15min =  card15x - card16x ;
    int card14min = card14x - card15x - card16x ;
    int card13min = card13x - card14x - card15x - card16x;
    int card12min = card12x - card13x - card14x - card15x - card16x;
    int card11min = card11x - card12x - card13x - card14x - card15x - card16x;
    int card10min = card10x - card11x - card12x - card13x - card14x - card15x - card16x;
    int card9min = card9x - card10x - card11x - card12x - card13x - card14x - card15x - card16x;
    int card8min = card8x - card9x - card10x - card11x - card12x  - card13x - card14x - card15x - card16x ;
    int card7min = card7x - card8x - card9x - card10x - card11x - card12x - card13min;
    int card6min = card6x - card7x - card8x - card9x - card10x - card11x - card12x - card13min;
    int card5min = card5x - card6x - card7x - card8x - card9x - card10x - card11x - card13min;
    int card4min = card4x - card5x - card6x - card7x - card8x - card9x - card10x - card11x - card12x - card13min;
    int card3min = card3x - card4x - card5x - card6x - card7x - card8x - card9x - card10x - card11x - card12x - card13min;
    int card2min = card2x - card3x - card4x - card5x - card6x - card7x - card8x - card9x - card10x - card11x - card12x - card13min;

    card16 = (card % 10);
    card15 = ((card % 100 - card16x) / 10);
    card14 = ((card % 1000 - card15min) / 100);
    card13 = ((card % 10000 - card14min) / 1000);
    card12 = ((card % 100000 - card13min) / 10000);
    card11 = ((card % 1000000 - card12min) / 100000);
    card10 = ((card % 10000000 - card11min) / 1000000);
    card9 = ((card %  100000000 - card10min) / 10000000) ;
    card8 = ((card %  1000000000 - card9min) / 100000000);
    card7 = ((card %  10000000000 - card8min) / 1000000000);
    card6 = ((card %  100000000000 - card7min) / 10000000000);
    card5 = ((card %  1000000000000 - card6min) / 100000000000);
    card4 = ((card %  10000000000000 - card5min) / 1000000000000);
    card3 = ((card %  100000000000000 - card4min) / 10000000000000);
    card2 = ((card %  1000000000000000 - card3min) / 100000000000000);
    card1 = ((card %  10000000000000000 - card2min) / 1000000000000000);
    // then multiply odd digits by 2 and add digits that is more than 9
    int card1o = (((((card1 * 2) - (card1 * 2 % 10)) / 10) + (card1 * 2 % 10)));
    int card3o = (((((card3 * 2) - (card3 * 2 % 10)) / 10) + (card3 * 2 % 10)));
    int card5o = (((((card5 * 2) - (card5 * 2 % 10)) / 10) + (card5 * 2 % 10)));
    int card7o = (((((card7 * 2) - (card7 * 2 % 10)) / 10) + (card7 * 2 % 10)));
    int card9o = (((((card9 * 2) - (card9 * 2 % 10)) / 10) + (card9 * 2 % 10)));
    int card11o = (((((card11 * 2) - (card11 * 2 % 10)) / 10) + (card11 * 2 % 10)));
    int card13o = (((((card13 * 2) - (card13 * 2 % 10)) / 10) + (card13 * 2 % 10)));
    int card15o = (((((card15 * 2) - (card15 * 2 % 10)) / 10) + (card15 * 2 % 10)));
    //then add all odds in sum_of_odds
    int sum_of_odds = card1o + card3o  + card5o + card7o + card9o + card11o + card13o + card15o;
    //then add all odds in sum_of_evens
    int sum_of_evens =  card2 + card4 + card6 + card8 + card10 + card12 + card14 + card16;
    // total summation of sum_of_odds and sum_of_evens
    int total = sum_of_odds + sum_of_evens;
    //make variable if card's digits16
    int card1t16 = (card1 * 10) + card2;
    //make variable if card's digits15
    int card1t15 = (card2 * 10) + card3;
    //make variable if card's digits13
    int card1t13 = (card4 * 10) + card5;
    // if total dose not include 0 then print "INVAILD CARD NUMBER" message
    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    else if (card1 == 4 || card1t16 == 40 || card1t16 == 41 || card1t16 == 42 || card1t16 == 43)
    {
        printf("VISA\n");
        return 0 ;
    }
    else if (card1t16 == 44 || card1t16 == 45 || card1t16 == 46 || card1t16 == 47 || card1t16 == 48 || card1t16 == 49)
    {
        printf("VISA\n");
        return 0 ;
    }
    else if (card1t13 == 45 || card1t13 == 46 || card1t13 == 47 || card1t13 == 48 || card1t13 == 49)
    {
        printf("VISA\n");
        return 0 ;
    }
    else if (card1t13 == 40 || card1t13 == 41 || card1t13 == 42 || card1t13 == 43 || card1t13 == 44)
    {
        printf("VISA\n");
        return 0 ;
    }
    else if (card1t16 == 51 || card1t16 == 52 || card1t16 == 53 || card1t16 == 54 || card1t16 == 55)
    {
        printf("MASTERCARD\n");
        return 0 ;
    }

    else if (card1t15 == 34 || card1t15 == 37)
    {
        printf("AMEX\n");
        return 0 ;
    }
    else
    {
        printf("INVALID\n");
        return 0 ;
    }

}

