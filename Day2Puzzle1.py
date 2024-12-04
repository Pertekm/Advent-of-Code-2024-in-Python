with open("Day2Puzzle1_Input.txt", "r") as file:
    data = file.read()

countSaveReports = 0

for lineIndex, line in enumerate(data.splitlines(), start=1):
    #print("line " + str(lineIndex) + ": " + line)
    numbers = line.split()
    #print("numbers of line/report:", numbers)

    saveReport = False
    increasing = False
    decreasing = False
    isFirstNumber = True

    for numberIndex, number in enumerate(numbers):
        try:
            number = int(number)
            nextNumber = int(numbers[numberIndex + 1])

            if number < nextNumber:
                if abs(number - nextNumber) > 3 or ( isFirstNumber == False and increasing == False ):
                    print("unsafe report: ", numbers)
                    saveReport = False
                    break

                increasing = True
                saveReport = True
                isFirstNumber = False
            elif number > nextNumber:
                if abs(number - nextNumber) > 3 or ( isFirstNumber == False and decreasing == False ):
                    print("unsafe report: ", numbers)
                    saveReport = False
                    break

                decreasing = True
                saveReport = True
                isFirstNumber = False
            else:
                print("unsafe report: ", numbers)
                saveReport = False
                break
        except IndexError:
            #print(f"IndexError: list index out of range for index {numberIndex}")
            pass

    if(saveReport):
        #print("safe report: ", numbers)
        countSaveReports += 1

print("countSaveReports:", countSaveReports)