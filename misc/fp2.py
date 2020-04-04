'''problem with list - zip '''
def haf():
    ''' first inner function'''
    my_zip = zip(range(3), range(3))
    print(list(my_zip))
    my_list = list(my_zip)
    print(my_list)

def baf():
    '''fist assign into variable'''
    my_zip = zip(range(3), range(3))
    my_list = list(my_zip)
    print(my_list)
    print(list(my_zip))

def naf():
    ''' works as expected'''
    print(list(zip(range(3), range(3))))


haf()
baf()
naf()
