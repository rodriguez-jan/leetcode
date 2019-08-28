# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def recursiveConvert(self, left_index, right_index):
            if left_index > right_index:
                return None
            mid = (left_index + right_index) / 2
            temp = TreeNode(nums[mid])
            temp.left = recursiveConvert(self, left_index, mid - 1)
            temp.right = recursiveConvert(self, mid + 1, right_index)
            return temp

        return recursiveConvert(self, 0, len(nums) - 1)







