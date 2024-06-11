def __main__():
    a = input()
    print(convert(a))

def convert(a):
    a = a.replace(":)", "\N{Slightly Smiling Face}")
    a = a.replace(":(", "\N{Slightly Frowning Face}")
    return a
__main__()
