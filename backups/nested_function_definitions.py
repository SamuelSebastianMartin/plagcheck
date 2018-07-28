def outer():
    def inner():
        x = 4
        return x
    myvar = inner()
    return myvar
a = outer()
print(a)
