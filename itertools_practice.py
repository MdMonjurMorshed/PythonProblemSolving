### infinity iterator
   ##  this have three iterator
   ## count, cycle, repeate

from itertools import count, cycle, repeate

infinity_iter = [1,2,3]


### first argument in count is starting and second is step
for item in count(2,3):
    if item > 10:
       break

### cycle takes iterator and run it as cycle to infinity

for item in cycle(infinity_iter):
    
    if item == 10:
       break

### repeate takes value and the repeating time

for item in repeate(1,10):
    print(item)



#### iterator that works in input sequence

    ### accumulate, chain, compress, dropwhile, take while

## accumulate takes iterator and function
## by default accumulate returns sum

print(list(accumulate(infinity_iter)))

## chain takes two iterator and chain it like first then second iter

print(list([1,2,3],['a']))

## compress takes a iterator and a boolean set of iterator containing 0 and 1

print(list(compress([1,2,3],[0,0,1])))

###dropwhile takes function and iterator. 
# it started dropping elements from the iter until function return false

print(list(dropwhile(lamda x:x<4,[2,3,5,1,8])))