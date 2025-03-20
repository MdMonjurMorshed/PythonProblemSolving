### infinity iterator
   ##  this have three iterator
   ## count, cycle, repeate

from itertools import count, cycle, repeat,combinations,combinations_with_replacement,accumulate,compress,dropwhile,product,permutations

infinity_iter = [1,2,3]


### first argument in count is starting and second is step
for item in count(2,3):
    if item > 10:
       break

### cycle takes iterator and run it as cycle to infinity

# for item in cycle(infinity_iter):
    
#     if item == 10:
#        break

### repeate takes value and the repeating time

for item in repeat(1,10):
    print('+++repeat+++',item)



#### iterator that works in input sequence

    ### accumulate, chain, compress, dropwhile, take while

## accumulate takes iterator and function
## by default accumulate returns sum

print('====accumelate====',list(accumulate(infinity_iter)))

## chain takes two iterator and chain it like first then second iter

# print(list([1,2,3],['a']))

## compress takes a iterator and a boolean set of iterator containing 0 and 1

print('===compress===:',list(compress([1,2,3],[0,0,1])))

###dropwhile takes function and iterator. 
# it started dropping elements from the iter until function return false

print("dropwhile:",list(dropwhile(lambda x:x<4,[2,3,5,1,8])))


### combination function

### product. like Cartesian product

for item in product(['a','b'],[1,2]):
    print('product:',item)

## permutation 
   ## returns all possible combination of iteration

for item in permutations('abc',2):
    print("permutation",item)


## combination
  # returns all combination based on the combination size

for item in combinations('abc',2):
    print('Combination:',item)

## combination_with_relacement
   ## it is like combination but it's also returns repeatative combination

for item in combinations_with_replacement('abc',2):
    print(item)

for item in combinations([1,2,3],2):
    print(item)
