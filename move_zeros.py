### 283. Move Zeroes leetcode

def move_zeros(nums):
    list_first = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[list_first],nums[i] = nums[i],nums[list_first]
            list_first +=1
    return nums

print(move_zeros([0,1,0,3,12]))        