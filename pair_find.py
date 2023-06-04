class PairFind:
    def find_pair(self,nums,target):
        new_dict={}
        a=[]
        for i,num in enumerate(nums):
          
            if target-num in new_dict:
                
                a.append((new_dict[target-num],i))
               
                
                
            elif  target-num not in new_dict:
                  new_dict[num]=i

        return a        
            
            
           
        print(new_dict)

find=PairFind()
print(find.find_pair((1,2,3,4,5,6,7),7))        