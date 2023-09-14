#include "lists.h"
#include <stdio.h>
/**
  * print_dlistint - prints all the elements of a dlistint_t list.
  * @h: head of the list
  * Return: the number of nodes
  */
size_t print_dlistint(const dlistint_t *h)
{
	size_t elements = 0;

	do {
		printf("%d\n", h->n);
		h = h->next;
		elements++;
	} while (h != NULL);
	return (elements);
}
