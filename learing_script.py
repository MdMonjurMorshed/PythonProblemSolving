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