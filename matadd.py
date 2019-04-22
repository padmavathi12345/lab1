X = [[0,0,0],[0,0,0],[0 ,0,0]]

Y = [[6,8,1],[9,27,5],[2,43,31]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
 for j in range(len(X[0])):
                    result[i][j] = X[i][j] +Y[i][j]

for r in result:
 print(r)

