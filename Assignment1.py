import unittest
from sys import stdout


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, val):
        return self.val < val

    def __gt__(self, val):
        return self.val > val

    def __eq__(self, val):
        return self.val == val

    def __str__(self):
        return "[Node val: %d]" % self.val


class Tree(object):
    def __init__(self):
        self.root = None

    def put(self, val):
        self.root = self._put(self.root, val)

    def _put(self, node, val):
        if node is None:
            node = Node(val)

        if val < node:
            node.left = self._put(node.left, val)
        elif val > node:
            node.right = self._put(node.right, val)
        else:
            node.val = val

        return node

    def get(self, val):
        return self._get(self.root, val)

    def _get(self, node, val):
        while not node is None:
            if val < node: node = node.left
            elif val > node: node = node.right
            else: return node.val

        return None

    # This method returns `None` if no common is found
    def find_common(self, a, b):
        return self._find_common(self.root, a, b)

    def _find_common(self, node, a, b):
        # Traverse right until a diverge occurs
        if a > node and b > node:
            if node.right is None: return None

            # if right node is `a` or `b` then we found common
            if node.right == a or node.right == b:
                return node.val

            return self._find_common(node.right, a, b)

        # Traverse left until a diverge occurs
        elif a < node and b < node:
            if node.left is None: return None

            # if left node is `a` or `b` then we found common
            if node.left == a or node.left == b:
                return node.val

            return self._find_common(node.left, a, b)

        # root does not have any common ancestor
        # This test is later because we dont want the
        # recursion to hit it every time
        elif a == self.root or b == self.root:
            return None

        else:
            # A diverge of the tree traversal occurs here
            # So the current node is a potential common ancestor
            # Verify that a and b are legitimate nodes
            if self._node_exists(node, a):
                # `a` exists ensure `b` exists
                if self._node_exists(node, b):
                    # Common ancestor is validated
                    return node.val
                else:
                    return None
            else:
                return None

    def node_exists(self, val):
        return self._node_exists(self.root, val)

    def _node_exists(self, node, val):
        return not self._get(node, val) is None

if __name__ == "__main__":
    from sys import stdout
    vals = [30, 8, 52, 3, 20, 10, 29, 62]
    tree = Tree()
    [tree.put(val) for val in vals]
    pairs = [
        (3, 20),
        (3, 29),
        (10, 29),
        (20, 52),
        (3, 62),
        (4, 29),
        (3, 1),
        (8, 3),
        (8, 20)
    ]
    for (a, b) in pairs:
        stdout.write("Common for %d & %d: " % (a, b))
        print (tree.find_common(a, b))
    unittest.main()

    def print_tree(self):
        _print_tree(self.root)


    def _print_tree(self, node):

        if node is None:
            print("")
            return

        if node.left is None:
            print("")
            return
        else:
            _print_tree(node.left)

        if node.right is None:
            print("")
            return
        else:
            _print_tree(node.right)


class TestStringMethods(unittest.TestCase):

    def test_constructor(self):
        tree = Tree()
        self.assertEqual(tree.root, None)

    def test_empty_tree(self):
        tree = Tree()
        self.assertEqual(tree.find_common(1, 2), None)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    #unittest.main()
    vals = [1, 2, 3]
    tree = Tree()
    for val in vals:
        tree.put(val)

    tree.print_tree()
    
