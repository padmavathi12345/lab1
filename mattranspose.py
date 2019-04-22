X= [[6,8],[9,27],[2,43]]

result = [[0,0,0],[0,0,0]]

for i in range(len(X)):
 for j in range(len(X[0])):
                    result[j][i] = X[i][j]

for r in result:
 print(r)

