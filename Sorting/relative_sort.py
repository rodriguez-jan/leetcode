class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dict_sort = {}
        list_total = []
        list_diffs = []
        for i in arr2:
            dict_sort[i] = 0

        for i in arr1:
            if i in dict_sort:
                dict_sort[i] +=1
            else:
                list_diffs.append(i)
        list_diffs.sort()

        for i in arr2:
            list_total.extend([i] * dict_sort[i])

        list_total.extend(list_diffs)

        return  list_total
