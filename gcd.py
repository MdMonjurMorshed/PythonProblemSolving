def find_gcd(num1,num2):
    # if num1>num2:
    #     small=num2
    # else:
    #     small=num1

    # for i in range (1,small+1):
    #     if ((num1 % i)==0 and (num2%i)==0):
    #         gcd =i 

    # return gcd
    while num2:
        rem=num1%num2
        num1=num2
        num2=rem
    return num1    

num1=54
num2=24
print(find_gcd(num1,num2))           

