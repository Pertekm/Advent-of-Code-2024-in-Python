from itertools import product

#with open("Day7Puzzle1_Input_Sample.txt", "r") as file:
with open("Day7Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

operatorsConst = ['+', '*']
splittedInputData = inputData.split('\n')
sumOfTestValuesOfSolvedEquations = 0

for equationIndex in range(len(splittedInputData)):
    inputEquation = splittedInputData[equationIndex].split(':')

    testValue = inputEquation[0]
    numbers = inputEquation[1].split(' ')
    numbers.remove('')
    print("input equation from index ", equationIndex ," with test value: ", testValue, " and numbers: ", numbers)
    # Generate all possible operator combinations
    # f.e. for two numbers there are 4 possible combinations:
    # 1. + +
    # 2. + *
    # 3. * +
    # 4. * *
    operatorCombinations = list(product(operatorsConst, repeat=len(numbers) - 1))
    
    for operatorCombination in operatorCombinations:
        for numberIndex in range(len(numbers)):
            if numberIndex == 0:
                # First Number is start value
                result = int(numbers[numberIndex])
                continue

            operator = operatorCombination[numberIndex - 1]    
            if operator == '+':
                result += int(numbers[numberIndex])
            elif operator == '*':
                result *= int(numbers[numberIndex])

        if result == int(testValue):
            print("equation solved: test value: ", testValue, " numbers: ", numbers, " with operator combination: ", operatorCombination)
            sumOfTestValuesOfSolvedEquations += int(testValue)
            break

print("Sum of test values of solved equations: ", sumOfTestValuesOfSolvedEquations)