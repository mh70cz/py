""" get the original variable name of a variable passed to a function """

# https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function
# %%
import traceback


# %%
def get_arg_var_name(var):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    # return filename, lineno, function_name, code

    # extract single argument variable name
    arg_var_name = code.rpartition("func(")[2].strip(")")
    return arg_var_name


foo = "myfoo" 

arg_var_name = get_arg_var_name(foo)
print (arg_var_name)

# %%


