#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle in it.
  * @list: list to be checked
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *start, *end;

	if (list == NULL)
		return (0);

	start = list;
	end = list;

	while (end != NULL && end->next != NULL)
	{
		start = start->next;
		end = end->next->next;

		if (start == end)
			return (1);
	}
	return (0);
}
