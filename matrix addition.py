X = [[2,2],[2,2],[2,2]]
Y = [[2,2],[2,2],[2,2]]
result = [[0,0],[0,0], [0,0]]      
for i in range(len(X)):
   for j in range(len(Y[0])):
      
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
