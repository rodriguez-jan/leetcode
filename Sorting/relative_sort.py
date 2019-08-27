class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        temp = []
        arr1.sort()
        for i in arr2:
            for j in arr1:
                if(j==i):
                    temp.append(j)

        for end in arr1:
            if end not in arr2:
                temp.append(end)
        return temp