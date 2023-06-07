# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

from functools import cache

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @property
    def children(self):
        for node in (self.left, self.right):
            if node is not None:
                yield node

tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))


def memo(root):
    unival = {}
    
    def dfs(node):
        if node is None:
            return 0
        
        count = 0
        is_unival = True
        for child in node.children:
            count += dfs(child)
            if not (unival[child] and child.val == node.val):
                is_unival = False
        
        unival[node] = is_unival
        count += (1 if is_unival else 0)
        
        return count
    
    return dfs(root)


def univals(root):
    @cache
    def unival(node):
        return (
            node is not None
            and (
                node.left is None
                or (
                    unival(node.left)
                    and node.left.val == node.val
                )
            )
            and (
                node.right is None
                or (
                    unival(node.right)
                    and node.right.val == node.val
                )
            )
        )
    
    def preorder(node):
        if node is not None:
            yield node
            yield from preorder(node.left)
            yield from preorder(node.right)
    
    count = 0
    for node in preorder(root):
        if unival(node):
            count += 1
    return count


print(memo(tree)) #=> 5
print(univals(tree)) #=> 5
    