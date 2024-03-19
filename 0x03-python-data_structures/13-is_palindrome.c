#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t (*last);
	int i, j;
	listint_t (**templist);

	if (head == NULL)
		return (-1);
	last = *head;
	for (i = 0; last != NULL; i++)
		last = last->next;
	templist = malloc(sizeof(listint_t) * (i + 1));
	if (templist == NULL)
		return (-1);
	last = *head;
	for (i = 0; last != NULL; i++)
	{
		templist[i] = last;
		last = last->next;
	}
	templist[i] = NULL;
	for (j = i - 1, i = 0; (j - i) > 1; i++, j--)
	{
		if (templist[i]->n != templist[j]->n)
			return (0);
	}
	return (1);

}
