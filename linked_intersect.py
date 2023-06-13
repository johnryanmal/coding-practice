# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def linked_iter(node):
    while node is not None:
        yield node
        node = node.next

def linked_intersect(a, b):
    seen = set()

    for node in linked_iter(a):
        seen.add(node)

    for node in linked_iter(b):
        if node in seen:
            return node


intersection = Node(8, Node(10))
a = Node(3, Node(7, intersection))
b = Node(99, Node(1, intersection))

print(linked_intersect(a, b).val) #=> 8