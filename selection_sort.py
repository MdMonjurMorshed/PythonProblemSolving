def selection_sort(arr):
    
    for i in range (len(arr)):
        starting_index=i
        for j in range(i+1,len(arr)):
            if arr[starting_index]>arr[j]:
                starting_index=j
        arr[i],arr[starting_index]=arr[starting_index],arr[i]
        
    return arr   

arr=[12,2,10,6,15]
print(selection_sort(arr))
