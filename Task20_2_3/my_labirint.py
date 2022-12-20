def printArr(Arr):
    for i in Arr:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()

def foundPath(pathArr, finPoint, cycle_count):
    weight = 1
    for i in range(cycle_count):
        for x in range(len(pathArr)):
            for y in range(len(pathArr[x])):
                if pathArr[x][y] == weight:
                    # Вверх
                    if x > 0 and pathArr[x - 1][y] == 0:
                        pathArr[x - 1][y] = weight + 1
                    # Вправо
                    if y < (len(pathArr[x]) - 1) and pathArr[x][y + 1] == 0:
                        pathArr[x][y + 1] = weight + 1
                    # Влево
                    if y > 0 and pathArr[x][y - 1] == 0:
                        pathArr[x][y - 1] = weight + 1
                    # Вниз
                    if x < (len(pathArr) - 1) and pathArr[x + 1][y] == 0:
                        pathArr[x + 1][y] = weight + 1

                    if (x == finPoint[0] and y == finPoint[1]):
                        return True
 #       printArr(pathArr)
 #       print("*********************")
        weight += 1
    return False

def printPath(labirint, posOut):
    x = posOut[0]
    y = posOut[1]
    point = labirint[x][y]
    path = []
    while point >= 1:
        point -= 1
        # Вверх
        if x >= 0 and labirint[x - 1][y] == point:
            x -= 1
            path.append("Вниз") # пришли сюда наоборот
        # Вниз
        if x <= len(labirint) and labirint[x + 1][y] == point:
            x += 1
            path.append("Вверх") # пришли сюда наоборот
        # Влево
        if y >= 0 and labirint[x][y - 1] == point:
            y -= 1
            path.append("Вправо") # пришли сюда наоборот
        # Вправо
        if y <= len(labirint) and labirint[x][y + 1] == point:
            y += 1
            path.append("Влево") # пришли сюда наоборот
    return path[::-1]

labirint = []
with open('labirint.txt') as myFile:
    for line in myFile:
        labirint.append(line.replace('\n','').split())

ii = 0
posIn = ()
posOut = ()
cycle_count = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            posIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            posOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
            cycle_count += 1
        jj += 1
    ii += 1

if not foundPath(labirint, posOut, cycle_count):
    print("Path not found")
else:
    result = printPath(labirint, posOut)
    printArr(labirint)
    print("Путь в лабиринте = ", result)