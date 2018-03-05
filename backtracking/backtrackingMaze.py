import copy

#MAZE = [[1,1,1,1,1],
#        [1,3,1,1,1],
#        [1,0,1,4,1],
#        [1,0,0,0,1],
#        [1,1,1,1,1]]


'''
MAZE = [[1,1,1,1,1,1,1],
        [1,3,1,1,1,1,1],
        [1,0,1,0,0,0,1],
        [1,0,0,0,1,0,1],
        [1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,1,1,0,1],
        [1,1,4,1,1,0,1],
        [1,1,1,1,1,1,1],]

MAZE = [["X","X","X","X","X","X","X"],
        ["X","S","X","X","X","X","X"],
        ["X"," ","X"," "," "," ","X"],
        ["X"," "," "," ","X"," ","X"],
        ["X","X","X","X","X"," ","X"],
        ["X"," "," "," "," "," ","X"],
        ["X","X"," ","X","X"," ","X"],
        ["X","X","Z","X","X"," ","X"],
        ["X","X","X","X","X","X","X"],]
'''

MAZE = [["|","|","|","|","|","|","|"],
        ["|","S","|","|","|","|","|"],
        ["|"," ","|"," "," "," ","|"],
        ["|"," "," "," ","|"," ","|"],
        ["|","|","|","|","|"," ","|"],
        ["|"," "," "," "," "," ","|"],
        ["|","|"," ","|","|"," ","|"],
        ["|","|","Z","|","|"," ","|"],
        ["|","|","|","|","|","|","|"],]


def findStartIndex(maze,startIndex):
    for i in range(len(maze)):
        for ii in range(len(maze[i])):
            if maze[i][ii] == startIndex:
                return i,ii

def searchAfterMice(maze,row,col,path, target):
    if (maze[row][col] == target):
        path.append([row,col])
        return True
    if ((maze[row][col] == "|") or (maze[row][col] == "M")):
        return False
    maze[row][col] = "M"
    if searchAfterMice(maze,row,col-1,path,target):
        path.append([row,col])
        return True
    if searchAfterMice(maze,row,col+1,path,target):
        path.append([row,col])
        return True
    if searchAfterMice(maze,row+1,col,path,target):
        path.append([row,col])
        return True
    if searchAfterMice(maze,row-1,col,path,target):
        path.append([row,col])
        return True

row,col = findStartIndex(MAZE,"S")
target = "Z"

maze = copy.deepcopy(MAZE)
path = []
foundX = searchAfterMice(maze,row,col,path,target)

for i in MAZE:
    print(i)

print()
for i in path[1:-1]:
    MAZE[i[0]][i[1]] = "M"

for i in MAZE:
    print(i)
