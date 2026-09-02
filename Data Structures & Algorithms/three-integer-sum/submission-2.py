class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # smallest numbers now on left and biggest on right
        result = []

        for i in range(len(nums) - 2):
            # if starting value is greater than 0, only positive numbers proceed (can't sum to 0)
            if nums[i] > 0:
                break
            # if value same as previous for i > 0, then skip this iteration (would produce same triplets)
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                # if sum less than target, need bigger numbers, move left pointer
                if current_sum < 0:
                    l += 1
                # if greater than target, need smaller numbers, move right pointer
                elif current_sum > 0:
                    r -= 1
                # if equals, then triplet found
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip duplicate values for l and r (before searching remaining)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # then look for any remaining triplets with current i
                    l += 1
                    r -= 1

        return result
