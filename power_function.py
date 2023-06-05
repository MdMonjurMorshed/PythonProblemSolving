# MAKING POWER FUNCTION WHICH WILL CALCULATE THE POWER OF SOMETHING

class PowerFunction:
    def pow(self,x,n):
  
        results=1
        
        for i in range (n):
         

            results *=x

        if n<0:
            
            return 1/self.pow(x,-n)    
        
        return results    



p=PowerFunction()
output=p.pow(-5,2)
print(output)