class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
        
        
        
        
    def insert(self, new_val):
        'Insearts new values in the tree according to the rule: smaller - to the left, gtreater - to the right'
        root = self.root
        self.insert_help(root, Node(new_val))

    def insert_help(self, root, new_val):
        'Recursive helper function'
        if root is None:
            # when hit the free spot, insert new value
            root = new_val
        else:
            if root.value > new_val.value:
                # look left
                if root.left is None:
                    # found free spot => insert new value
                    root.left = new_val
                else:
                    # go down the tree to the left child
                    self.insert_help(root.left, new_val)
            else:
                # look right
                if root.right is None:
                    # found free spot => insert new value
                    root.right = new_val
                else:
                    # go down the tree to the right child
                    self.insert_help(root.right, new_val)
                    
                    
                    
                    
            
    def search(self, find_val):
        'Searches for the given value in the tree using helper function'
        start = self.root
        return self.helper_search(start, find_val)
        
    
    def helper_search(self, start, find_val):
        'Recursive helper function'
        if find_val < start.value:
            # look left
            if start.left == None:
                return False
            return self.helper_search(start.left, find_val)
        elif find_val > start.value:
            # look right
            if start.right == None:
                return False
            return self.helper_search(start.right, find_val)
        else:
            # find_val = start.value => found!!!!
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




    
