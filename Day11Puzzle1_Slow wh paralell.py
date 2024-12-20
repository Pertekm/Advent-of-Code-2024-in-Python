import numpy as np
import time

#with open("Day11Puzzle1_Input_Sample_Small.txt", "r") as file:
#with open("Day11Puzzle1_Input_Sample_Larger.txt", "r") as file:
with open("Day11Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

stones = inputData.split(" ")
print(stones)
# stones = list(map(int, stones)) # better performance than list comprehension?
for blinkNr in range(75):
    i = 0
    blink_start_time = time.time()
    while i < len(stones):
        stoneNr = int(stones[i])
        #print("Stone Nr before: ", stoneNr)

        if stoneNr == 0:
            stoneNr = 1
            stones[i] = stoneNr
            #print("Stone Nr after: ", stoneNr)
            i += 1
            continue

        if len(str(stoneNr)) % 2 == 0:
            # even number of digits.
            # replace by two stones.
            #  The left half of the digits are engraved on the new left stone,
            #  and the right half of the digits are engraved on the new right stone.
            # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            stoneNrLeft = int(str(stoneNr)[:len(str(stoneNr))//2])
            stoneNrRight = int(str(stoneNr)[len(str(stoneNr))//2:])
            stones[i] = stoneNrLeft
            stones.insert(i+1, stoneNrRight)
            #print("Stone Nrs after: ", stoneNrLeft, stoneNrRight)
            i += 2
            continue

        stoneNr *= 2024
        stones[i] = stoneNr
        #print("Stone Nr after: ", stoneNr)
        i += 1

    blink_elapsed_time = time.time() - blink_start_time
    print("blinkNr: ", blinkNr+1 , " stone count: ", len(stones), " elapsed time: ", blink_elapsed_time, " stones: ", stones)