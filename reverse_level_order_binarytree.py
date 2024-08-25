'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    # code here
    if not root:
        return []
    queue=deque()
    queue.append(root)
    res=[]
    while queue:
        length=len(queue)
        levels=[]
        i=0
        while i<length:
            node=queue.popleft()
            levels.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i+=1
        res.append(levels)
        # we are appending multiple lists to result list , hence we need two loops to flatten it 
    return [val for j in reversed(res) for val in j]