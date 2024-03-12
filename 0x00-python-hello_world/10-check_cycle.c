#include "lists.h"
#include <stdio.h>
/**
 * _strcat- Entry point
 * Description: 'the program's description'
 * @dest: First operand
 * @src: Second operand;
 *
 * Return: An int
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, (**p);
	int i, j, n = 0, flag = 0;

	if (list == NULL)
		return (-1);
	for(n = 0; current != NULL; ++n)
		current = current->next;
	p = malloc((n + 1) * sizeof(listint_t *));
	if (p == NULL)
		return (-1);
	current = list;
	for (i = 0; i <= n; i++)
	{
		p[i] = NULL;
		if (current != NULL)
		{
			p[i] = current;
			current = current->next;
		}
	}
	current = list;
	for (i = 0; i <= n; i++)
	{
		for (j = 0, flag = 0; j < i; j++)
		{
			if (p[j] == current)
				flag += 1;
			if (flag == 2)
				break;
		}
		if (flag == 2)
			break;
		current = current->next;
	}
	free(p);
	if (flag == 2)
		return (1);
	return (0);
}

