# Find the Intersection Node of Two Linked Lists
# Given the heads of two singly linked lists, determine the node at which
# the two linked lists intersect. If they do not intersect, return null.
#
# Two linked lists intersect if they share the same node by reference,
# not just by value.

import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    p1 = headA
    p2 = headB

    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1

def build_list(elements):
    if not elements:
        return None

    head = ListNode(int(elements[0]))
    curr = head

    for val in elements[1:]:
        curr.next = ListNode(int(val))
        curr = curr.next

    return head

def main():
    input_data = sys.stdin.read().splitlines()

    if len(input_data) < 4:
        return

    listA_vals = input_data[0].split()
    listB_vals = input_data[1].split()
    idxA = int(input_data[2])
    idxB = int(input_data[3])

    headA = build_list(listA_vals)
    headB = build_list(listB_vals)

    if idxA != -1 and idxB != -1:
        intersect_node = headA

        for _ in range(idxA):
            intersect_node = intersect_node.next

        if idxB == 0:
            headB = intersect_node
        else:
            currB = headB

            for _ in range(idxB - 1):
                currB = currB.next

            currB.next = intersect_node

    result = getIntersectionNode(headA, headB)

    print(result.val if result else "null")

if __name__ == "__main__":
    main()