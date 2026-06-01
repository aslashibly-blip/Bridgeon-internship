def self_divide(a,b):
    if b ==0:
        raise ZeroDivisionError("cannot divide by zero")
    return a/b
try:
    print(self_divide(10,2))
    print(self_divide(10,0))
except ZeroDivisionError as e:
    print(e)