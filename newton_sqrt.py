## finding out square root of a number using newton's method
def newton_sqrt(number):
    approx=0.5*number
    better=0.5*(approx+number/approx)
    while better != approx:
        approx=better
        better=0.5*(approx+number/approx)
    return approx

number=float(input('enter a number yo get sqrt: '))
print(newton_sqrt(number))
