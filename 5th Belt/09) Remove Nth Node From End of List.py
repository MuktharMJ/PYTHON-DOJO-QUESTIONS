# Remove Nth Node From End of List
# Given a singly linked list and an integer k,
# remove the kth node from the end of the linked list
# and return the resulting list.
#
# The solution should be implemented in a single pass
# using O(1) auxiliary space.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("nullptr")

n = int(input())
values = list(map(int, input().split()))
k = int(input())

head = None
current = None

for value in values:
    newNode = ListNode(value)

    if head is None:
        head = newNode
        current = head
    else:
        current.next = newNode
        current = newNode

head = removeNthFromEnd(head, k)
printList(head)