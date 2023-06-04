class FindTriplets:
    def find_triplets(self,list_num):
        nums,results,i=sorted(list_num),[],0
        print(nums)
        while i<len(nums)-2:
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                else:
                    results.append([nums[i],nums[j],nums[k]])
                    j,k=j+1,k-1

                    while j<k and nums[j]== nums[j-1]:
                        j+=1
                    while j<k and nums[k]== nums[k-1]:
                        k-=1
            i+=1
            while i<len(nums)-2 and nums[i]== nums[i-1]:
                i+=1

        return results



triplet=FindTriplets()
real_number=list(map(int,input('enter space separated ingegers:').split()))
output=triplet.find_triplets(real_number)
print(output)
                         


