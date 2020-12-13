def div(arg1, arg2):
    try:
        return arg1/arg2
    except ZeroDivisionError as err:
        print("Error: ", err)


print(div(1, 4))
