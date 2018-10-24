import copy
import itertools
import pprint

# number of cases containing both first and second over the total number of cases
def calculate_support(first, second):
    count = 0
    for single_set in sets:
        if first in single_set and second in single_set:
            count += 1
    return count/len(sets)

# number of cases containing first and second over first
def calculate_confidence(first, second):
    first_count = 0
    second_count = 0
    for single_set in sets:
        if first in single_set:
            first_count += 1
            if second in single_set:
                second_count += 1
    return second_count/first_count

# DATA
sets = []
frequency = 1

sets.append(set([5, 6, 8, 9]))
sets.append(set([5, 6, 7, 9]))
sets.append(set([7, 8, 9]))
sets.append(set([4, 6, 9]))
sets.append(set([5, 7, 8, 9]))

# create a set of unique values
unique_values = frozenset([item for sublist in sets for item in sublist])
# create a dict that will hold final sets
counter = dict()
# define the number of elements in a set
element_no = 0

# continue until ther are possible sets
while len(unique_values) > 0:
    counter[element_no] = dict((key, 0) for key in unique_values)

    # for every set from original data
    for iter in range(len(sets)):
        # create all possible combinations
        set_to_iterate = sets[iter] if element_no == 0 else [frozenset(x) for x in frozenset(itertools.combinations(sets[iter], element_no + 1))]
        # for every entry in the original iterated set
        for entry in set_to_iterate:
            counter[element_no][entry] = counter[element_no].get(entry, 0) + 1
    counter_copy = copy.deepcopy(counter)

    for k, v in counter_copy[element_no].items():
        if counter[element_no][k] <= frequency:
            del counter[element_no][k]
    element_no += 1
    unique_values = frozenset(itertools.combinations(frozenset(counter[element_no - 1].keys()), element_no + 1))

pp = pprint.PrettyPrinter()
print("all sets that pass the frequency rule")
pp.pprint(counter)

for entry in [x for x in counter[1].keys()]:
    # print support
    first, second = entry
    print("support for {} {} is {}".format(first, second, calculate_support(first, second)))

print("confidence for {} {} is {}".format(5, 9, calculate_confidence(5, 9)))
print("confidence for {} {} is {}".format(9, 5, calculate_confidence(9, 5)))