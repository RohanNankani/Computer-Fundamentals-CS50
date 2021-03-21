#include <stdio.h>


int main()
{
//  int n = 50;
//  int *p = &n; // This line means that the point p is the address to the value of n using the syntax (&n)
//  printf("%i\n", *p); // This line means that give me an integer which is at the location of n. (*p is the point or the address of the integer n).

    char *s = "ROHAN";
    printf("%c %c %c %c %c\n", *s, *(s+1), *(s+2), *(s+3), *(s+4));

}