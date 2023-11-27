from BST import BST

class BST_test():
  
  def __init__(self):
    
    self.tree = BST()
      
  def create_tree(self):
    
    new_node = Tree_Node(9)
    self.tree.root = new_node
      
    new_node.left = Tree_Node(2)
    new_node.right = Tree_Node(13)
      
    new_node.left.left = Tree_Node(3)
    new_node.left.right = Tree_Node(5)
    new_node.right.left = Tree_Node(11)
    new_node.right.right = Tree_Node(18)

    return self.tree 
    
  def test_bfs(self):
    
    bst = self.create_tree()
    
    assert bst.root is not None, 'Root must exist'
    assert bst.bfs() == [9, 2, 13, 3, 5, 11, 18], f'Expected [9, 2, 13, 3, 5, 11, 18], received: {bst.bfs()}'

    print("BFS test passed")
        
  def test_dfs(self):

    bst = self.create_tree()

    assert bst.root is not None, 'Root must exist'
    assert bst.dfs() == [9,2,3,5,13,11,18], f'Expected [9,2,3,5,13,11,18], received: {bst.dfs()}'

    print("DFS test passed")

  def test_is_empty(self):
    
    bst = BST()

    assert bst.is_empty() == True, 'bst must be empty'

    bst = self.create_tree()

    assert bst.is_empty() == False, 'bst is not empty'

    print("is empty test passed")

  def test_contains(self):

    bst = self.create_tree()

    assert bst.root is not None, 'Root must exist'

    assert bst.contanins(5) == True, 'Expected True'
    assert bst.contanins(18) == True, 'Expected True'
    assert bst.contanins(4) == False, 'Expected False'

    print("contanins test passed")


'''                              (9)
                                /   \
                               /     \
                              /       \
                            (2)       (13)
                           /  \       / \
                          /    \     /   \
                        (3)    (5) (11)  (18)
                        
          
 '''

t = BST()
t.test_bfs()
t.test_dfs()
t.test_is_empty()
t.test_contains()

