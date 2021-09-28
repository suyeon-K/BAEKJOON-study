class Solution:
    def trap(self, height) -> int:
        water = 0
        height = [str(x) for x in height]
        height_str = "".join(height).strip('0')

        if height_str == "":
            return 0

        height = [int(x) for x in height_str]
        min_num = min(height)
        height = [str(x-min_num) for x in height]
        height_str = "".join(height)
 
        while(height_str.count('0') != 0):
            water += height_str.count('0')
            print(water)
            temp = [int(x) for x in height_str]
            for i in range(len(height_str)):
                if temp[i] != 0:
                    temp[i] = str(temp[i]-1)
                else:
                    temp[i] =str(temp[i])
            height_str = "".join(temp).strip('0')


        return water

x = Solution()
print(x.trap([4,2,3]))