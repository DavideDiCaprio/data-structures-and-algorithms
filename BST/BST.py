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

    # time complexity O(log n)
    def contanins(self,val):
      
      if self.root is None:
        return False
        
      curr_node = self.root
      
      while curr_node:
        if curr_node.key == val:
          return True

        if val < curr_node.key:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
      return False

    def insert(self,x):
      pass
