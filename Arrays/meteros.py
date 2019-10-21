class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        #iterate through asteroids right through left
        #place positive items onto stack
        #if we hit negative then couple conditions
        #if stack empty, then it passes through and gets appended to answer
        #if not empty, compare to last item, and see if bigger
        #go through all stack elements until stack item >= to curr neg item
        
        res = []
        s = []
        for curr in asteroids:
            if s:
                while s:
                    if curr >0:
                        s.append(curr)
                        break
                    else:
                        if curr > -s[-1]:
                            break
                        elif curr == -s[-1]:
                            s.pop()
                            break
                        else:
                            s.pop()
                            if not s:
                                res.append(curr)
            else:
                if curr >0:
                    s.append(curr)
                else:
                    res.append(curr)
        res.extend(s)
        return res
