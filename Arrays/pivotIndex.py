class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        left_sum = 0
        
        #calculate right sum by doing total - left_sum - index
        
        for i in range(len(nums)):
            if(left_sum == total - left_sum - nums[i]):
                return i
            left_sum += nums[i]
            
        return -1