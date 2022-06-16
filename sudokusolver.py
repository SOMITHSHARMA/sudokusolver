import numpy as np
r=9
c=9
values=list(map(int,input().split()))
grid=np.array(values).reshape(r,c)
def possible(row,column,number):
    global grid
    #checking if there exsit the number in the row
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    #checking if the number is in the any column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    #checking if the number is in the square
    x0=(column//3)*3
    y0=(row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==number:
                return False
    return True
def solve():
    global grid 
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column]==0:
               for number in range(1,10):
                if possible(row,column,number):
                    grid[row][column]=number 
                    solve()
                    grid[row][column]=0
               return 
    print(np.matrix(grid))
   
    
solve()
