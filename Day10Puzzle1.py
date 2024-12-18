import numpy as np

#with open("Day10Puzzle1_Input_Sample_Small.txt", "r") as file:
with open("Day10Puzzle1_Input_Sample_Larger.txt", "r") as file:
#with open("Day10Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

lines = []
for line in inputData.split("\n"):
    lines.append(np.array(list(line)))

map = np.array(lines, dtype=int)

#print(map)

reachedTopCount = 0
maxHeight = np.max(map)
indices = np.where(map == 0)
for tryNumber in range(2):
    print("try number: ", tryNumber)
    print(map)
    
    for startPosIndex in range(len(indices[0])):
        positionX = indices[0][startPosIndex]
        positionY = indices[1][startPosIndex]
        print("start position: ", positionX, positionY)

        currentHeight = map[positionX, positionY]

        moved = True
        notMovedCount = 0
        while moved == True and currentHeight < maxHeight:

            # try to move right
            try:
                if map[positionX, positionY+1] == currentHeight + 1:
                    positionY = positionY+1
                    currentHeight = map[positionX, positionY]
                    map[positionX, positionY] = -1 # mark as visited
                    notMovedCount = 0
                    print("moved right to: ", positionX, positionY, " with height: ", currentHeight)
                    if currentHeight == maxHeight:
                        print("reached one top of the map")
                        reachedTopCount += 1
                    continue
            except IndexError:
                notMovedCount += 1

            # try to move left
            try:
                if map[positionX, positionY-1] == currentHeight + 1:
                    positionY = positionY-1
                    currentHeight = map[positionX, positionY]
                    map[positionX, positionY] = -1 # mark as visited
                    notMovedCount = 0
                    print("moved left to: ", positionX, positionY, " with height: ", currentHeight)
                    if currentHeight == maxHeight:
                        print("reached one top of the map")
                        reachedTopCount += 1
                    continue
            except IndexError:
                notMovedCount += 1

            # try to move down
            try:
                if map[positionX+1, positionY] == currentHeight + 1:
                    positionX = positionX+1
                    currentHeight = map[positionX, positionY]
                    map[positionX, positionY] = -1 # mark as visited
                    notMovedCount = 0
                    print("moved down to: ", positionX, positionY, " with height: ", currentHeight)
                    if currentHeight == maxHeight:
                        print("reached one top of the map")
                        reachedTopCount += 1
                    continue
            except IndexError:
                notMovedCount += 1

            # try to move up
            try:
                if map[positionX-1, positionY] == currentHeight + 1:
                    positionX = positionX-1
                    currentHeight = map[positionX, positionY]
                    map[positionX, positionY] = -1 # mark as visited
                    notMovedCount = 0
                    print("moved up to: ",positionX, positionY, " with height: ", currentHeight)
                    if currentHeight == maxHeight:
                        print("reached one top of the map")
                        reachedTopCount += 1
                    continue
            except IndexError:
                notMovedCount += 1

            if notMovedCount == 4 or notMovedCount == 0:
                moved = False

print("reachedTopCount: ", reachedTopCount) # result is not correct. to low because multiple/split paths are not recognized. Recursion needed?