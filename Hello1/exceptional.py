def convert(s):
    '''convert to an interger'''
    try:
        x=int(s)
        print("conversion suceeded!  X=", x)
    except ValueError:
        x=-1
        print("conversion failed !  ")
    except TypeError:
        x=-1
        print("conversion failed !  ")
    return x

convert("20")

convert([4,5,6])