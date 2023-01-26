class Node:
    
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.rightChild = None
        self.leftChild = None         
        self.height = 0
        self.size = 1
        
    def __str__(self):
        return str(self.key)#+'('+str(self.height)+')'
    
    def is_leaf(self):
        return self.height == 0
    
    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.height,self.rightChild.height)
        elif self.leftChild:
            return self.leftChild.height
        elif self.rightChild:
            return self.rightChild.height
        else:
            return -1

    def balance(self):
        return (self.leftChild.height if self.leftChild else -1) -\
               (self.rightChild.height if self.rightChild else -1)
