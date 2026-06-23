class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start = 0
            end = 1
            if newInterval[start] > intervals[i][end]:
                res.append(intervals[i])
            elif newInterval[end] < intervals[i][start]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [
                    min(newInterval[start], intervals[i][start]),
                    max(newInterval[end], intervals[i][end])
                ]
        
        res.append(newInterval)
        return res