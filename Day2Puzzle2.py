with open("Day2Puzzle1_Input.txt", "r") as file:
    data = file.read()

countSaveReports = 0

def is_safe_report(numbers):
    saveReport = False
    increasing = False
    decreasing = False
    isFirstNumber = True

    for numberIndex, number in enumerate(numbers):
        try:
            number = int(number)
            nextNumber = int(numbers[numberIndex + 1])

            if number < nextNumber:
                if abs(number - nextNumber) > 3 or (isFirstNumber == False and increasing == False):
                    return False

                increasing = True
                saveReport = True
                isFirstNumber = False
            elif number > nextNumber:
                if abs(number - nextNumber) > 3 or (isFirstNumber == False and decreasing == False):
                    return False

                decreasing = True
                saveReport = True
                isFirstNumber = False
            else:
                return False
        except IndexError:
            pass

    return saveReport

for lineIndex, line in enumerate(data.splitlines(), start=1):
    numbers = line.split()
    if is_safe_report(numbers):
        countSaveReports += 1
    else:
        print("try tolerating unsafe report: ", numbers)

        for numberIndex, number in enumerate(numbers):
            numbersOneRevmoved = numbers.copy()
            numbersOneRevmoved.pop(numberIndex)
            if is_safe_report(numbersOneRevmoved):
                countSaveReports += 1
                break

        pass

print("countSaveReports:", countSaveReports)