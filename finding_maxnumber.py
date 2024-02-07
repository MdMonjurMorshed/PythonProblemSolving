## finding max number from a list of numbers

def find_max_number():
    n= int(input('enter the limit'))
    l=[]
    for i in range(0,n):
        a= int(input('enter numbers in the list:'))
        l.append(a)
    max_number=l[0]
    for j in range(1,len(l)):
        if l[j]>max_number:
            max_number=l[j]
    print(max_number)        
find_max_number()
