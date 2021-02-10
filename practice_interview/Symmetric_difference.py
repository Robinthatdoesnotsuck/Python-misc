set_1 = [1, 2, 5]
set_2 = [2, 3, 5]
set_3 =[3, 4, 5]
set_set = [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]


def sym_difference(set_of_sets):
    if len(set_of_sets) == 1:
        print(set_of_sets)
        
    else:
        my_len = len(set_of_sets)
        first_set = set_of_sets[0]
        second_set = set_of_sets[1]
        set_difference = []
        
        for element in first_set:
            flag = 0
            for element_2 in second_set:
                if element == element_2:
                    flag += 1
                    print("found it")
                else:
                    print("not yet")
            if flag == 0:
                if not element in set_difference:
                    set_difference.append(element)
        for element_2 in second_set:
            flag = 0
            for element in first_set:
                if element_2 == element:
                    flag += 1
                    print("found it")
                else:
                    print("not yet")
            if flag == 0:
                if not element_2 in set_difference:
                    set_difference.append(element_2)
        set_of_sets[0] = set_difference
        set_of_sets.remove(second_set)

        set_of_sets = sym_difference(set_of_sets)
    return set_of_sets
whatever = []
whatever = sym_difference(set_set)
print(whatever[0])