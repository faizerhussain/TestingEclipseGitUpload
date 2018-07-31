import sys
from math import log

def convert(s):
    '''convert to an interger'''
    try:
        return int(s)       
    except (ValueError, TypeError) as e:
        print("conversion error : {}".format(str(e)),file=sys.stderr)
        raise

def string_log(s):
    print("test")
    v=convert(s)
    return log(v)


convert("20")
# 
convert([4,5,6])


#string_log("test")


# print("#############################")
# string_log("25h")
