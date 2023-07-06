import collections

def numIslands( grid) -> int:
    if not grid:
        return 0
    rows,cols = len(grid),len(grid[0]) #matrix size 
    visit = set() #does not allow duplicate values to be added 
    islands = 0
    def BFS(r,c): #breathe first search algorithm to check all neighbors and update a queue within the island grid 
        q = collections.deque()
        q.append((r,c))
        visit.add((r,c)) #adding specific row/column to queue and visited set
                            #double parenthese (touple) so that they added as a pair 
        while q: 
            row,col =q.popleft() #removes row,col from the queue 
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                r,c = row +dr, col + dc #updates r, c to check the neighbors around it after pop row,col
                if ((r in range(rows)) and 
                (c in range(cols)) and 
                (grid[r][c]=="1") and 
                ((r,c) not in visit)): 
                #checking to see if neighbors are in range of matrix and not in visit set 
                    q.append((r,c ))
                    visit.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit: #only islands with no checked neighbors will be passed with BFS
                BFS(r,c)
                islands+=1 
    
    return islands 
        

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(grid)
x = numIslands(grid) 
print("number of islands =")
print(x)