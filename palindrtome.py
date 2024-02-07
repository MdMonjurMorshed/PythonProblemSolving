class FindPalindrom():
    def getpalindrom(self,x):
        
        compareTo=x
        result=0
        while(x>0):
          print('i am in while')
          mod=x%10
          result=result*10+mod

          x=int(x/10)
          
         
          
        if (result==compareTo):
           return True
        else:
           return False
            
num=input("enter number")
int_num=int(num)    
findPalindrom=FindPalindrom()
print(findPalindrom.getpalindrom(int_num))






