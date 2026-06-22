# Linked List Cycle
# Given the head of a linked list, determine whether the linked list
# contains a cycle.
#
# A cycle occurs when the last node points back to an earlier node
# instead of pointing to None.

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def buildLinkedList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)

    if 1 <= pos <= len(values):
        current.next = nodes[pos - 1]

    return head

n = int(input())
values = list(map(int, input().split()))
x = int(input())

head = buildLinkedList(values, x)

print("True" if hasCycle(head) else "False")