#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: points to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (!list)
		return (0);
	t = list;
	h = list;
	while (h->next != NULL && h->next->next != NULL)
	{
		t = t->next;
		h = h->next->next;
	}
	if (t == h)
	{
		return (1);
	}
	return (0);
}
