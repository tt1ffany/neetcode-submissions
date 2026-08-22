class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]   # return pair of new index found, current index checking
            map[n] = i  # add to hashmap if no solution found (for this value n, index is i)
        return