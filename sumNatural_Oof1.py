# to reduce time complexity O(n) to O(1)
n=int(input("Enter an integer number: "))
sum=int(n*(n+1)/2)
print(sum)

# Split the number into digit
sum=0
ans=0
while (n>0):
    digit=n%10
    sum+=digit # sum of those digits
    ans=ans*10+digit # getting reverse of the input number
    print(digit)
    n=int(n/10)  



print(ans)    