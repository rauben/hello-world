import copy

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

def drawPath(maze,path, pathSymbol):
    for i in path[1:-1]:
        maze[i[0]][i[1]] = pathSymbol

def makeMaze():  
    maze = [["|","|","|","|","|","|","|","|","|"],
            ["|","S","|","|","|","|","|","Z","|"],
            ["|"," ","|"," "," "," ","|"," ","|"],
            ["|"," "," "," ","|"," ","|"," ","|"],
            ["|","|","|","|","|"," ","|"," ","|"],
            ["|"," "," "," "," "," "," "," ","|"],
            ["|","|"," ","|","|"," ","|","|","|"],
            ["|"," "," ","|","|"," "," "," ","|"],
            ["|","|","|","|","|","|","|","|","|"],]
    return maze

def printMaze(maze):
    for i in maze:
        print(i)

if __name__ == "__main__":

    path = []
    target = "Z"
    start  = "S"
    pathSymbol = "M"

    maze = makeMaze()
    row,col = findStartIndex(maze,start)
    mazeCopy = copy.deepcopy(maze)

    found = searchAfterMice(mazeCopy,row,col,path,target)

    printMaze(maze)
    print()
    enter = input("Press Enter...")
    drawPath(maze,path,pathSymbol)
    printMaze(maze)
