#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - function to check if a singly linked list is a palindrome
 *
 * @head: parameter that point to list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int array[2048];
	int i = 0;
	int j;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	while (tmp != NULL)
	{
		array[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (array[j] != array[i - 1 - j])
		{
			return (0);
		}
	}
	return (1);
}
