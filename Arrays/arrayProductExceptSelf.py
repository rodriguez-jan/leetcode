class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        lProduct = [0]*length
        rProduct = [0]*length
        res = [0]*length
        
        #Calculate left product values
        lProduct[0] = 1
        for i in range(1,length):
            lProduct[i] = lProduct[i-1] * nums[i-1]
         #Calculate right product values
        rProduct[-1] = 1
        for i in range(length-2,-1,-1):
            rProduct[i] = rProduct[i+1] * nums[i+1]
        
        #Multiply left and right based on indices
        for i in range(length):
            res[i] = lProduct[i] * rProduct[i]
        return res
