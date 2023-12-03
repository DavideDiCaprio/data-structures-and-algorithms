from Binary_Search_Tree import Binary_Search_Tree, Tree_Node

class Binary_Search_Tree_test():
  
  
    def __init__(self):
        self.tree = Binary_Search_Tree()
      
      
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
        assert bst.dfs() == [9, 2, 3, 5, 13, 11, 18], f'Expected [9, 2, 3, 5, 13, 11, 18], received: {bst.dfs()}'
        print("DFS test passed")


    def test_is_empty(self):
    
        bst = Binary_Search_Tree()
        assert bst.is_empty() == True, 'bst must be empty'
        bst = self.create_tree()
        assert bst.is_empty() == False, 'bst is not empty'
        print("is empty test passed")


    def test_contains(self):
    
        bst = self.create_tree()
        assert bst.root is not None, 'Root must exist'
        assert bst.contains(5) == True, 'Expected True'
        assert bst.contains(18) == True, 'Expected True'
        assert bst.contains(4) == False, 'Expected False'
        print("contains test passed")
        
        
    def test_insert(self):

      bst = Binary_Search_Tree()
      bst.insert(9)

      assert bst.root is not None, 'Root must be exist'
      assert bst.root.key == 9, f'Expected 9, got {bst.root.key}'

      bst.insert(2)

      assert bst.root.left is not None, 'Right child must exist'
      assert bst.root.left.key == 2, f'Expected 2, got {bst.root.right.key}'

      bst.insert(11)

      assert bst.root.right is not None, 'Right child must exist'
      assert bst.root.right.key == 11, f'Expected 11, got {bst.root.right.key}'

      bst.insert(10)
      bst.insert(3)
      bst.insert(1)

      assert bst.root.right.left.key == 10, f'Expected 11, got {bst.root.right.left.key}'
      assert bst.root.left.right.key == 3, f'Expected 3, got {bst.root.left.right.key}'
      assert bst.root.left.left.key == 1, f'Expected 1, got {bst.root.left.left.key}'

      print("insert test passed")
    
    
    def run_tests(self):
    
        self.test_bfs()
        self.test_dfs()
        self.test_is_empty()
        self.test_contains()
        self.test_insert()
      
      
def main():

    test = Binary_Search_Tree_test()
    test.run_tests()


if __name__ == "__main__":
    main()




'''                              (9)
                                /   \
                               /     \
                              /       \
                            (2)       (13)
                           /  \       / \
                          /    \     /   \
                        (3)    (5) (11)  (18)
                        
          
 '''
 