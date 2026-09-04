def moyenne_poderee(valeurs, poids):
    mult = []
    for i, j in zip(l, s):
        mult.append(i*j)
    
    return (sum(mult))/sum(poids)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [9, 2, 3, 4, 5, 6, 7, 8, 9]
    
# print(temp)
print(moyenne_poderee(l ,l))


