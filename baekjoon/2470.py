N = int(input())

nums = list(map(int,input().split()))
# -2 4 -99 -1 98

nums.sort()
# -99 -2 -1 4 98

left = 0
right = N-1

sum_num = abs(nums[left] + nums[right])
two_nums = [nums[left],nums[right]]

while left < right:

    temp = nums[left] + nums[right]

    if abs(temp) < sum_num:
        sum_num = abs(temp)
        two_nums = [nums[left],nums[right]]

    if temp < 0:  
        left += 1
    else:
        right -= 1

print(*two_nums, sep=" ")
