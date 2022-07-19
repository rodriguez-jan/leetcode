class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def make_adj_list(manager):
            adj_list = [[] for i in manager]
            
            for index,val in enumerate(manager):
                if val != -1:
                    adj_list[val].append(index)
            
            return adj_list
        
        #want to traverse through adj_list and add the cost of the dfs travels from the root and return the max
        #max_time is the max cost of dfs traversal
        def dfs(vertex,seen,adj_list,inform_time,max_time) -> int:

            if not adj_list[vertex]:
                return 0
            seen.add(vertex)
            max_time = 0
            for emp in adj_list[vertex]:
                if emp not in seen:
                    max_time = max(max_time, dfs(emp,seen,adj_list,inform_time,max_time))
            return max_time + inform_time[vertex]
        
        if n == 1:
            return 0
        adj_list = make_adj_list(manager)
        print(adj_list)
        seen = set()
        max_time = 0
        max_time = dfs(headID,seen,adj_list,informTime,max_time)
        return max_time
    
        
        #so we were close, it was just that our solution was adding too much to the answer
        #how do we think of the computes that we need to do and the the return statements that we want
        
        #we have two base cases, one where we return from empty employee, should be zero, cause no time. makes sense
        #we sift those return values up the tree, essentially for every node, once we start returning we want to know that we have the max inform time from its children
        #then we want to pass it up
        #we actually do not know the max return time at the bottom of the tree
        #return statements in dfs is essentially what info we know from this traversal so far

        #also we did not need a seen array because we knew this is a non clyclic graph

        #in general for return statements in a dfs solution, we will have a base case return and a return on the bottom of the call when were done and want to sift the values back up