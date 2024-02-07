def margeSort(n):
    if len(n)<=1:
        return n
    mid=len(n)//2
    left_half=n[:mid]
    right_half=n[mid:]
    print("left half: ",left_half)
    print("right half: ",right_half)

    left_half=margeSort(left_half)
    right_half=margeSort(right_half)

    return marge(left_half,right_half)


def marge(left,right):
    result=[]
    left_ind,right_ind=0,0
    while left_ind<len(left) and right_ind<len(right):
        if left[left_ind] <right[right_ind]:
            result.append(left[left_ind])
            left_ind+=1
        else:
            result.append(right[right_ind])
            right_ind+=1
    result.extend(left[left_ind:])            
    result.extend(right[right_ind:])
    return result            
        


print(margeSort([3,5,8,2,1,9]))


    