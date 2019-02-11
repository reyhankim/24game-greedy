def accept(l1, l2):
    if (l1[1] != l2[1]) & (l1[1] != l2[2]) & (l1[2] != l2[1]) & (l1[2] != l2[2]):
        if  (l1[0] + l2[0] == 24):
            return 5
        elif (l1[0] - l2[0] == 24):
            return 4
        elif (l1[0] * l2[0] == 24):
            return 3
        elif(l2[0] != 0):
            if (l1[0] / l2[0] == 24):
                return 2
        else:
            return 0

def Olah(sco, ope, num):
    if (ope == 5):
        return sco+num
    elif (ope == 4):
        return sco-num
    elif (ope == 3):
        return sco*num
    else:
        return sco/num

def op(oper):
    if (oper == 5):
        return "+"
    elif (oper == 4):
        return "-"
    elif (oper == 3):
        return "*"
    else:
        return "/"

arr = []
arr.append(int(input("Bilangan pertama   : ")))
arr.append(int(input("Bilangan kedua     : ")))
arr.append(int(input("Bilangan ketiga    : ")))
arr.append(int(input("Bilangan keempat   : ")))

arr.sort(reverse = True)

ph2 = []

for i in range(0,3):
    for j in range(i+1, 4):
        for oper in range(2,6):
            tmp = Olah(arr[i],oper,arr[j])
            ph2.append([tmp,i,j,oper])


for l1 in ph2:
    for l2 in ph2:
        if(accept(l1,l2)):
            print("(",arr[l1[1]], op(l1[3]), arr[l1[2]] , ")",op(accept(l1,l2)),"(",arr[l2[1]], op(l2[3]), arr[l2[2]] , ")")
            print()