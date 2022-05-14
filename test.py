#import random, math


def random_list_generator(len):
    res = []
    for i in range(len):
        x = random.randint(1, len)
        if x not in res:
            res.append(x)
    return res
  
  
def random_data_generator(len):
  for i in range(len):
      yield random.randint(1, len)
        
        
def testkth(l=10000, p = 1000, q =10000):
    lst = random_list_generator(l)
    c = AVLTree(lst)
    lst.sort()
    
    # Let's test kth after some appends
    for i in range(1,len(lst)+1):
        assert c.findkth(i)==lst[i-1], f'wrong {i}-th answer!'
    
    # Let's do some removes
    for k in range(p):
        x = random.randint(1,q)
        if not x in lst:
            continue
        else:
            lst.remove(x)
            c.remove(x)  
            
    # Let's test kth after some removes
    lst.sort()
    for i in range(1,len(lst)+1):
        assert c.findkth(i)==lst[i-1], f'wrong {i}-th answer!'         
        
        
def testsize(l=1000000):
    tree = AVLTree()
    for val in random_data_generator(l):
        tree.insert(val)
    assert (tree.height() < 1.44 * math.log(l+2, 2) - 1)
    return tree.elements_count, tree.height()
  
  
if __name__ == "__main__": 
    testkth()
    testsize()    
