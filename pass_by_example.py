def pop_list(some_list):
    some_list.pop()

def mod_list(some_list):
    new_list = [4]
    some_list = new_list

list1 = [1, 2, 3]
pop_list(list1)
list2 = ["hello"]
mod_list(list2)
print(list1, list2)