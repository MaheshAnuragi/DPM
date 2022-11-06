# Insert import statements below

def backtrack(x,y,maze,destination,n,m):
    if x <0 or y < 0 or x >= n or y >=m  or maze[x][y] != 'w':
        return False
    temp = maze[x][y]
    maze[x][y] = 'p'
    if x == destination[0] and y == destination[1]:
        return True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if backtrack(nx,ny,maze,destination,n,m):
            return True
    maze[x][y] = temp


def pathFinder(maze, source, destination):
    
    n = len(maze)
    m = len(maze[0])
    

    if backtrack(source[0],source[1],maze,destination,n,m):
        return maze
    return []
    
    
if __name__ == "__main__":
    
    maze = [
            ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c','c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
            ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w','c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
            ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c','c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
            ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w', 'c', 'w'],
            ['w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c','c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w'],
            ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'c', 'w', 'w','w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c','w', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
            ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c','c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'],
            ['w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c','w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']
            ]
    
    source = []
    print("Enter the source points: ")
    for i in range(2):
        n = int(input())
        source.append(n)
    
    print("Enter the destination points: ")
    destination = []
    for i in range(2):
        n = int(input())
        destination.append(n)
    
    maze = pathFinder(maze, source, destination)
    if (len(maze) == 0):
        print(maze)
    else : 
        for x in maze:
            print(x)
    