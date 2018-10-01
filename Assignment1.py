import unittest
from sys import stdout
from coverage import Coverage

cov = Coverage()
cov.set_option('report:show_missing', True)
cov.start()

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
        if node is None:
            return None
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


class TestStringMethods(unittest.TestCase):

    def test_constructor(self):
        tree = Tree()
        self.assertEqual(tree.root, None)

    def test_empty_tree(self):
        tree = Tree()
        self.assertEqual(tree.find_common(1, 2), None)

    def test_simple_tree(self):
        vals = [2, 1, 3, 3]
        tree = Tree()
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.find_common(1,3), 2)

    def test_one_node_tree(self):
        tree = Tree()
        tree.put(2)

        self.assertEqual(tree.find_common(2,2), None)

    def test_order(self):
        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.find_common(3, 20), 8)
        self.assertEqual(tree.find_common(20, 3), 8)

    def test_complex_tree(self):
        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        #Test all scenarios
        self.assertEqual(tree.find_common(3, 29), 8)
        self.assertEqual(tree.find_common(10, 29), 20)
        self.assertEqual(tree.find_common(20, 52), 30)
        self.assertEqual(tree.find_common(3, 62), 30)
        self.assertEqual(tree.find_common(4, 29), None)
        self.assertEqual(tree.find_common(29, 4), None)
        self.assertEqual(tree.find_common(3, 1), 8)
        self.assertEqual(tree.find_common(8, 3), 30)
        self.assertEqual(tree.find_common(8, 20), 30)
        self.assertEqual(tree.find_common(62, 52), 30)
        self.assertEqual(tree.find_common(10, 20), 8)
        self.assertEqual(tree.find_common(3, 8), 30)

    def test_not_in_tree(self):
        #test when the numbers are not in the tree
        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.find_common(4, 29), None)
        self.assertEqual(tree.find_common(29, 4), None)

    def test_get(self):
        #test the get function of Tree
        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.get(8), 8)
        self.assertEqual(tree.get(30), 30)

    def test_typeerror(self):
        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        #with self.assertRaises(TypeError):
        #    tree.find_common(4, 29)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


print("Hi")
unittest.main(exit=False)

print("Hi")

cov.stop()
#cov.save()
cov.report()
