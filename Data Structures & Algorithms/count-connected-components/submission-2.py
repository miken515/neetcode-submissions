class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {v:-1 for v in range(n)}

        def find(u):
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        
        res = n
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u != parent_v:
                res -= 1
                parent[parent_v] = parent_u
        
        return res
