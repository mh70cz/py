'''dice'''
def haf():
    '''main'''

    dct = assing_to_dict(roll_dice())
    for i in dct:
        print(i, dct[i])

def assing_to_dict(all_posible_rolls):
    '''assign first 10 added result (i.e. dice 1 + dice 2) into dictionary '''
    dct = dict()
    for i in range(2, 13):
        dct[i] = fnd_eqls(i, all_posible_rolls)
    return dct

def fnd_eqls(searched_added_result, all_posible_rolls):
    ''' find equal added results (i.e. dice 1 + dice 2) in all_posible_rolls'''
    equals = []
    for item in all_posible_rolls:
        if item[0] + item[1] == searched_added_result:
            equals.append(item)
    return equals

def roll_dice():
    ''' create a list of all possible rolls'''
    all_posible_rolls = []
    for i in range(1, 7):
        for j in range(1, 7):
            all_posible_rolls.append((i, j))
    return all_posible_rolls

haf()

