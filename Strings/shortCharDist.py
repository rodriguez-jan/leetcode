class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        
        prev = float('-inf')
        for i,char in enumerate(S):
            if (char == C):
                prev = i
            res.append(i - prev);
        
        
        prev = float('inf')
        for j in range(len(S)-1,-1,-1):
            if(S[j] == C):
                prev = j
            res[j] = min(prev-j,res[j])
            
        return res
