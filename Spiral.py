
  
matrix = []
tmp = []
m = int(input("Enter Number of Rows of Matrix\n"))
n = int(input("Enter Number of Columns of Matrix\n"))

print("Enter Matrix Values")
for i in range(m):
    for j in range(n):
        print("Enter matrix[",i,"][",j,"]")
        tmp.append(int(input()))
    matrix.append(tmp)
    tmp = []
for i in matrix:
    print(i)

print("Spiral Pattern for Above Matrix is\n")

row = 0
col = 0

while (row < m and col < n) : 
          
        for i in range(col, n) : 
            print(matrix[row][i], end = " ") 
              
        row += 1
  
        for i in range(row, m) : 
            print(matrix[i][n - 1], end = " ") 
              
        n -= 1
  
        if ( row < m) : 
              
            for i in range(n - 1, (col - 1), -1) : 
                print(matrix[m - 1][i], end = " ") 
              
            m -= 1
          
        if (col < n) : 
            for i in range(m - 1, row - 1, -1) : 
                print(matrix[i][col], end = " ") 
              
            col += 1

