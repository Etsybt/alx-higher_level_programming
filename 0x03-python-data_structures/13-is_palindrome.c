#include "lists.h"
/**
  * is_palindrome - checks the list
  * @start: of the list
  * Return: void
  */
int is_palindrome(listint_t **start)
{
	if (start == NULL || *start == NULL)
		return (1);
	return (check_pal(start, *start));
}
/**
  * check_pal - checks if the the list is palindrome
  * @start: of the list
  * @end: end
  */
int check_pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_pal(start, end->next) && (*start)->n == end->n)
	{
		*end = (*end)->next;
		return (1);
	}
	return (0);
}
