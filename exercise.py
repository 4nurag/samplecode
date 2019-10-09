L = []
L1 = []
L2 = []
for i in range(6,10):
    L.append(i)
for i in range(10,4,-2):
    L1.append(i)
for i in range(len(L1)):
    L2.append(L[i]+L1[i])
L2.append(len(L)-len(L1))
print(L2)
