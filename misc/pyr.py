'''build a pyramid via recursive funcion'''
def pyr_rec(height, right_shift=0):
    '''recursive pyramid'''
    if height == 1:
        return right_shift * " " + "*"
    else:
        line = right_shift * " " + ((height -1) * 2 + 1) * "*"
        return pyr_rec(height - 1, right_shift + 1) + "\n" + line

print(pyr_rec(6, 2))

