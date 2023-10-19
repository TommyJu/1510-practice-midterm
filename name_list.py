"""
(10) Implement a function called name_list that uses a while loop to ask the user to enter a sequence of names.
Make sure the user knows they must type quit when they are finished. When the user does not want to enter any
more names, return the names they have entered in a dictionary. The dictionary’s keys must be integers representing
the number of letters in a name, and the values must be lists that contain names of that length.
For example, if your user enters the names “Amy”, “Ann”, “Anton”, and “Adam”, the function will return a dictionary
of the form { 3: [“Amy”, “Ann”], 4: [“Adam”], 5: [“Anton”] }
"""

def name_list():
    names = []
    while True:
        user_input = input("Enter a name or 'quit': ")
        if user_input == "quit":
            break
        else:
            names.append(user_input)

    result = {}
    for name in names:
        if len(name) in result.keys():
            result[len(name)].append(name)
        else:
            result[len(name)] = [name]

    return result

def main():
    print(name_list())

if __name__ == "__main__":
    main()
