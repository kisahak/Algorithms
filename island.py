import collections
#LC 200, how many islands are in a grid
#an island = a "1" or groups of "1"s that are compeletely surrounded by "0"s or at the ends of the matrix 
#a priority queue and visit set are used to keep track of current and visited points 
#BSF algoirthm 

def numIslands( grid) -> int:
    if not grid:
        return 0
    rows,cols = len(grid),len(grid[0]) #matrix size 
    visit = set() #does not allow duplicate values to be added 
    islands = 0
    def BFS(r,c): #breadth first search algorithm to check all neighbors and update a queue within the island grid 
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
#The grid below is an example of one big island, as all "1"s have connected neighbors
#grid = [["1","1","1","1","0"],
#        ["1","1","0","1","0"],
#        ["1","1","0","0","0"],
#        ["0","0","0","0","0"]] 

#The grid below is an example of one big island, and two small islands, giving a total of three islands 
#grid = [["1","1","1","0","0"],
#        ["1","1","0","1","0"],
#        ["1","1","0","0","0"],
#        ["0","0","0","0","1"]] 


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(grid)
x = numIslands(grid) 
print("number of islands =")
print(x)
