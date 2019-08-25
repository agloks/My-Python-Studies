#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFER 1024 //tamanho do buffer
int main(void)
{
	int fd[2];//variavel do pipe que armazenara o valor no 1, e mostra saida no 0
	pid_t pid;//variavel do pid para o fork(), fork criança uma copia do processo, nesse caso o processo é nosso programa

	if(pipe(fd) < 0)//transformando a variavel fd para pipe, junto com tratamento de error caso fork de error
	{
		perror("pipe");
		return -1;
	}

	if((pid = fork()) < 0)//declarando o pid como fork, e ao mesmo tempo vereficando se nao deu erro
	{
		perror("fork");
		return -1;
	}

	if(pid > 0)//processo filho, a copia
	{
		close(fd[0]);//fecha a saida do pipe, para poder escrever

		char str[BUFFER];//minha msg que guardara a saida do system()
		char comando[BUFFER];//comando dado para o system, necessita correção para uso

		scanf("%s",comando);
		sprintf(str,"%s",comando);
		printf("String enviada pelo pai no pipe: %s\n",str);

		write(fd[1],str,BUFFER);
		exit(0);
	}

	else
	{
		char str_recebida[BUFFER];

		close(fd[1]);

		read(fd[0], str_recebida, BUFFER);
		printf("String Recebida pelo filho no Pipe: %s\n",str_recebida);
		exit(0);
	}

	return 0;
}
