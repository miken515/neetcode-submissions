# Kth Largest Integer In A Stream Solution
#
# This solution implements an efficient algorithm for the kth largest integer in a stream problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        """Method: add"""
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
