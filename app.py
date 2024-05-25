def somme (a,b):
    return a+b

def soustraction(a,b):
    return a-b

def modilo (a,b):
    if (a != 0 and b != 0 ):
        return a%b
    print("On ne peut pas faire le modilo de ",a, " et ",b)
    return 0

def division( a,b):
    if (a != 0 and b != 0 ):
        return a/b
    return 0

print(somme(5,8))
print(soustraction(9,51))
print(modilo(8,0))
print(division(5,6))
print("ok")
