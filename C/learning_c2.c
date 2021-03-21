#include <cs50.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    float x = get_float("x: ");
    float y = get_float("y: ");

    printf("x / y = %.10f\n", x /y);

    for (int i = 1; ; i *= 2)
    {
        printf("%i\n", i);
        sleep(1);
    }

}