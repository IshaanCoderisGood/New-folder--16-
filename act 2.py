def zerotoend(a,a_size):
    zero = 0
    nonzero = 0
    while (nonzero!=a_size):
        if (a[nonzero]!=0):
            a[nonzero], a[zero] = a[zero], a[nonzero]
            zero += 1
        nonzero += 1
a = [1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1]
a_size = len(a)
zerotoend(a,a_size)
print(a)