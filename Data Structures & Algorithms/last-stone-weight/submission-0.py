class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            difference = stones.pop() - stones.pop() # difference of 2 largest stones
            if difference:
                stones.append(difference)

        return stones[0] if stones else 0