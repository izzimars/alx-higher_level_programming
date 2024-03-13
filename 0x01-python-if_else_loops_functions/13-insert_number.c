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

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	current = *head;
	prev = NULL;
	while (current->next != NULL)
	{
		if (current->n > number)
		{
			if (current == *head)
			{
				*head = new;
				new->next = current;
			}
			else
			{
				prev->next = new;
				new->next = current;
			}
			break;
		}
		prev = current;
		current = current->next;
	}
	return (0);
}
