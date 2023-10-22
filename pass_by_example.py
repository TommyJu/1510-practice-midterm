def pop_list(some_list):
    some_list.pop()

def mod_list(some_list):
    new_list = [4]
    some_list = new_list

list1 = [1, 2, 3]
# pop_list(list1)
# list2 = ["hello"]
# mod_list(list2)
# print(list1, list2)

for i in list1:
    i += 5
print(list1)

list_of_list = [[1,2], [4,3]]
for i in list_of_list:
    i += [0]
print(list_of_list)