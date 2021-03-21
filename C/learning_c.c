#include <cs50.h> //string does not exist in C, and when compiled it will show an error.
//To fix this, we used another library (created by Harvard) where string exist, and hence we declare the libraru so that the computer knows what string means.
#include <stdio.h>

int get_positive_int(void);

void cough(int n);

int main()
{
//    char str[8];
//    printf("Give me a name: \n");
//    fgets(str,8,stdin);
//    printf("Your name is %s\n", str);

    string answer = get_string("What's your name?\n");
    printf("Hello, %s\n", answer);

    int age = get_int("What's your age?\n");
    printf("You are at least %i years old\n", age * 365);

    float price = get_float("What's the price\n");
    printf("Your total is %.2f.\n", price * 1.0625);

     int n = get_int("n: ");
     if (n % 2 == 0)
     {
         printf("Even\n");
     }
     else
     {
         printf("Odd\n");
     }

     int x = get_int("x: ");
     int y = get_int("y: ");
     if (x < y)
     {
         printf("x is less than y\n");
     }
     else if (x > y)
     {
         printf("x is greater than y\n");
     }
     else
     {
         printf("x is equal to y\n");
     }

     char c = get_char("Do you agree\n");
     if (c == 'Y' || c == 'y')
     {
         printf("Agreed\n");
     }
     else if (c == 'N' || c == 'n')
     {
         printf("Not agreed\n");
     }

     cough(3);

     int z = get_positive_int();
     printf("%i\n", z);

     int r;
     do
     {
         r = get_int("Width: ");
     }
     while (r < 1);
     for (int i = 0; i < r; i++)
     {
         printf("?");
     }
     printf("\n");
}

void cough(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("cough\n");
    }
}

int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Positive Integer: ");
    }
    while (n < 1);
    return n;
}

// To print a string, you will have to first create an array telling the computer how many boxes to create for the number of characters of the string.
// For the code to work, you will always need one more box instead of boxes being the same as the number of characters.
// For ex. to print Rohan.N you will put "char str[8]".

// To create a compiler which doesn't use ./a.out all the time
// You can use "clang -o rohan hello.c". This will create a new file of the binary code which will be rohan.
// You can execute by saying "./rohan" and this will run your code

// To find out how many files there are, you can say "ls"
// To remove a file say "rm rohan"
// It will ask you "rm: remove regular file 'rohan'?" and then you go ahead and type "y" which will delete the file.

// The computer won't allow you to run the program since you haven't told the computer to use terms from both libraries.
// To tell the computer to compine libaries, you can say "make learning_c"(don't include the ".c") and then run the code by typing "./learning_c"

