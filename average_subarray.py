def average_subarray(nums,k):
    sum_of_window = sum(nums[:k])
    max_sum = sum_of_window

    for i in range(k,len(nums)):
        sum_of_window += nums[i]
        sum_of_window -= nums[i-k]
        max_sum = max(max_sum,sum_of_window)
    return max_sum / float(k)    

print(average_subarray([1,12,-5,-6,50,3],4))