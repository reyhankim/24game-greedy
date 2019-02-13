import os

def Close(sco, tar):
    return (abs(tar-sco))

def Olah(sco, ope, num):
    if (ope == 5):
        return sco+num
    elif (ope == 4):
        return sco-num
    elif (ope == 3):
        return sco*num
    else:
        return sco/num

def targ(n):
    if (n == 1):
        return 24
    elif(n == 2):
        return 20
    else:
        return 10

def nilai(oper):
    if (oper == "+"):
        return 5
    elif (oper == "-"):
        return 4
    elif (oper == "*"):
        return 3
    else:
        return 2

def op(oper):
    if (oper == 5):
        return "+"
    elif (oper == 4):
        return "-"
    elif (oper == 3):
        return "*"
    else:
        return "/"

def Score2(sco, ope, num, n):
    if (ope == 5):
        return sco + ope - Close(sco+num,targ(n)) - (sco+num) % 4
    elif (ope == 4):
        return sco + ope - Close(sco-num,targ(n)) - (sco-num) % 4
    elif (ope == 3):
        return sco + ope - Close(sco*num,targ(n)) - (sco*num) % 4
    else:
        return sco + ope - Close(sco/num,targ(n)) - (sco/num) % 4


def result(res,num):
    n = nilai(res[1]) + nilai(res[3]) + nilai(res[5]) - Close(num,24)
    if ((res[3] == "*") | (res[3] == "/")) & ((res[1] == "+") | (res[1] == "-")):
        file_out.write("("+str(res[0])+res[1]+str(res[2])+")"+res[3]+ str(res[4])+ res[5]+ str(res[6])+"\n")
        #file_out.write(str(n-2))
    else:
        file_out.write(str(res[0])+res[1]+str(res[2])+ res[3]+ str(res[4])+ res[5]+ str(res[6])+"\n")
        #file_out.write(str(n))

""" Program utama """
flag = True
file_in = open("debug_2.txt")
file_out = open("outfile_2.txt","w")
while (True):
    arr = []
    arr = file_in.readline().split(" ")
    if (arr[0] == "") : break
    arr[0] = int(arr[0])
    arr[1] = int(arr[1])
    arr[2] = int(arr[2])
    arr[3] = int(arr[3])

    num = arr[0]
    res = []
    opp = []
    ind = 0
    tmp = 0

    for i in range(1,4):
        if (arr[i] > num):
            num = arr[i]
            ind = i
    res.append(arr[ind])
    del arr[ind]

    ind = 0
    cho = -999
    neff = 3

    while (arr != []):
        cho = -999
        for i in range(0,4):
            ope = 5-i
            for j  in range(0,neff):
                sc = Score2(num,ope,arr[j],neff)
                if (cho  < sc):
                    cho = sc
                    ind = j
                    tmp = ope
        te = arr[ind]
        num = Olah(num,tmp,te)
        opp.append(tmp)
        res.append(op(tmp))
        res.append(arr[ind])
        del arr[ind]
        neff -= 1

    result(res,num)