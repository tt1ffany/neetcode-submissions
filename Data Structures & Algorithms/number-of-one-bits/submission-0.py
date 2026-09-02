class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n > 0:
            mod = n % 2
            if mod == 1:
                result += 1
            n = n >> 1

        return result