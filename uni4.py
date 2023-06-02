while True :
    num = input("Enter Number : ")
    flag = 0
    for i in num :
        if (i != "1" and i != "0") :
            flag = 1
    if flag == 1 :
        print("Invalid Input ")
    if flag == 0 :
        break
j = 1
dec_num = 0
for i in num :
    d = int(i) * 2**(len(num)-j)
    dec_num = dec_num + d
    j += 1
print("The Equivalent Decimal Number",dec_num)
