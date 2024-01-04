#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinite_while - sleeps forever
 * return: 1
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - function creates 5 zombies
 * return: always returns 1
 */
int main(void)
{
	int ai;

	for (ai = 0; ai < 5; ai++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
