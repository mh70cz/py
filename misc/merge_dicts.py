''' merge 2 dictionaries where their keys are result of:
difference, intersection, union, symetric_difference'''
def haf():
    ''' define dictionaries and merge keys then call merges '''
    di1 = {'a': 1, 'b': 3, 'd': 4, 'e': 7}
    di2 = {'a': 4, 'b': 8, 'c': 10, 'e': 9}

    s_a = set(k for k in di1)
    s_b = set(k for k in di2)

    s_difference = (s_a - s_b)
    s_intersection = (s_a & s_b)
    s_union = (s_a | s_b)
    s_symetric_difference = (s_a ^ s_b)

    print('difference:')
    merge(s_difference, di1, di2)
    print('intersection:')
    merge(s_intersection, di1, di2)
    print('union:')
    merge(s_union, di1, di2)
    print('symetric_difference:')
    merge(s_symetric_difference, di1, di2)

def merge(merge_keys, di1, di2):
    '''merge 2 dictionaries by common_keys'''
    out_dic = {}
    for k in merge_keys:
        if k in di1:
            val1 = di1[k]
        else:
            val1 = None

        if k in di2:
            val2 = di2[k]
        else:
            val2 = None

        out_dic[k] = [val1, val2]
    print(out_dic)

haf()
