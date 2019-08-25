#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//code work if len_number_char >5
void permutation(char *origin,char final[][8],char permuta_valor[][8],int permutation_posibles,int len_number_char)
{
	//your code here
	char *ret;
	char memory;
	int len_first,len_second,adjust_number_char,adjust_index=0;

	do
	{
		len_first=strlen(permuta_valor[0]);
		printf("strlen - %d and variable - %s\n",len_first,permuta_valor[0]);
		++permuta_valor;
	}while(len_first<len_number_char-1);

	len_second = len_first;

	for(int x=0;x<len_number_char;x++)
	{
		if(len_first == len_second)
		{
			while(len_first == len_second)
			{
				ret = memchr(permuta_valor[1],origin[x],sizeof(permuta_valor[1]));
				if(ret == 0)
				{
					sprintf(final[0],"%c%s",origin[x],permuta_valor[1]);
					printf("first == %s\n",final);
				}
				len_first=strlen(permuta_valor[1]);
				permuta_valor++;
			}
		}
		else if(len_first == len_second+1)
		{
			while(len_first != len_second-1)
			{
				permuta_valor--;
				ret = memchr(permuta_valor[1],origin[x],sizeof(permuta_valor[1]));
				if(ret == 0)
				{
					sprintf(final[0],"%c%s",origin[x],permuta_valor[1]);
					printf("first == %s\n",final);
				}
				len_first = strlen(permuta_valor[1]);
			}
		}
		else
		{
			while(len_first == len_second-1)
			{
				permuta_valor++;
				ret = memchr(permuta_valor[1],origin[x],sizeof(permuta_valor[1]));
				if(ret == 0)
				{
					sprintf(final[0],"%c%s",origin[x],permuta_valor[1]);
					printf("first == %s\n",final);
				}
				len_first=strlen(permuta_valor[1]);
			}
		}
	}



	/*for(int x=0;x<=100;x++)
	{
		printf("sl- %d pv- %s\n",strlen(permuta_valor[1]),permuta_valor[1]);
		++permuta_valor;
		--final;
		if(final==permuta_valor)
		{
			printf("f- %s p- %s\n",final,permuta_valor);
		}
	}*/

}



//permutation with three value --> need condition {if} for case with number that contains number equals example(122,344,566...)
void triple(char *origin,char permuta_valor[][8],char twice_valor[][8],int permutation_possibles,int len_number_char,int *to_triple){
	char cobaia[permutation_possibles+600][len_number_char+1];
	char *ret;
	int memory=0;
	int help = *to_triple;

	//execution first for to generator cobaia for permutation possibles if total>1
	for(int i=1;i<help+1;i++){
		for(int x=0;x<=len_number_char;x++){
			ret = memchr(twice_valor[i],origin[x],sizeof(twice_valor[i]));
			if(ret == 0){
				++memory;
				sprintf(permuta_valor[memory],"%c%s",origin[x],twice_valor[i]);
				printf("%s\n",permuta_valor[memory]);
				}
			}
		}

	//your code here...
	int sum=0,controle=0,s=0,armazenar=0,hope=len_number_char-3;
	if(len_number_char>3){
		for(int d=0;d<hope;d++){
			if(d!=s){
				armazenar=controle-(controle/2);
				controle=0;
				memory+= memory;
				sum = sum-(sum/2);
				}
			for(int x=0;x<len_number_char;x++){
				for(int k=1;k<=memory;k++){
					ret = memchr(permuta_valor[k+armazenar],origin[x],sizeof(permuta_valor[k+armazenar]));
					if(ret == 0){
						++controle;
						++sum;
						sprintf(permuta_valor[sum+memory],"%c%s",origin[x],permuta_valor[k+armazenar]);
						printf("origin -->%c\tcobaia -->%s\tarmazenar -->%d\tmemory -->%d\tnew -->%s\n",origin[x],permuta_valor[k+armazenar],armazenar,memory,permuta_valor[sum+memory]);
					}
				}
			}
		}
	}
}
//function return permutation !2
void twice(char *strin,char dest[][8],int permutation_possibles,int len_number_char,int *to_triple){
	if(permutation_possibles<3&&permutation_possibles>1){
		sprintf(dest[1],"%s",strin);
		sprintf(dest[2],"%c%c",strin[1],strin[0]);
		}
	else{
		int add=0,reverse_add,sub;
		for(int k=0;k<len_number_char;k++){
			for(int i=1;i<len_number_char-k;i++){
				++add;
				sprintf(dest[add],"%c%c",strin[k],strin[i+k]);
				printf("%s\n",dest[add]);
				}
			}
		reverse_add = add;
		int adjust;
		for(int k=0;k<len_number_char;k++){
			adjust = ((len_number_char-1)-k>=0)?((len_number_char-1)-k):0;
			for(int i=1;i<len_number_char-k;i++){
				++reverse_add;
				sprintf(dest[reverse_add],"%c%c",strin[adjust],strin[adjust-i]);
				printf("loop reverse -- >%s\n",dest[reverse_add]);
				}
			sub++;
		}
	*to_triple = add*2;
	}
}

//found n!,(this valor is total possible permutation)
int recursion(int n){
	if(n==0){return 1;}
	else{return n * recursion(n-1);}
}


int main(){
	//variables
	unsigned int found_divisors=0;
	char number_char[10];
	scanf("%s",number_char);
	unsigned int number_int = atoi(number_char);
	unsigned int len_number_char = strlen(number_char);
	unsigned int permutation_possibles = recursion(len_number_char);
	char twice_valor[permutation_possibles+1][8];
	//test -->
	char permuta_valor[permutation_possibles*2][8];
	char final[permutation_possibles*2][8];
	int to_triple=1;
	//condition found prime number
	for (unsigned int x=1;x<number_int;x++){
		if(number_int%x==0){
			found_divisors+=1;
		}
	}

	//print number primer
	printf("found number divides per self = %d and total permutation possible with the number = %d\n",found_divisors,permutation_possibles);
	printf("numberchar =%s\npermutationpossibles =%d\nlennumberchar =%d\n",number_char,permutation_possibles,len_number_char);
	//function what return all permutation
	twice(number_char,twice_valor,permutation_possibles,len_number_char,&to_triple);
	printf("twice_valor[1] = %s  and twice valor[2] = %s\n",twice_valor[1],twice_valor[2]);

	//triple value
	puts("\n");
	triple(number_char,permuta_valor,twice_valor,permutation_possibles,len_number_char,&to_triple);

	//test -->
	permutation(number_char,twice_valor,permuta_valor,permutation_possibles,len_number_char);

	return 0;
}
