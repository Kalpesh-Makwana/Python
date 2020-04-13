SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def sublist(list_one, list_two):
    
    A = ','.join([str(element) for element in list_one])
    B = ','.join([str(element) for element in list_two])

    if A == B:
        return EQUAL
    if A in B:
        return SUBLIST
    if B in A:
        return SUPERLIST
    return UNEQUAL