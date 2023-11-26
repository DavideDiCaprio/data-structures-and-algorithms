from Stack import Stack 
from collections import deque


class Tree_Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BST:
    def __init__(self):
      self.root = None

    def bfs(self):
      q = deque()
      values = []
      if self.root:
        q.append(self.root)
        
      while q:
        curr_node = q.popleft()
        values.append(curr_node.key)
        
        if curr_node.left:
          q.append(curr_node.left)
          
        if curr_node.right:
          q.append(curr_node.right)

      return values

    #pre-order
    def dfs(self):

      if self.root is None:
        return
      
      values = []
      stack = Stack()
      stack.push(self.root)

      while not stack.is_stack_empty():

        curr_node = stack.pop()
        values.append(curr_node.key)

        if curr_node.right is not None:
          stack.push(curr_node.right)

        if curr_node.left is not None:
          stack.push(curr_node.left)

      return values

    def is_empty(self):
      if not self.root:
        return True
      return False

    def contanins(self,val):
      pass

    def create_tree(self):
      
      tree = BST()
      new_node = Tree_Node(9)
      tree.root = new_node
      
      new_node.left = Tree_Node(2)
      new_node.right = Tree_Node(13)
      
      new_node.left.left = Tree_Node(3)
      new_node.left.right = Tree_Node(5)
      new_node.right.left = Tree_Node(11)
      new_node.right.right = Tree_Node(18)

      return tree 

  '''                             
                                 (9)
                                /   \
                               /     \
                              /       \
                            (2)       (13)
                           /  \       / \
                          /    \     /   \
                        (3)    (5) (11)  (18)
                                             
'''
    
    def test_bfs(self):
      
      bst = self.create_tree()
        
      assert bst.root is not None, 'Root must exist'
      assert bst.bfs() == [9, 2, 13, 3, 5, 11, 18], f'Expected [1, 2, 7, 3, 5, 6, 10], received: {bst.bfs()}'
      print("BFS test passed")
        
    def test_dfs(self):

      bst = self.create_tree()

      assert bst.root is not None, 'Root must exist'
      assert bst.dfs() == [9,2,3,5,13,11,18], f'Expected [9,2,3,5,13,11,18], received: {bst.dfs()}'
      print("DFS test passed")

test = BST()
test.test_bfs()
test.test_dfs()
