class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        
        #iterate through all possible arnges
        #from each range, find the min and max in nums and subtract to add to res
        
        #start of subarray
        for index in range(n):
            low, high = nums[index],nums[index]
            #start of contiguos subarrays after the element we are on
            for j in range(index,n):
                low = min(nums[j],low)
                high = max(nums[j],high)
                res+= high-low
        
        return res