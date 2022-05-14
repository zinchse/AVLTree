# AVLTree (Python 3)
AVLTree implementation with pretty print and built-in k-th find

## Why did I do it


AVL tree is one of the most powerful yet simple data structures. To my surprise, I did not find on the Internet any implementation of this structure with a nice tree visualization.
So I decided to do it myself. Besides, he immediately began to support the subtree size parameter for each nodes and implemented, on the basis of this, the search for k-th statistics on the tree.

I based on the following [implementation](https://github.com/pgrafov/python-avl-tree/blob/master/pyavltree.py).
Also for a complete understanding of all rotations and other operations, I advise you to read the following [article](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/).

## Overview

The AVL tree is a special case of a search tree that maintains some invariant related to the heights of the children. 
This allows you to maintain the speed of inserting and deleting an element of the order of the logarithm of the number of vertices in the tree.


## Interface examples

### Print

```
        >>> tree = AVLTree([1,2,3,4,5,6])
        >>> print(tree)
        >>>        4       
        >>>       / \        
        >>>      /   \       
        >>>     /     \      
        >>>    2       5   
        >>>   / \       \      
        >>>  1   3       6
```        

### Remove
```        
        >>> tree = AVLTree([1,2,3,4,5,6])
        >>> tree.remove(3)
        >>> print(tree)   
        >>>        4       
        >>>       / \        
        >>>      /   \       
        >>>     /     \      
        >>>    2       5   
        >>>   /         \      
        >>>  1           6         
```                
### k-th find        
```               
        >>> tree = AVLTree([1,2,3,4,5,6])
        >>> tree.findkth(2) 
        >>> 2
        >>> tree.findkth(2,tree.rootNode.rightChild)
        >>> 6  
```        

## File structure

```
+-- AVLTree.py/ contains an implementation of the class avl tree based on the node
+-- Node.py/ contains node implementation
+-- test.py/ simple check of work of search of ku statistics and maintenance of height of the order of a logarithm
```
**If it helps you** or you just find it funny, please upvote a star

Good luck!
