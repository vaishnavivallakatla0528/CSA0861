def vaishu(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(vaishu("fool","poor"))
print(vaishu("foal","poor"))
print(vaishu("too","bar"))
print(vaishu("toto","yaya"))
