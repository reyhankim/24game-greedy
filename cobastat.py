from algoColl import *
from random import randint

#Number of wins for each algorithm
ATTEMPT = 5000
count1 = 0
count2 = 0
draws = 0
chosen = 0
delta = 0
exp1 = 0
exp2 = 0
delta1_24 = 0
delta2_24 = 0
point1 = 0
point2 = 0

for tries in range(0,ATTEMPT):
    #fill array
    arr1 = []
    arr2 = []
    for i in range(0,4):
        x = randint(1,13)
        arr1.append(x)
        arr2.append(x)

    result2 = solve2(arr2)
    result1 = solve1(arr1)

    if result1[1] > result2[1]:
        count1 += 1
        chosen += result1[1]
    elif result1[1] < result2[1]:
        count2 += 1
        chosen += result2[1]
    else:
        draws += 1
        chosen += result2[1]
    
    eval1 = eval(result1[0])
    eval2 = eval(result2[0])

    point1 += result1[1] 
    point2 += result2[1] 
    delta += abs(result1[1] - result2[1])
    exp1 += eval1
    delta1_24 += (eval1 - 24)
    exp2 += eval2
    delta2_24 += (eval2 - 24)

print("1 wins: ", count1/ATTEMPT)
print("2 wins: ", count2/ATTEMPT)
print("draws: ", draws/ATTEMPT)
print("average delta: ", delta/ATTEMPT)
print("chosen point average: ", chosen/ATTEMPT)
print("point1 average: ", point1/ATTEMPT)
print("point2 average: ", point2/ATTEMPT)
print("average of exp1: ", exp1/ATTEMPT)
print("average of exp2: ", exp2/ATTEMPT)
print("delta algo1 with 24: ", delta1_24/ATTEMPT)
print("delta algo2 with 24: ", delta2_24/ATTEMPT)        

