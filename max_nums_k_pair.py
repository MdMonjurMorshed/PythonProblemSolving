# Max Number of K-Sum Pairs

def maxOperations(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_count = {}
        process = 0

        for i in nums:
            diff = k-i
            if sum_count.get(diff,0)>0:
                sum_count[diff]-=1
                process+=1
            else:
                sum_count[i] = sum_count.get(i,0)+1  

        return process          
                  

print(maxOperations(nums=[3,1,3,4,3],k=6))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                