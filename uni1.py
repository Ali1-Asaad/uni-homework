l = []
for i in range(1,1001) :
    flag = 0
    for j in range(2,i) :
        if i%j==0 :
            flag = 1
    if flag == 0 :
        l.append(i)
print(l)
