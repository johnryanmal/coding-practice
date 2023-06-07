
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is None:
        return ''

    if node.left is not None or node.right is not None:
        return f'{node.val}({serialize(node.left)},{serialize(node.right)})'
    else:
        return f'{node.val}'


def deserialize(string):
    if string == '':
        return None

    #token types
    NUMBER = 0
    L_PAREN = 1
    R_PAREN = 2
    COMMA = 3

    def tokens(string):
        digits = ''
        negative = False
        for char in string:
            if char == '-' or '0' <= char <= '9':
                digits += char
                continue

            if digits:
                yield NUMBER, digits
                digits = ''

            if char == '(':
                yield L_PAREN, char
            elif char == ')':
                yield R_PAREN, char
            elif char == ',':
                yield COMMA, char
            else:
                raise ValueError(f"Unexpected character '{char}'")
        if digits:
            yield NUMBER, digits

    #states
    CURR = 0
    LEFT = 1
    RIGHT = 2
    UP_RIGHT = 3


    root = Node(None)
    curr = root
    stack = []
    state = CURR
    for token, value in tokens(string):
        if token == NUMBER:
            if state == CURR:
                curr.val = value
            elif state == LEFT:
                node = Node(value)
                curr.left = node
                stack.append(curr)
                curr = node
            elif state == RIGHT:
                node = Node(value)
                curr.right = node
                stack.append(curr)
                curr = node
            elif state == UP_RIGHT:
                if stack:
                    node = Node(value)
                    stack[-1].right = node
                    curr = node
            state = CURR
        elif token == L_PAREN:
            state = LEFT
        elif token == COMMA:
            if state == CURR:
                state = UP_RIGHT
            elif state == LEFT:
                state = RIGHT
        elif token == R_PAREN:
            if stack:
                curr = stack.pop()
                state = UP_RIGHT

    return root


# Tree:

#   1
#  / \
#  2 3
# /
# 4

tree = Node(1, Node(2, Node(4)), Node(3))
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)

string = serialize(tree)
print(string)

print('---')

tree2 = deserialize(string)
print(tree2.val)
print(tree2.left.val)
print(tree2.right.val)
print(tree2.left.left.val)
print(serialize(tree2))
