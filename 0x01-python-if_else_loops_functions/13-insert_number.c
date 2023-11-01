#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked
 *
 * @head: Pointer to the list
 *
 * @number: number that will be insert into list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *c;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next  = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		c = *head;
		while (c->next != && c->next->n < number)
		{
			c = c->next;
			new->next = c->next;
			c->next = new;
		}
	}
	return (new);
}
