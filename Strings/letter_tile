class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        result  = set()
        
        def permute(current, remaining):
            if current not in result:
                if current:
                    result.add(current)
                for i,e in enumerate(remaining):
                    permute(current+remaining[i], remaining[:i] + remaining[i+1:])
                    
        permute('',tiles)
        return len(result)
