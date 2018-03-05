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

def searchAfterMice(maze,x,y,path, target):
    if (maze[x][y] == target):
        path.append([x,y])
        return True
    if ((maze[x][y] == "|") or (maze[x][y] == "M")):
        return False
    maze[x][y] = "M"
    result = searchAfterMice(maze,x,   y-1,path,target)
    if result:
        path.append([x,y])
        return True
    result = searchAfterMice(maze,x,   y+1,path,target)
    if result:
        path.append([x,y])
        return True
    result = searchAfterMice(maze,x+1, y  ,path,target)
    if result:
        path.append([x,y])
        return True
    result = searchAfterMice(maze,x-1, y  ,path,target)
    if result:
        path.append([x,y])
        return True

x,y = findStartIndex(MAZE,"S")
target = "Z"

maze = copy.deepcopy(MAZE)
path = []
foundX = searchAfterMice(maze,x,y,path,target)

for i in MAZE:
    print(i)

print()
for i in path[1:-1]:
    MAZE[i[0]][i[1]] = "M"

for i in MAZE:
    print(i)
