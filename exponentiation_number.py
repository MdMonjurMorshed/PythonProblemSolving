## finding out the exponentiation of a number

def power_of_number(base,exp):
    if exp == 1:
        return base
    else:
        return base*power_of_number(base,exp-1)
    
base=int(input("please enter base:"))
exp=int(input('please enter exponentiation: '))
print(power_of_number(base,exp))    