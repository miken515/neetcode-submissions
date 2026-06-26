# Find Median In A Data Stream Solution
#
# This solution implements an efficient algorithm for the find median in a data stream problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        

    def addNum(self, num: int) -> None:
        """Method: addNum"""
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num) # multiple -1 to make it a max heap

        # uneven sizes
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

        

    def findMedian(self) -> float:
        """Method: findMedian"""
        smallLength = len(self.small)
        largeLength = len(self.large)

        if smallLength < largeLength:
            return self.large[0]
        elif smallLength > largeLength:
            return -1 * self.small[0]
        
        smallVal = -1 * self.small[0]
        largeVal = self.large[0]

        return (smallVal + largeVal) / 2
        
        