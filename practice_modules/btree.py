#! /usr/bin/env python

def binary_tree(r):
    return [r, [], []]


def insert_left(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insert_right(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_Val(root, newVal):
    root[0] = newVal


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def build_tree():
    tree = binary_tree('a')
    insert_left(tree, 'b')
    insert_right(tree, 'c')
    insert_right(get_left_child(tree), 'd')
    insert_left(get_right_child(tree), 'e')
    insert_right(get_right_child(tree), 'f')
    return tree


class BinaryTree(object):
    """docstring for binaryTree"""
    def __init__(self, root_object):
        super(BinaryTree, self).__init__()
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, key):
        if self.left_child is None:
            self.left_child = BinaryTree(key)
        else:
            (self.left_child,
             self.left_child.left_child) = (BinaryTree(key),
                                            self.left_child)

    def insert_right(self, key):
        if self.right_child is None:
            self.right_child = BinaryTree(key)
        else:
            (self.right_child,
             self.right_child.right_child) = (BinaryTree(key),
                                              self.right_child)

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, key):
        self.key = key

    def get_root_val(self):
        return self.key


def build_tree_w_class():
    tree = BinaryTree('a')
    tree.insert_left('b')
    tree.insert_right('c')
    tree.get_left_child().insert_right('d')
    tree.get_right_child().insert_left('e')
    tree.get_right_child().insert_right('f')
    return tree


def build_parse_tree(fpexp):
    # fplist = fpexp.split()
    fplist = list(fpexp)
    pstack = []
    etree = BinaryTree('')
    pstack.append(etree)
    current_tree = etree

    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pstack.append(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '/', '*', '**', ')']:
            current_tree.set_root_val(int(i))
            current_tree = pstack.pop()
        elif i in ['+', '-', '/', '*', '**']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            pstack.append(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pstack.pop()
        else:
            raise ValueError
    return etree


def evaluate_parse_tree(ptree):
    import operator
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    lchild = ptree.get_left_child()
    rchild = ptree.get_right_child()

    if lchild and rchild:
        func = operators[ptree.get_root_val()]
        return func(evaluate_parse_tree(lchild), evaluate_parse_tree(rchild))

    else:
        return ptree.get_root_val()


if __name__ == '__main__':
