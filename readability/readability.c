#include <cs50.h>
#include <stdio.h>
#include<string.h>
//variables for number of letters,words ,and sentences
int letters_no;
int words_no;
int sentences_no;
//functions indicators
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int calculation(void);
//main
int main(void)
{
    string text;
    //take input of text
    text = get_string("Text: ");
    //functions
    count_letters(text);
    count_sentences(text);
    count_words(text);
    calculation();
}
//count letters functions
int count_letters(string text)
{
    //letters_no = strlen(text);
    letters_no = 0;
    //for loop of counting letters
    for (int i = 0 ; i < strlen(text); i++)
    {
        //if (text[i] == ' ' || text[i] == '!' || text[i] == '?' || text[i] == ',' || text[i] == '\'' || text[i] == ':'|| text[i] == ';'|| text[i] == '"'|| text[i] == '.' )
        if ((text[i] >= 'A' && text[i] <= 'z') || (text[i] >= 'a' && text[i] <= 'z'))
        {
            //letters_no--;
            letters_no++;
        }
    }
    //
    //printf("letters no. is: %i\n", letters_no);
    return letters_no ;
}
//count letters words
int count_words(string text)
{
    words_no = 1 ;
    //for loop of counting words
    for (int i = 0 ; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            words_no++;
        }
        else if (text[i] == ';')
        {
            //words_no++;
        }
        else if (text[i] == ':')
        {
            //words_no++;
        }
        else if (text[i] == ',')
        {
            //words_no++;
        }

    }
    //printf("words no. is: %i \n", words_no);
    return words_no;
}
//count sentences functions
int count_sentences(string text)
{
    sentences_no = 0;
    //for loop of counting sentences
    for (int i = 0 ; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences_no++;
        }
    }
    //printf("sentences no. is: %i\n", sentences_no);
    return sentences_no;
}
//claculation function
int calculation(void)
{

    //printf("letters_no %i\n", letters_no);
    //printf("words_no %i\n", words_no);
    //printf("sentences_no %i\n", sentences_no);
    //int L = (letters_no / words_no*100.0) ;
    //int S = (sentences_no / words_no*100.0);
    //int index = (0.0588 * L - 0.296 * S - 15.8);
    //main claculation
    int index = (0.0588 * letters_no / words_no * 100.0) - (0.296 * sentences_no / words_no * 100.0) - 15.8 + 0.48;
    //printf("words: %i,letters: %i,sentences: %i\n",words_no,letters_no,sentences_no);
    //if statment of grades
    //if grade more than 16 (equivalent to or greater than a senior undergraduate reading level)
    //printf("Grade %i\n", index);
    if (index >=  16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    //if grade less than 1
    if (index <= 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    //else like: grade: 5,7,8....
    else
    {
        printf("Grade %i\n", index);
        return 0;
    }

    return index;
}