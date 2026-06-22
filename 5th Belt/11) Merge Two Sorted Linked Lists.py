# Merge Two Sorted Linked Lists
# You are given two sorted singly linked lists.
# Merge them into a single linked list such that
# the final list is also sorted in ascending order.
#
# The lists must be merged by manipulating nodes directly.
# Using any built-in sorting function is not allowed.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

def createLinkedList(elements):
    head = None
    current = None

    for val in elements:
        newNode = ListNode(val)

        if head is None:
            head = newNode
            current = head
        else:
            current.next = newNode
            current = newNode

    return head

def printLinkedList(head):
    current = head

    while current is not None:
        print(current.val, end=" -> ")
        current = current.next

    print("nullptr")

n1 = int(input())
l1_elements = list(map(int, input().split())) if n1 > 0 else []

n2 = int(input())
l2_elements = list(map(int, input().split())) if n2 > 0 else []

l1 = createLinkedList(l1_elements)
l2 = createLinkedList(l2_elements)

merged = mergeTwoLists(l1, l2)
printLinkedList(merged)