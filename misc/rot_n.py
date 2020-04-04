'''rot n'''
def haf():
    '''Challenge 1'''
    orig = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc
    dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq 
    qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. maps'''

    n = 24
    assert (orig == rotN(rotN(orig, n), -n)), "error in code and decode"

    print(''.join(rotN(orig, 2)))

def rotN(in_str, n):
    '''rot n '''
    out_str = []
    assert (abs(n) <= ord('z') - ord('a')), "abs value of shift {0} to long".format(n)
    for c in in_str:
        if c >= 'a' and c <= 'z':
            c_shifted = ord(c) + n
            if c_shifted > ord('z'):
                c_shifted -= ord('z') - ord('a') + 1
            elif c_shifted < ord('a'):
                c_shifted += ord('z') - ord('a') + 1
            out_str.append(chr(c_shifted))
        else:
            out_str.append(c)
    return ''.join(out_str)

haf()

