class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0

        def getMin():
            nonlocal p1, p2

            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == len(nums2):
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            
            return ans

        if (len(nums1) + len(nums2)) % 2 == 0:
            for i in range((len(nums1) + len(nums2)) // 2 - 1):
                i = getMin()
            
            return (getMin() + getMin()) / 2
        else:
            for i in range((len(nums1) + len(nums2)) // 2): 
                i = getMin()
            return getMin()