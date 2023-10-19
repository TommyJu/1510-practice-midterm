"""
(5) Define a function called cleaner that accepts two parameters in this order: a list called measurements
and a float called maximum. Assume the list contains floats and has non-zero length. The function should return
a new list that consists of all the numbers in the list called measurements that are less than maximum.
(As you consider how to answer this, think about how to break this down into steps, the order of the steps,
and the control structure(s) we want to use. Be ‘comprehensive’ in your analysis.)
"""

# measurements is a non-zero list of floats
# maximum is a float
def cleaner(measurements, maximum):
    new_list = [number for number in measurements if number < maximum]
    print (new_list)

cleaner([1.5, 2.0, 10.7, 9.2], 10.6)
cleaner([3.3333333, 3.1000001, -5, 0, 1.2], 3.1)