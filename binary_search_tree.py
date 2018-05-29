class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        node = self.root
        self.helper_insert(node, new_val)
    
    def helper_insert(self, node, new_val):
        if node == None:
            node = Node(new_val)
        if new_val < node.value:
            return self.helper_insert(node.left, new_val)
        elif new_val > node.value:
            return self.helper_insert(node.right, new_val)
        return
            
    def search(self, find_val):
        start = self.root
        return self.helper_search(start, find_val)
        
    
    def helper_search(self, start, find_val):
        if find_val < start.value:
            if start.left == None:
                return False
            return self.helper_search(start.left, find_val)
        elif find_val > start.value:
            if start.right == None:
                return False
            return self.helper_search(start.right, find_val)
        else:
            return True
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
