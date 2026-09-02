class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(0, n + 1):
            temp = i
            
            while temp > 0:
                mod = temp % 2
                if mod == 1:
                    result[i] += 1
                temp = temp >> 1

        return result

            
            