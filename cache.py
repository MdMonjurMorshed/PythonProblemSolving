fibe_cache={}

def Fibo(n):
    sequence=[0,1]
    for i in range(2,n+3):
        new_fibo=sequence[i-1]+sequence[i-2]
        sequence.append(new_fibo)
    print(sequence)    

    if n in fibe_cache:
        return fibe_cache[n]
    if n==0:
        result= 0
    elif n==1:
        result=1
    else:
        result= Fibo(n-1)+Fibo(n-2)
        
    
    fibe_cache[n]=result
    return result
print(Fibo(10))
print(fibe_cache)

    