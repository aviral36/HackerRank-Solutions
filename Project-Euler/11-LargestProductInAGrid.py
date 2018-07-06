import sys

grid = []
for _ in xrange(20):
    temp = map(int,raw_input().strip().split(' '))
    grid.append(temp)

prod_hr=[]
prod_diar=[]
prod_dial=[]
prod_vert=[]
high=[]
for row in range(len(grid)):
    for column in range(len(grid)-3):
        producth=(grid[row][column])*(grid[row][column+1])*(grid[row][column+2])*(grid[row][column+3])
        prod_hr.append(producth)
high.append(max(prod_hr))

for row in range(len(grid)-3):
    for column in range(len(grid)):
        productv=(grid[row][column])*(grid[row+1][column])*(grid[row+2][column])*(grid[row+3][column])
        prod_vert.append(productv)
high.append(max(prod_vert))

for row in range(len(grid)-3):
    for column in range(len(grid)-3):
        productdr=(grid[row][column])*(grid[row+1][column+1])*(grid[row+2][column+2])*(grid[row+3][column+3])
        prod_diar.append(productdr)
high.append(max(prod_diar))

for row in range(3,len(grid)):
    for column in range(0,len(grid)-3):
        productdl=(grid[row][column])*(grid[row-1][column+1])*(grid[row-2][column+2])*(grid[row-3][column+3])
        prod_dial.append(productdl)
high.append(max(prod_dial))

print max(high)
