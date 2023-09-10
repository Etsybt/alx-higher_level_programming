#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
  * is_palindrome - checks the list
  * @head: of the list
  * Return: void
  */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}
/**
  * check_pal - checks if the the list is palindrome
  * @head: of the list
  * @last: last
  */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
