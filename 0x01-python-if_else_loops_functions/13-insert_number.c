#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/*
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: number to insert in the node
 * Return: address of the new node else NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *behind;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		behind = NULL;
		while (current != NULL)
		{
			if (current->n > number)
			{
				if (behind == NULL)
				{
					new->next = *head;
					*head = new;
					break;
				}
				behind->next = new;
				new->next = current;
				break;
			}
			behind = current;
			current = current->next;
		}
		behind->next = new;
	}

	return (new);
}
