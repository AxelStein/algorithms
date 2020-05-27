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
        self.remove_from = None

    def insert(self, root, val):
        if root is None:
            self.root = Node(val)
            return
        if val == root.val:
            return
        if val < root.val:
            if root.left:
                self.insert(root.left, val)
            else:
                root.left = Node(val)
        else:
            if root.right:
                self.insert(root.right, val)
            else:
                root.right = Node(val)

    def find_node(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.find_node(root.left, val)
        else:
            return self.find_node(root.right, val)

    def find_most_left_node(self, root):
        if root is None:
            return None
        if not root.left:
            return root
        else:
            return self.find_most_left_node(root.left)

    def remove(self, node, val):
        if node is None:
            return
        if not self.root:
            return
        if self.root.val == val:
            # fixme check children
            return

        if node.val == val:
            # two children case
            if node.left and node.right:
                # find the most left node in the right subtree
                s = self.find_most_left_node(node.right)
                node.val = s.val
                s.val = -1
                self.remove(node, -1)
            # one child case
            elif node.left or node.right:
                BST.swap_nodes(self.remove_from, node, BST.get_child(node))
            # no children case
            else:
                BST.swap_nodes(self.remove_from, node, None)
            self.remove_from = None
            return

        if node.left:
            self.remove_from = node
            self.remove(node.left, val)

        if node.right:
            self.remove_from = node
            self.remove(node.right, val)

    @staticmethod
    def swap_nodes(n1, n2, to):
        if BST.node_equals(n1.left, n2):
            n1.left = to
        elif BST.node_equals(n1.right, n2):
            n1.right = to

    @staticmethod
    def get_child(n):
        if n.left:
            return n.left
        if n.right:
            return n.right
        return None

    @staticmethod
    def node_equals(n1, n2):
        return n1 and n2 and n1.val == n2.val

    def print_tree(self, root):
        if root:
            print(root)
            self.print_tree(root.left)
            self.print_tree(root.right)


bst = BST()
bst.insert(bst.root, 5)
bst.insert(bst.root, 1)
bst.insert(bst.root, 3)
bst.insert(bst.root, 4)
bst.insert(bst.root, 9)
bst.insert(bst.root, 7)
bst.insert(bst.root, 6)
bst.insert(bst.root, 8)
bst.insert(bst.root, 2)
bst.insert(bst.root, 10)

bst.print_tree(bst.root)
print("----")

bst.remove(bst.root, 9)

print("----")
bst.print_tree(bst.root)

# bst.remove(bst.root, 3)
# bst.print_tree(bst.root)
# print("----")
