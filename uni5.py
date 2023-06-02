ofile = open('data1.txt' , 'r')
name = input("Enter Your Name : ")
result = 0
j = 0
for i in ofile :
    res = i.rstrip().split(',')
    break
for i in ofile :
    y = i.rstrip().split(',')
    print("the question is " , y[0])
    print(y[1:4])
    ans = input("choose the right choice ")
    if ans == res[j] :
        result = result + 5
    j = j + 1
print("hi ",name ," you got ", result," from 100 ")
ofile.close()
orfile = open('res.txt' , 'w')
d = {"Student's Name ", name ," and its Result is " ,str(result)}
orfile.writelines(d)
orfile.close()
