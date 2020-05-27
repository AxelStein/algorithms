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


class BST:
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
                return BST._get_child(node)

        if val < node.val:
            node.left = self._delete(node.left, val)
        else:
            node.right = self._delete(node.right, val)

        return node

    def find_node(self, val):
        return self._find_node(self.root, val)

    def _find_node(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self._find_node(root.left, val)
        else:
            return self._find_node(root.right, val)

    @staticmethod
    def _get_child(node):
        if node:
            if node.left:
                return node.left
            elif node.right:
                return node.right
        return None

    def _find_min(self, root):
        if root is None:
            return None
        if not root.left:
            return root
        else:
            return self._find_min(root.left)

    def _print_tree(self, root):
        if root:
            print(root)
            self._print_tree(root.left)
            self._print_tree(root.right)

    def __str__(self):
        self._print_tree(self.root)
        return "----"


bst = BST()
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(9)
bst.insert(7)
bst.insert(6)
bst.insert(8)
bst.insert(2)
bst.insert(10)

print(bst)

print("delete 2")
bst.delete(2)
print(bst)

print("delete 1")
bst.delete(1)
print(bst)

print("delete 7")
bst.delete(7)
print(bst)

print("delete 5")
bst.delete(5)
print(bst)
