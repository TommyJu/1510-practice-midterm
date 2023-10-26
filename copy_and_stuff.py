"""
Tommy Ju
A01347715
"""
import copy

some_list = [1, 2, 3]
shallow_copy = copy.copy(some_list)
deep_copy = copy.deepcopy(some_list)

print (id(some_list))
print (id(shallow_copy))
print (id(deep_copy))

print ('-' * 5)

print (id(some_list[0]))
print (id(shallow_copy[0]))
print (id(deep_copy[0]))