#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main() {

int x1 = get_int("Input value of x1:\n");
int y1 = get_int("Input value of y1:\n");
int x2 = get_int("Input value of x2:\n");
int y2 = get_int("Input value of y2:\n");
int distance = ((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1));

printf("The resut is %0.4f\n", sqrt(distance)); // The printf function only prints strings and not integers or floats, hence you have to use a placeholder such as %i.
}