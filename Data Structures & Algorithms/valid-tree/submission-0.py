class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjlist = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

        visited = set()
        def dfs(i, prevN):
            if i in visited:
                return False
            
            visited.add(i)

            for j in adjlist[i]:
                if j == prevN:
                    continue
                
                if not dfs(j, i):
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n
            


