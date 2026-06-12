class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map
        previousMap = {}

        for i, n in enumerate(nums):
            print('Previous Map:', previousMap)
            print('I,N', i, n)
            difference = target - n
            print('Target', target)
            print('Diff', difference)
            if difference in previousMap:
                return[previousMap[difference], i]
            previousMap[n] = i 
        return

# Create a map, enumerate, then it finds the difference, using that difference in the map, 
# If difference is not found in the map, we add the first num from the list to the mapp
# Window problem