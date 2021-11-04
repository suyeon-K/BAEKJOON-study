class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        temp = [a,b,c]
        count = 0
        while temp.count(0)<2 :
            temp = sorted(temp)
            temp[-1] = temp[-1] -1
            temp[-2] = temp[-2] -1
            count += 1
        return count

    def maximumScore2(self, a: int, b: int, c: int) -> int:
        num_list = sorted([a,b,c])

        if num_list[0]+num_list[1] <= num_list[2] :
            return num_list[0]+num_list[1]
        else:
            return sum(num_list)//2


S = Solution()
print(S.maximumScore(2,4,6))