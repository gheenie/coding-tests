def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    totalCost = 0
    
    if initR != finalR:
        if initR < finalR:
            while initR != finalR:
                totalCost += costRows[initR]
                initR += 1
        else:
            while initR != finalR:
                totalCost += costRows[initR]
                initR -= 1
    
    if initC != finalC:
        if initC < finalC:
            while initC != finalC:
                totalCost += costCols[initC]
                initC += 1
        else:
            while initC != finalC:
                totalCost += costCols[initC]
                initC -= 1
    
    return totalCost

print(minCost(4, 4, 1, 0, 2, 3, [1, 2, 3], [4, 5, 6]))
print(minCost(3, 3, 0, 0, 1, 2, [2, 5], [6, 1]))
