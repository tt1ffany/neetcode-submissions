class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # starting at step 3
        oneBefore = 2
        twoBefore = 1

        for i in range(3, n + 1):
            currentStep = oneBefore + twoBefore

            # update steps
            twoBefore = oneBefore # two steps before old current is one step before old current
            oneBefore = currentStep
        
        return oneBefore
