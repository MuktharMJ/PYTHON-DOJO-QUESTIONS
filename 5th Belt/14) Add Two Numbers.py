# Add Two Numbers
# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each node contains a single digit.
#
# Add the two numbers and return the sum as a linked list.
# The result should also be stored in reverse order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

    return dummy.next

def create_list(arr):
    head = ListNode(arr[0])
    tail = head

    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next

    return head

def print_list(head):
    while head:
        print(head.val, end="")
        if head.next:
            print(" ", end="")
        head = head.next
    print()

n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

l1 = create_list(arr1)
l2 = create_list(arr2)

result = add_two_numbers(l1, l2)
print_list(result)