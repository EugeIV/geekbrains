def div(arg1, arg2):
    try:
        return arg1/arg2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

