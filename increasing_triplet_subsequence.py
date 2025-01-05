#### 334. Increasing Triplet Subsequence

def increasing_triplet_subsequence(nums):
    if len(nums)<3:
        return False
    i = (2**31)-1
    j = (2**31)-1

    # i = j = float('inf')
    # for num in nums:
    #     if num <= i:
    #         i = num
    #     elif num <= j:
    #         j = num
    #     else:
    #         return True
                
        

    for ind in range (len(nums)):
        if nums[ind] <= i:
            i = nums[ind]
        elif nums[ind] <= j:
            j = nums[ind]
        else:
            return True

    return False            

print(increasing_triplet_subsequence([1,1,2,1]))