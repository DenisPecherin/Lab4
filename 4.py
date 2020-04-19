# Напишите процедуры нерекурсивных обходов бинарного
# дерева:
# a) префиксного;
# b) инфиксного;
# c) постфиксного;
# d) поуровневого.
from collections import namedtuple

Node = namedtuple('Node', 'data, left, right') # дерево
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))


def printwithspace(i):
    print(i, end=' ')


def dfs(order, node, visitor): 
    if node is not None:
        for action in order:
            if action == 'N':
                visitor(node.data)
            elif action == 'L':
                dfs(order, node.left, visitor)
            elif action == 'R':
                dfs(order, node.right, visitor)


def prefix(node, visitor=printwithspace): # префиксный
    dfs('NLR', node, visitor)


def infix(node, visitor=printwithspace): # инфиксный
    dfs('LNR', node, visitor)


def postfix(node, visitor=printwithspace): # постфиксный
    dfs('LRN', node, visitor)


def ls(node, more, visitor, order='TB'):
    if node:
        if more is None:
            more = []
        more += [node.left, node.right]
    for action in order:
        if action == 'B' and more:
            ls(more[0], more[1:], visitor, order)
        elif action == 'T' and node:
            visitor(node.data)


def level(node, more=None, visitor=printwithspace): # поуровневый
    ls(node, more, visitor, 'TB')


if __name__ == '__main__':
    w = 10
    for traversal in [prefix, infix, postfix, level]:
        print(f"{traversal.__name__:>{w}}:", end=' ')
        traversal(tree)
        print()
