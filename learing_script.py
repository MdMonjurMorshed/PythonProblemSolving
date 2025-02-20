class FirstClass(object):
    x = 1
class SecondClass(FirstClass):
    pass
class ThirdClass(FirstClass):
    pass

print(FirstClass.x,SecondClass.x,ThirdClass.x)
SecondClass.x = 2
print(FirstClass.x,SecondClass.x,ThirdClass.x)
FirstClass.x = 3
print(FirstClass.x,SecondClass.x,ThirdClass.x)

# map() function

'''map takes function and single or multiple iterable.
iterable could be list or tuple. 
function in the map uses every elements from the iterable. 
map returns an another iterable. '''

output_map = map(lamda x:x**2,[1,2,3])
print(output_map)
