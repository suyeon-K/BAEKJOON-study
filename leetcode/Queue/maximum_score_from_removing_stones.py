class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        temp = [a,b,c]
        count = 0
        while temp.count(0)<1 :
            temp = sorted(temp)
            print(temp)
            temp[-1] = temp[-1] -1
            temp[-2] = temp[-2] -1
            count += 1
        return count

S = Solution()
print(S.maximumScore(2,4,6))