#include "lists.h"

/**
 *is_palindrome -checks if a list is palindrome
 *@head: the head of the list
 *
 *Return: 0 if is not palindrome, 1 if it is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reverse_node = NULL, *aux;

	if (!head)
		return (1);

	aux = *head;
	while (aux != NULL)
	{
		push_node(&reverse_node, aux->n);
		aux = aux->next;
	}
	aux = *head;
	while (aux != NULL)
	{
		if (aux->n != reverse_node->n)
		{
			return (0);
		}
		aux = aux->next;
		reverse_node = reverse_node->next;
	}
	return (1);
}
/**
 *push_node - a push node list
 *@head: the head of the list
 *@n: the number to be inserted
 */
void push_node(listint_t **head, int n)
{
	listint_t *node = NULL;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return;
	}

	node->n = n;
	node->next = *head;
	*head = node;
}
