from collections import deque


class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class Binary_Search_Tree:
  def __init__(self):
    self.root = None

  def breadth_First_Search(self):
    q = deque()
    values = []

    if self.root:
      q.append(self.root)

    while q:
      level = []
      for _ in range(len(q)):
        curr = q.popleft()
        level.append(curr.key)
        if curr.left:
          q.append(curr.left)
        if curr.right:
          q.append(curr.right)
      values.append(level)
    return values

  def preorder_Traversal(self):
    if self.root is None:
      return

    values = []
    stack = [self.root]

    while stack:
      curr = stack.pop()
      values.append(curr.key)
      if curr.right:
        stack += [curr.right]
      if curr.left:
        stack += [curr.left]
    return values

  def postorder_Traversal(self):
    pass

  def inorder_Traversal(self):
    pass

  def insert(self, val):
    if not self.root:
      self.root = Node(val)
      return

    curr = self.root

    while curr:
      if curr.key > val:
        if curr.left is None:
          curr.left = Node(val)
          return
        else:
          curr = curr.left
      else:
        if curr.right is None:
          curr.right = Node(val)
          return
        else:
          curr = curr.right

  def delete(self, val):
    curr = self.root
    prev = None

    while curr!= None and curr.key != val:
      prev = curr
      if curr.key < val:
        curr = curr.right
      else:
        curr = curr.left

    if curr == None:
      return self.root

    if not curr.left and not curr.right:
      if not prev:
        return None
      if prev.left == curr:
        prev.left = None
      else:
        prev.right = None

    elif not curr.left or not curr.right:
      if not curr.left:
        child = curr.right
      else:
        child = curr.left
      if not prev:
        return child
      if prev.left == curr:
        prev.left = child
      else:
        prev.right = child

    else:
      successor_parent = curr
      successor = curr.right
      while successor.left:
        successor_parent = successor
        successor = successor.left
      curr.key = successor.key
      if successor_parent.left == successor:
        successor_parent.left = successor.right
      else:
        successor_parent.right = successor.right

  def contains(self, val):
    if self.root is None:
      return False
    curr = self.root
    while curr:
      if curr.key == val:
        return True
      if val < curr.key:
        curr = curr.left
      else:
        curr = curr.right
    return False