#include <stdio.h>
#include <cs50.h>

float average(int lenght, int array[]);

int main()
{
//  int mark1 = 10;
//  int mark2 = 20;
//  int mark3 = 30;

//  printf("Average: %i\n", (mark1 + mark2 + mark3)/3);

    int n = get_int("Number of scores: ");

    int scores[n];

    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Scores %i: ", i + 1);
    }

    printf("Average: %.1f\n", average(n, scores));
}


float average(int lenght, int array[])
{
    int sum = 0;
    for (int i = 0; i < lenght; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) lenght;
}

