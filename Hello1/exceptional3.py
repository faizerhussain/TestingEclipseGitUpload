import sys
def convert(s):
    '''convert to an interger'''
    try:
        return int(s)       
    except (ValueError, TypeError) as e:
        print("conversion error : {}".format(str(e)),file=sys.stderr)
        return -1

convert("20")

convert([4,5,6])