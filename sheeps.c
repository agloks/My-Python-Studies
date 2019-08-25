#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* count_sheep(int n)
{
  char *ptr = (char*)malloc((n*10)*sizeof(int));
  char *end = (char*)malloc((n*10)*sizeof(int));
  char sheep[] = " sheep...";

  for(int a=1;a<=n;a++)
    {
      sprintf(ptr,"%d%s",a,sheep);
      strcat(end,ptr);
      free(ptr);
    }

  return end;
}

char* count_sheep_two(int n) {

  char *ptr=(char*)calloc(10,sizeof(char));
  char *end=(char*)calloc((n*30),sizeof(char));
  char sheep[] = " sheep...";

  for(int a=1;a<=n;a++)
    {
      sprintf(ptr,"%d%s",a,sheep);
      strcat(end,ptr);
    }

  return end;
}

int main()
{
	char* ver = count_sheep(5);
	printf("result --> %s\n",ver);
}
