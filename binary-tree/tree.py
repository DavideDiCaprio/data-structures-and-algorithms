from utils import print_tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two


print_tree(root)