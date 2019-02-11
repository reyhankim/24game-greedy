def Close(sco):
    return (abs(24-sco))

def Olah(sco, ope, num):
    if (ope == 5):
        return sco+num
    elif (ope == 4):
        return sco-num
    elif (ope == 3):
        return sco*num
    else:
        return sco/num

def Score(sco, ope, num):
    if (ope == 5):
        return sco + ope - Close(sco+num) 
    elif (ope == 4):
        return sco + ope - Close(sco-num) 
    elif (ope == 3):
        return sco + ope - Close(sco*num) 
    else:
        return sco + ope - Close(sco/num) 

""" Program utama """
arr = []
arr.append(int(input("Bilangan pertama   : ")))
arr.append(int(input("Bilangan kedua     : ")))
arr.append(int(input("Bilangan ketiga    : ")))
arr.append(int(input("Bilangan keempat   : ")))

num = arr[0]
opp = []
ind = 0
tmp = 0

for i in range(1,4):
    if (arr[i] > num):
        num = arr[i]
        ind = i

del arr[ind]

ind = 0
cho = -999
neff = 3

while (arr != []):
    cho = -999
    for i in range(0,4):
        ope = 5-i
        print(ope)
        for j  in range(0,neff):
            sc = Score(num,ope,arr[j])
            if (cho  < sc):
                print("caught")
                cho = sc
                ind = j
                tmp = ope
                print(j)
                print(arr)
    te = arr[ind]
    print(ind)
    print(arr)
    num = Olah(num,tmp,te)
    opp.append(tmp)
    del arr[ind]
    print(cho)
    print(arr)
    print(opp)
    print(num)
    print()
    neff -= 1