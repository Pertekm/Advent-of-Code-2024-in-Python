with open("Day1Puzzle1_Input.txt", "r") as file:
    data = file.read()

numbersLeft = []
numbersRight = []

for lineIndex, line in enumerate(data.splitlines(), start=1):
    # print("line " + str(lineIndex) + ": " + line)
    numbers = line.split()
    # print("numbers:", numbers)
    numberLeft = numbers[0]
    numberRight = numbers[1]
    #print("numberLeft:", numberLeft, " numberRight:", numberRight)
    numbersLeft.append(int(numberLeft))
    numbersRight.append(int(numberRight))

#print("numbersLeft:", numbersLeft)
#print("numbersRight:", numbersRight)

numbersLeft.sort()
numbersRight.sort()

#print("sorted numbersLeft:", numbersLeft)
#print("sorted numbersRight:", numbersRight.len)

totalDistance = 0

for numberLeftIndex, numberLeft in enumerate(numbersLeft):
    try:
        numberRight = numbersRight[numberLeftIndex]
        distance = abs(numberRight - numberLeft)
        #print("numberLeftIndex", numberLeftIndex, "numberLeft:", numberLeft, " numberRight:", numberRight, " absolute distance:", distance)
        totalDistance += distance
    except IndexError:
        print(f"IndexError: list index out of range for index {numberLeftIndex}")
   
print("totalDistance:", totalDistance)