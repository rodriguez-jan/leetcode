class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def build(st):
            res = []
            for i in st:
                if i != "#":
                    res.append(i)
                elif res:
                    res.pop()
            
            return str(res)
        
        return build(S) == build(T)
        
