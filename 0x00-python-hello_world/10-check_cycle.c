#include "lists.h"

/**
 * check_cycle - checks if a single list has a cycle
 * @list: head of the list
 *
 * Return: 0 if there is no, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);

	}
	return (0);
}
