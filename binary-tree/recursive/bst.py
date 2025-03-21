class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root = None

    def dfs(node):
        if node == None:
            return

        dfs(node.left)
        dfs(node.right)
        return