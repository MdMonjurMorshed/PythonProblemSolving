def linear_search(alist,item):
    pos=0
    for i in range(len(alist)):
         
        if alist[i] == item:
            pos=i

    print(pos)
alist=[1,2,3,4,5,6]
item= 3
linear_search(alist,item)   
            