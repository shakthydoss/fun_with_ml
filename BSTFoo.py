class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insertNode(self.root,val)

    def insertNode(self, current_node, val):
        if val <= current_node.val:
            # insert into left 
            if current_node.left_child is None:
                current_node.left_child = Node(val)
            else:
                self.insertNode(current_node.left_child, val)
        else:
            # insert into right 
            if current_node.right_child is None:
                current_node.right_child = Node(val)
            else:
                self.insertNode(current_node.right_child, val)
