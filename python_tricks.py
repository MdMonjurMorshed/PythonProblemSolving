
# slicing string  to reverse 

string_ = "hello"

print(string_[::-1])

### aliasing

a = [1, 2, 3, 4 ,5]
b = a
b[2] = 20
print('check alias:',a)
print('check alias:',b)

### The most straightforward way to create a clone is to leverage slicing
a = [1, 2, 3, 4 ,5]
b = a[:]
b[4] = 0

print(a)
print(b)

### dictionary merging

a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}

a_and_b = a | b
print('merged dict a and b:',a_and_b)


## removes duplicates from the list 

a = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 2, 2]
print('removed the duplicates:',list(set(a)))


### use of setdefault

string_value = ["tahi","tahi"]

count ={}

for word in string_value: # if string the string_value.split()
    count.setdefault(word,0)
    count[word]+=1

print("used setdefault here:",count)
