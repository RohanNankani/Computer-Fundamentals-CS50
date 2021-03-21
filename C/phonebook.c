#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main()
{
    person people[4];

    people[0].name = "ROHAN";
    people[0].number = "647-875-5107";

    people[1].name = "SAILESH";
    people[1].number = "647-978-4143";

    people[2].name = "MUMMY";
    people[2].number = "647-872-6131";

    people[3].name = "PAPA";
    people[3].number = "647-721-4143";

    for (int i = 0; i < 4; i++)
    {
        if(strcmp(people[i].name, "ROHAN") == 0)
        {
            printf("%s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found!\n");
    return 1;
}