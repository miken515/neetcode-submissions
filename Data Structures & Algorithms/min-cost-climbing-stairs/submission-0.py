class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            oneJump = cost[i + 1]
            twoJump = cost[i + 2]
            cost[i] += min(oneJump, twoJump)
            print(cost)

        return min(cost[0], cost[1])