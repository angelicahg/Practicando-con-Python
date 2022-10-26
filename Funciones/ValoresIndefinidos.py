def argumento (num):
    return type(num)

print(argumento(10))

def argumento (*num):
    return type(num)
    
print(argumento(10))