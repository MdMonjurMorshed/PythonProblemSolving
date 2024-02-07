num = int(input("enter an integer number: "))
#write your code here
temp=num
result=0
n=len(str(num))
print(n)
if (temp<10 and temp>0):
   result=0
else:
      
   
    while(temp>0):  
      mod=temp%10
      result=result+mod**n
      temp=int(temp/10)
print(result)      
if (num == result):
  print("Armstrong number")
else:
  print("Not Armstrong number")