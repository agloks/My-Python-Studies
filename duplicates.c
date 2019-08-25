/*
	1- Receber uma string(vetor de caracter) na função
	2- Checkar qual caracter da string se repete nela(letra minuscula == letra maiscula)
	3- As qual for letra repetida sera = ')' e as não repetidas sera = '('
	4- Retorna a string final formatada no respectitivo objetivo acima
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *duplicate(char *s)
{
	char *ptr = s, *get;
	int count = strlen(s), index = 0, control = 0;
	get=(char*)malloc(count*sizeof(char));
	while(*s != 0)
	{
		for(int r = 0;r<count;r++)
		{
			if((r != index && ptr[r] == *s)||(r != index && ptr[r] == *(s)+32)||(r != index && ptr[r] == *(s)-32))
			{
				control+=1;
				break;
			}
		}
		if(control != 0)
		{
			get[index] = ')';
			control = 0;
		}
		else{get[index] = '(';}
		s++;
		index++;
	}
	return get;
}


int main()
{
	char string[50];
	for(int x = 0;x<3;x++)
	{
		sprintf("%s",string);
		printf("%s\n",duplicate(string));
	}
return 0;
}
