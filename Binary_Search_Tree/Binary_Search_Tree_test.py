from Binary_Search_Tree import Binary_Search_Tree, Node

class Binary_Search_Tree_test():

  def __init__(self):
    self.tree = Binary_Search_Tree()

  def create_tree(self):
    tree = Binary_Search_Tree()
    tree.root = Node(8)
    tree.root.left = Node(3)
    tree.root.right = Node(10)

    tree.root.left.left = Node(1)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(4)
    tree.root.left.right.right = Node(7)

    tree.root.right.right = Node(14)
    tree.root.right.right.left = Node(13)
    return tree

  def run_tests(self):
    self.breadth_First_Search_test()
    self.preorder_Traversal_test()
    self.insert_test()
    self.delete_test()
    self.contains_test()

  def breadth_First_Search_test(self):
    bst = self.create_tree()
    assert bst.root is not None, 'Root must exist'
    assert bst.breadth_First_Search() == [[8], [3, 10], [1, 6, 14], [4, 7, 13]], f'Expected [[8], [3, 10], [1, 6, 14], [4, 7, 13]], received: {bst.bfs()}'
    print("Breadth First Search test passed")

  def preorder_Traversal_test(self):
    bst = self.create_tree()
    assert bst.root is not None, 'Root must exist'
    assert bst.preorder_Traversal() == [8,3,1,6,4,7,10,14,13], f'Expected [8,3,1,6,4,7,10,14,13], received: {bst.preorder_Traversal()}'
    print("Preorder traversal test passed")

  def postorder_traversal_test(self):
    pass

  def inorder_traversal_test(self):
    pass

  def insert_test(self):
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

    print("Insert test passed")

  def delete_test(self):
    bst = self.create_tree()
    assert bst.root is not None, 'Root must exist'
    bst.delete(1)
    assert bst.root.left.left is None, f'Expected None, received {bst.root.left.left.key}'

    bst.delete(14)
    assert bst.root.right.right.key == 13, f'Expected 13, received {bst.root.right.right.key}'
    assert bst.root.right.right.left is None, f'Expected None, received {bst.root.right.right.left}'

    bst.delete(8)
    assert bst.root.key == 10, f'Expected 10, received {bst.root.key}'    
    print("Delete test passed")

  def contains_test(self):
    bst = self.create_tree()
    assert bst.root is not None, 'Root must exist'
    assert bst.contains(5) == False, 'Expected False'
    assert bst.contains(13) == True, 'Expected True'
    assert bst.contains(4) == True, 'Expected True'
    print("Contains test passed")


def main():
    test = Binary_Search_Tree_test()
    test.run_tests()

if __name__ == "__main__":
    main()



'''                              (8)
                                /   \
                               /     \
                              /       \
                            (3)       (13)
                           /  \       / 
                          /    \     /   
                        (1)    (6) (13)  
                               / \
                              /   \
                            (4)   (7)
          
 '''
 