#include <stdio.h>
#include <cs50.h>

int main(int arcg, string argv[])
{
    if (arcg == 2)
    {
        printf("Hello, %s\n", argv[1]);
    }
    else
    {
        printf("Hello, world\n");
    }
}