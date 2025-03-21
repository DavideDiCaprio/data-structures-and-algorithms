def print_tree(root):
    if not root:
        print("Empty Tree")
        return
    
    # Get the height of the tree
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1
    
    h = height(root)
    
    # Width of the tree display
    width = 2**(h+1) - 1
    
    # Create a 2D matrix to represent the tree
    matrix = [[' ' for _ in range(width)] for _ in range(2*h - 1)]
    
    # Fill the matrix with the tree representation
    def fill_matrix(node, row, left, right):
        if not node:
            return
        
        # Calculate middle position
        mid = (left + right) // 2
        
        # Place the node value - use str(node.val) here to access the value
        matrix[row][mid] = str(node.val)
        
        # Draw connections to children
        if node.left:
            # Calculate left child position
            child_mid = (left + mid - 1) // 2
            
            # Draw the connection line
            for i in range(1, mid - child_mid):
                matrix[row + 1][mid - i] = '/'
            
            fill_matrix(node.left, row + 2, left, mid - 1)
        
        if node.right:
            # Calculate right child position
            child_mid = (mid + 1 + right) // 2
            
            # Draw the connection line
            for i in range(1, child_mid - mid):
                matrix[row + 1][mid + i] = '\\'
            
            fill_matrix(node.right, row + 2, mid + 1, right)
    
    fill_matrix(root, 0, 0, width - 1)
    
    # Print the matrix
    for row in matrix:
        print(''.join(row))