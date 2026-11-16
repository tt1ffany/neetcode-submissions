class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current_combo, remaining):
            # Base case 1: found a valid combo
            if remaining == 0:
                res.append(current_combo.copy()) # save snapshot of current_combo
                return

            # Base case 2: exceeded target
            if remaining < 0:
                return

            # Explore candidates
            for i in range(start, len(nums)):
                # Make a choice
                current_combo.append(nums[i])

                # Recursive call
                backtrack(i, current_combo, remaining - nums[i])

                # Undo the choice
                current_combo.pop()

        backtrack(0, [], target)
        return res
