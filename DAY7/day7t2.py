def log_call(func):
    def wrapper(*args,**kwargs):
        print(f"Function name:{func.__name__}")
        print(f"Arguments:{args}")

        result=func(*args,**kwargs)
        return result
    return wrapper

@log_call
def add(a,b):
    print("sum=",a+b)

@log_call
def greet(name):
    print("Hello,",name)

@log_call
def multiply(x,y):
    print("product=",x*y)

print(add(10,20))
print(greet("Arun"))
print(multiply(3,5))