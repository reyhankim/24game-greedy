# Define operator symbol for each allowed operations
op_sym = ['+','-','*','/']
 
def scoreToOp(opScore):
    return {
        5 : op_sym[0],      # Add
        4 : op_sym[1],      # Subtract
        3 : op_sym[2],      # Multiply
        2 : op_sym[3],      # Divide
    }[opScore]
 
def opToScore(op):
    return {
        op_sym[0] : 5,      # Add
        op_sym[1] : 4,      # Subtract
        op_sym[2] : 3,      # Multiply
        op_sym[3] : 2,      # Divide
    }[op]
 
def distToTarget(some_value, target_value):
    return (abs(target_value - some_value))
 
def determineTarget(operandRemaining):
    return {
        1 : 24,
        2 : ,
        3 : 21,
        4 : 10,
    }[operandRemaining]
 
def printSolution(current_result, expected_math_result):
    current_op = [current_result[1],current_result[3],current_result[5]]
    current_int = [current_result[0],current_result[2],current_result[4],current_result[6]]
    finalOpScore = opToScore(current_op[0]) + opToScore(current_op[1]) + opToScore(current_op[2]) - distToTarget(expected_math_result, 24)
 
    if ((current_op[1] == op_sym[2]) or (current_op[1] == op_sym[3])) and ((current_op[0] == op_sym[0]) or (current_op[0] == op_sym[1])):
        solution = '(%d %s %d) %s %d %s %d' % (current_int[0],current_op[0],current_int[1],current_op[1],current_int[2],current_op[2],current_int[3])
        """ print(solution, ' = ', eval(solution), '\n')
        print('Operator score: ', finalOpScore-2, '\n') """
        return(solution , finalOpScore-2)
    else:
        solution = '%d %s %d %s %d %s %d' % (current_int[0],current_op[0],current_int[1],current_op[1],current_int[2],current_op[2],current_int[3])
        """ print(solution, ' = ', eval(solution), '\n')
        print('Operator score: ', finalOpScore, '\n') """
        return(solution, finalOpScore)
 
def mathChunkProcess1(operand1, operatorScore, operand2):
    return eval('%d %s %d' % (operand1,scoreToOp(operatorScore),operand2))
 
def getScore1(operand1, operatorScore, operand2):
    return eval('%d - %d' % (operatorScore, distToTarget(eval('%d %s %d' % (operand1,scoreToOp(operatorScore),operand2)),24)))
 
def getScore2(operand1, operatorScore, operand2, operandRemaining):
    a = eval('%d %s %d' % (operand1, scoreToOp(operatorScore), operand2)) % 4

    return eval("%d+%d-%d-%d" % (operand1, operand2, distToTarget(eval('%d %s %d' % (operand1, scoreToOp(operatorScore), operand2)), determineTarget(operandRemaining)), a))
 
def solve1(arr):
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
        for i in range(4):
            ope = 5-i
            for j in range(neff):
                sc = getScore1(num,ope,arr[j])
                if (cho  < sc):
                    cho = sc
                    ind = j
                    tmp = ope
        te = arr[ind]
        num = mathChunkProcess1(num,tmp,te)
        opp.append(tmp)
        res.append(scoreToOp(tmp))
        res.append(arr[ind])
        del arr[ind]
        neff -= 1
    return printSolution(res,num)
 
def solve2(arr):
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
        for i in range(4):
            ope = 5-i
            for j  in range(neff):
                sc = getScore2(num,ope,arr[j],neff)
                if (cho  < sc):
                    cho = sc
                    ind = j
                    tmp = ope
        te = arr[ind]
        num = mathChunkProcess1(num,tmp,te)
        opp.append(tmp)
        res.append(scoreToOp(tmp))
        res.append(arr[ind])
        del arr[ind]
        neff -= 1
    return printSolution(res,num)
