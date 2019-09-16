class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        memo = set()
        result = []
        
        def perm(current, left, right):
            if left == right:
                result.append(current)
                return
            temp = left+right
            for i,e in enumerate(temp):
                perm(current+ [temp[i]],temp[:i],temp[i+1:])
            
        perm([],nums,[])
        return result
        
