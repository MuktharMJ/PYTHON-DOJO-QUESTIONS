# Sort Linked List of 0s, 1s and 2s
# Given a singly linked list containing only 0s, 1s, and 2s,
# sort the linked list in ascending order without using any built-in sorting functions.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    count = [0, 0, 0]

    temp = head
    while temp:
        count[temp.data] += 1
        temp = temp.next

    temp = head
    i = 0

    while temp:
        while count[i] == 0:
            i += 1

        temp.data = i
        count[i] -= 1
        temp = temp.next

def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

n = int(input())
values = list(map(int, input().split()))

head = None
tail = None

for value in values:
    newNode = Node(value)

    if head is None:
        head = tail = newNode
    else:
        tail.next = newNode
        tail = newNode

sortList(head)
printList(head)