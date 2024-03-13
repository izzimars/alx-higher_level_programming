#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new;
	int tot = 1, i = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		for (current = *head; current->next != NULL; ++tot)
			current = current->next;
		tot = tot / 2;
	}
	current = *head;
	prev = *head;
	while (current->next != NULL)
	{
		if (i == tot)
		{
			prev->next = new;
			new->next = current;
		}
		i++;
		prev = current;
		current = current->next;
	}
	return (0);
}
