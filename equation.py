import math
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': math.pow,
              'abs': abs, 'sqrt': math.sqrt, 'cos': math.cos, 'sin': math.sin}


class Node:
    def __init__(self, value):
        self.value = value
        self.root = None
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = Node(value)

    def insert_right(self, value):
        if self.right is None:
            self.right = Node(value)

    def set_value(self, value):
        self.value = value

    def set_root(self, root):
        self.root = root


def compute(root):
    if root.left and root.right:
        op = operations[root.value]
        return op(compute(root.left), compute(root.right))
    elif root.left:
        op = operations[root.value]
        return op(compute(root.left))
    else:
        return root.value


def parse(array):
    root = Node('')
    current = root
    for t in array:
        if t == '(':
            current.insert_left('')
            current.left.set_root(current)
            current = current.left
        elif t == ')':
            if current.root:
                current = current.root
            else:
                return root
        elif t.isdigit():
            current.set_value(t)
            current = current.root
        elif t == 'pi':
            current.set_value(math.pi)
            current = current.root
        elif t in ['+', '-', '*', '**', '/']:
            current.set_value(t)
            current.insert_right('')
            current.right.set_root(current)
            current = current.right
        elif t in ['sqrt', 'abs', 'cos', 'sin']:
            current.set_value(t)
            current.insert_left('')
            current.left.set_root(current)
            current = current.left
        else:
            current.set_value(t)
            current.insert_right('')
            current.right.set_root(current)
            current = current.right
