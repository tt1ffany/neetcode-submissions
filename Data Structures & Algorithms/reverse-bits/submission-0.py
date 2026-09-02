class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1 # 1 if n=1, 0 if n=0
            result = result | (bit << (31 - i))
        return result