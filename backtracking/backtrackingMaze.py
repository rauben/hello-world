#MAZE = [[1,1,1,1,1],
#        [1,3,1,1,1],
#        [1,0,1,4,1],
#        [1,0,0,0,1],
#        [1,1,1,1,1]]



MAZE = [[1,1,1,1,1,1,1],
        [1,3,1,1,1,1,1],
        [1,0,1,0,0,0,1],
        [1,0,0,0,1,0,1],
        [1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,1,1,0,1],
        [1,1,4,1,1,0,1],
        [1,1,1,1,1,1,1],]


def findStartIndex(maze,startIndex):
    for i in range(len(maze)):
        for ii in range(len(maze[i])):
            if maze[i][ii] == startIndex:
                return i,ii

def searchAfterMice(maze,x,y,target):
    if (maze[x][y] == target):
        return True
    if ((maze[x][y] == 1) or (maze[x][y] == 2)):
        return False
    maze[x][y] = 2
    result = searchAfterMice(maze,x,   y-1,target)
    if result:
        return True
    result = searchAfterMice(maze,x,   y+1,target)
    if result:
        return True
    result = searchAfterMice(maze,x+1, y  ,target)
    if result:
        return True
    result = searchAfterMice(maze,x-1, y  ,target)
    if result:
        return True

x,y = findStartIndex(MAZE,3)
target = 4

path = []
foundX = searchAfterMice(MAZE,x,y,target)

print(MAZE)