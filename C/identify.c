 #include <stdio.h>
 #include <cs50.h>
 #include <string.h>

 int main()
 {
  string names[4] = {"ROHAN", "SAILESH", "MUMMY", "PAPA"};

  for (int i = 0; i < 4; i++)
  {
   if (strcmp(names[i], "ROHAN") == 0)
   {
    printf("Found\n");
    return 0;
   }
  }
  printf("Not found\n");
  return 1;
 }