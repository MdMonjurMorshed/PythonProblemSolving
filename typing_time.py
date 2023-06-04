
# SINGLE ROW KEYBOARD ALGORITHM

def calculate_timing(digits,target):
    
  digit={}
  for x,y in enumerate(digits):
    digit[y]=x
  total_time=0
  prev=0
  for i in target:
    total_time+= abs(digit[i]-prev)
    prev=digit[i]
  return total_time  
a="8675309124"
b="12"
output=calculate_timing(a,b)
print(output)