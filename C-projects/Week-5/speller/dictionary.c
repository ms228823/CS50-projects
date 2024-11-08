//Collins Speller 2020 Solution

// Implements a dictionary's functionality
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


unsigned int Count_size = 0;

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 500;
// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return Count_size;
}

// Hash table
node *table[N];
// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *open_dictionary = fopen(dictionary, "r");
    if (open_dictionary == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(open_dictionary, "%s", word) != EOF)
    {
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            return false;
        }
        strcpy(newNode -> word, word);
        newNode -> next = NULL;
        int i = hash(word);

        if (table[i] == NULL)
        {
            table[i] = newNode;
        }
        else
        {
            newNode -> next = table[i];
            table[i] = newNode;
        }
        Count_size++;
    }
    fclose(open_dictionary);
    return true;
}
// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int value = 0;
    unsigned int key_len = strlen(word);
    for (int i = 0; i < key_len; i++)
    {
        value = value + 37 * tolower(word[i]);
    }
    value = value % N;
    return value;
}
// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);

    node *cursor = table[index];

    while (cursor != NULL)
    {
        //compare word in text with word in dictionary
        if (strcasecmp(cursor -> word, word) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }
    return false;
}
// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
        while (table[i] != NULL)
        {
            node *tmp = table[i] ->next;
            free(table[i]);
            table[i] = tmp;
        }
    return true;
}
