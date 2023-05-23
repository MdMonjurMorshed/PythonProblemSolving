class FindSunsets:
    def subset(self,list_num):
        return self.recursion([],list_num)

    def recursion(self,current,list_set):
        if   list_set:
            return self.recursion(current,list_set[1:])+self.recursion(current+[list_set[0]],list_set[1:])

        return [current]   

find_subset=FindSunsets()  


print(find_subset.subset([3,5,6]))

print("hello")