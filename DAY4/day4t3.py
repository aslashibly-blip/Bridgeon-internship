class WeakpasswordError(Exception):
    pass
def check(password):
    if len(password)<8:
        print("password must contain 8 characters")
    elif not any(char.isdigit() for char in password):
        print("password must contain digits")
    elif not any(char.isupper() for char in password):
        print("password must contain uppercase")
    else:
        print("right password")
try:
    password=input("enter password:")
    check(password)
except WeakpasswordError as e:
    print("error:",e)
