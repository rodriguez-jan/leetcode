# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_count = 0
        
        #Bottom up, post order 
        #Every node needs previous info of:
        #1 if everything below it is valid subtree
        #2 greatest value from left subtree
        #3 least value from right subtree
        #4 the sizes of the subtree
        
        
        def isValidBST(node):
            if not node:return True, float('inf'), float('-inf'),0
            isLeftValid, leftMin,leftMax,lSize = isValidBST(node.left)
            isRightValid, rightMin,rightMax,rSize = isValidBST(node.right)
            isValid = isLeftValid and isRightValid and node.val> leftMax and node.val<rightMin
            size = lSize+rSize+1
            if isValid:self.max_count = max(self.max_count,size)
            return isValid,min(leftMin,node.val),max(rightMax,node.val),size
        
            
        
        isValidBST(root)
        return self.max_count
                
            
            
            
        
            
            
                
