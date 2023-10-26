"""
Tommy Ju
A01347715
"""
import copy

some_list = [[1, 2, 3], 4, 5]
alias = some_list
shallow_copy = copy.copy(some_list)
deep_copy = copy.deepcopy(some_list)

print ("list:", id(some_list))
print ("alias:", id(alias))
print ("shallow copy:", id(shallow_copy))
print ("deep copy:", id(deep_copy))

print ('-' * 10)

print ("list:", id(some_list[0]))
print ("alias:", id(alias[0]))
print ("shallow copy:", id(shallow_copy[0]))
print ("deep copy:", id(deep_copy[0]))