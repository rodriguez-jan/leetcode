from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        
        #1
        #11
        #21
        #1211
        #111221
        def convertString(s: str):
            left = 0
            right = 0
            
            res = ""
            while right < len(s) :
                if s[left] == s[right]:
                    right+=1
                else:
                    res += str(right-left) + s[left]
                    left= right
            res += str(right-left) + s[left]
            return res
        
        #recurse through
        ans = ""
        for i in range(n):
            if i == 0:
                ans = "1"
            else:
                ans = convertString(ans)
        
        return ans
        
        return recurse(n)
            
        