# different iteration tricks
# to unpack list item into other list

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
final_list = [*list_1,*list_2,*list_3]
print(final_list)

# unpack list item through variable

var_1,var_2,var_3,*var_other =final_list
print(var_1)
print(var_2)
print(var_3)
print(var_other)