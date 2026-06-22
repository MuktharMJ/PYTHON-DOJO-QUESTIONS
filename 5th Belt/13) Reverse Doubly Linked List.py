# Reverse a Doubly Linked List
# Given a doubly linked list, reverse it and print
# the reversed values separated by spaces.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    current = head
    new_head = None

    while current:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev

    return new_head

def print_list(head):
    if head is None:
        print(" ")
        return

    while head:
        print(head.data, end=" ")
        head = head.next

def create_doubly_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head

n = int(input())
values = list(map(int, input().split()))

head = create_doubly_linked_list(values)
reversed_head = reverse_doubly_linked_list(head)
print_list(reversed_head)