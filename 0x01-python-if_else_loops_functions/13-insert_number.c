#include "lists.h"

/**
 *insert_node - insert a node in a sorted list
 *@head: the linked list
 *@number: the data of the new node
 *Return: the address of the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = NULL, *tmp = NULL, *new = NULL;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	aux = *head;
	while (aux->next != NULL && aux->n < number)
	{
		tmp = aux;
		aux = aux->next;
	}
	if (aux->next != NULL)
	{
		new->next = aux;
		tmp->next = new;
		return (new);
	}
	aux->next = new;
	return (new);
}
