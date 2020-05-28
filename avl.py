class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        arr = [str(self.val), ' -> ']
        if self.left:
            arr.append(str(self.left.val))
        else:
            arr.append(".")
        arr.append(' - ')
        if self.right:
            arr.append(str(self.right.val))
        else:
            arr.append(".")
        return ''.join(arr)


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        bf = self._get_height(node.right) - self._get_height(node.left)
        if bf < -1:
            return self._rotate_right(node)
        if bf > 1:
            return self._rotate_left(node)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if node.val == val:
            # two children case
            if node.left and node.right:
                # find the most left node in the right subtree
                # swap values and remove leaf node
                tmp = self._find_min(node.right)
                node.val = tmp.val
                node.right = self._delete(node.right, tmp.val)
            else:
                return AVL._get_child(node)

        if val < node.val:
            node.left = self._delete(node.left, val)
        else:
            node.right = self._delete(node.right, val)

        bf = self._get_height(node.right) - self._get_height(node.left)
        if bf < -1:
            return self._rotate_right(node)
        if bf > 1:
            return self._rotate_left(node)

        return node

    def find_node(self, val):
        return self._find_node(self.root, val)

    def _find_node(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        if val < node.val:
            return self._find_node(node.left, val)
        else:
            return self._find_node(node.right, val)

    @staticmethod
    def _rotate_right(node):
        next_node = node.left
        node.left = next_node.right
        next_node.right = node
        return next_node

    @staticmethod
    def _rotate_left(node):
        next_node = node.right
        node.right = next_node.left
        next_node.left = node
        return next_node

    def _get_height(self, node):
        if node is None:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    @staticmethod
    def _get_child(node):
        if node:
            if node.left:
                return node.left
            elif node.right:
                return node.right
        return None

    def _find_min(self, node):
        if node is None:
            return None
        if not node.left:
            return node
        else:
            return self._find_min(node.left)

    def _print_tree(self, node):
        if node:
            print(node)
            self._print_tree(node.left)
            self._print_tree(node.right)

    def __str__(self):
        self._print_tree(self.root)
        return "----"


avl = AVL()
for i in range(1, 11):
    avl.insert(i)
"""
avl.insert(5)
avl.insert(1)
avl.insert(3)
avl.insert(4)
avl.insert(9)
avl.insert(7)
avl.insert(6)
avl.insert(8)
avl.insert(2)
avl.insert(10)
"""

print(avl)

print("delete 2")
avl.delete(2)
print(avl)

print("delete 1")
avl.delete(1)
print(avl)

print("delete 7")
avl.delete(7)
print(avl)

print("delete 5")
avl.delete(5)
print(avl)
