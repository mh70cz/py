""" Using get() to return a default value from a Python dict
    keywords: disctionary, default_value, lefpad, padleft, string_format
    based on: https://dbader.org/blog/python-dict-get-default-value
"""

name_for_userid = {
    382: "Alice",
    950: "Bob",
    590: "Dilbert"
}

ids_to_greet = [382, 999]

def non_pythonic_get(userid):
    """ verbose, dictionary is accessed twice"""
    if userid in name_for_userid:
        return "Hi %s!" % name_for_userid[userid]
    else:
        return "Hi there!"

def pythonic_get(userid):
    """ standard """
    return "Hi %s!" % name_for_userid.get(userid, "there")

for uid in ids_to_greet:
    print((str(uid) + " non pythonic, old string format: ").ljust(40)
          + str(non_pythonic_get(uid)))
    print("{:<40}".format(str(uid) + " non pythonic, new string format: ")
          +  str(non_pythonic_get(uid)))
    print((str(uid) + " pythonic, old string format: ").ljust(40)
          + str(pythonic_get(uid)))
    print("{:<40}".format(str(uid) + " pythonic, new string format: ")
          +  str(pythonic_get(uid)))
