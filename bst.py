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
bst.print_tree(bst.root)

print("----")
print(bst.find_node(bst.root, 8))
print(bst.find_node(bst.root, 2))
