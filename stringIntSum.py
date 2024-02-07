# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         carry=0
#         result=[]

#         i=len(num1)-1
#         j=len(num2)-1

#         # length_def=abs(len(num1)-len(num2))
#         # if len(num1)>len(num2):
#         #     num2="0"*length_def+num2
#         # else:
#         #     num1='0'*length_def+ num1      

#         while i>=0 or j>=0 or carry:

#             a=int(num1[i]) if i >=0 else 0
#             b=int(num2[i]) if j>=0 else 0
#             sum=a+b+carry
#             carry=sum//10
#             result.append(str(sum%10))
#             i -=1
#             j-=1
#         if carry:
#             result.append(str(carry))  
#         return ''.join(result[::-1])      
            
        

# solution=Solution()
# s1=str(input())
# s2=str(input())
# print(solution.addStrings(s1,s2))


class Solution():
    def sumStrings(self,s1,s2):
        carry=0
        result=[]
        i=1
        if len(s1)<len(s2):
            s1,s2=s2,s1
        s2=s2.zfill(len(s1))    
        while i<=len(s1) :
            a=int(s1[-i])      
            b=int(s2[-i])
            sum=a+b+carry
            carry=sum//10
            result.append(str(sum%10))
            i+=1
        if carry:
            result.append(str(carry))    
        return ''.join(result[::-1])    

solution=Solution()
s1=str(input())
s2=str(input())
print(solution.sumStrings(s1,s2)) 