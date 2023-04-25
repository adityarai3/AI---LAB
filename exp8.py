def unification(a,b):
    if len(a) != len(b):
        return "Unification Failed"
    elif(a[0] != b[0]):
        return "Unification Failed"
    else:
        result = a[:2]
    
    for l in range(2,len(a)-1):
        result += a[l]
        if(a[l]==";"):
            continue
        result += "/"
        result += b[l]
        result += ")"

        print("Unification Success")
        return result
print("Enter Expression 1")
a = input()
print("Enter Expression 2")
b = input()
print(unification(a, b))