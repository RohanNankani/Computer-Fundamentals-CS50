#include <stdio.h>
#include <cs50.h>

int main()
{
    string names[4];
    names[0] = "ROHAN";
    names[1] = "SAILESH";
    names[2] = "MUMMY";
    names[3] = "PAPA";

    printf("%s\n", names[3]);
    printf("%c%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3], names[0][4]);
}