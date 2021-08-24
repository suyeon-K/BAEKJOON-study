class Solution3(object):
    def search(self, nums, target):
        def binary_search(left, right):
            mid = (left+right)//2
            
            if left <= right:
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            return -1

        return binary_search(0, len(nums)-1)  # search() 함수의 return문

def binary_search(nums, target, left, right):
    if (left > right):
        return -1
    
    mid = (left+right)//2

    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return binary_search(nums, target, mid+1, right)
    else:
        return binary_search(nums, target, left, mid-1)

    