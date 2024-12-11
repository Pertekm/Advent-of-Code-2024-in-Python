import copy
import re
import math

#with open("Day6Puzzle1_Input_Sample.txt", "r") as file:
with open("Day6Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

splittedInputData = inputData.split('\n')

two_dimensional_map = [list(line) for line in splittedInputData if line]

#print(f"value at x=6,y=4: {two_dimensional_map[6][4]} is position of the guard")

symbol_guard = "^"
symbol_obstruction = "#"
symbol_visited = "X"
symbol_open_space = "."
symbol_new_obstruction = "O"

## Definitions
# find position of the guard
def get_guard_coordinate(two_dimensional_map, symbol_guard):
    guard_position = [(index, row.index(symbol_guard)) for index, row in enumerate(two_dimensional_map) if symbol_guard in row]
    if len(guard_position) == 1: # only one guard is expected
        return guard_position[0]

def walk_up_the_map(two_dimensional_map, start_position):
    end_position = start_position

    position_y = start_position[1]
    new_position_x = start_position[0]
    while True:
        new_position_x -= 1

        if new_position_x < 0:
            print("reached the top of the map at", new_position_x, position_y)
            raise Exception("reached the top of the map")

        #print("try to walk to pos", new_position_x, position_y, " found: ", two_dimensional_map[new_position_x][position_y])

        if two_dimensional_map[new_position_x][position_y] in [symbol_obstruction, symbol_new_obstruction]:
            #print("obstruction found at", new_position_x, position_y)
            break
        else:
            # mark as visited
            two_dimensional_map[new_position_x][position_y] = symbol_visited
            end_position = (new_position_x, position_y)
    
    return end_position

def walk_right_the_map(two_dimensional_map, start_position):
    end_position = start_position

    position_x = start_position[0]
    new_position_y = start_position[1]
    
    while True:
        new_position_y += 1
        if new_position_y > len(two_dimensional_map[0]) - 1:
            print("reached the right edge of the map at", position_x, new_position_y)
            raise Exception("reached the right edge of the map")
        
        #print("try to walk to pos", position_x, new_position_y, " found: ", two_dimensional_map[position_x][new_position_y])

        if two_dimensional_map[position_x][new_position_y] in [symbol_obstruction, symbol_new_obstruction]:
            #print("obstruction found at", position_x, new_position_y)
            break
        else:
            # mark as visited
            two_dimensional_map[position_x][new_position_y] = symbol_visited
            end_position = (position_x, new_position_y)

    return end_position

def walk_left_the_map(two_dimensional_map, start_position):
    end_position = start_position

    position_x = start_position[0]
    new_position_y = start_position[1]
    
    while True:
        new_position_y -= 1
        if new_position_y < 0:
            print("reached the right edge of the map at", position_x, new_position_y)
            raise Exception("reached the left edge of the map")
        
        #print("try to walk to pos", position_x, new_position_y, " found: ", two_dimensional_map[position_x][new_position_y])

        if two_dimensional_map[position_x][new_position_y] in [symbol_obstruction, symbol_new_obstruction]:
            #print("obstruction found at", position_x, new_position_y)
            break
        else:
            # mark as visited
            two_dimensional_map[position_x][new_position_y] = symbol_visited
            end_position = (position_x, new_position_y)

    return end_position

def walk_down_the_map(two_dimensional_map, start_position):
    end_position = start_position

    position_y = start_position[1]
    new_position_x = start_position[0]
    
    while True:
        new_position_x += 1
        if new_position_x > len(two_dimensional_map) - 1:
            print("reached the top of the map at", new_position_x, position_y)
            raise Exception("reached the bottom of the map")
        
        #print("try to walk to pos", new_position_x, position_y, " found: ", two_dimensional_map[new_position_x][position_y])

        if two_dimensional_map[new_position_x][position_y] in [symbol_obstruction, symbol_new_obstruction]:
            #print("obstruction found at", new_position_x, position_y)
            break
        else:
            # mark as visited
            two_dimensional_map[new_position_x][position_y] = symbol_visited
            end_position = (new_position_x, position_y)

    return end_position

def walk_round(two_dimensional_map, walk_up_the_map, walk_right_the_map, walk_left_the_map, walk_down_the_map, end_position):
    end_position = walk_up_the_map(two_dimensional_map, end_position)
    #print("end position X=", end_position[0], "Y=", end_position[1])
        
    end_position = walk_right_the_map(two_dimensional_map, end_position)
    #print("end position X=", end_position[0], "Y=", end_position[1])

    end_position = walk_down_the_map(two_dimensional_map, end_position)
    #print("end position X=", end_position[0], "Y=", end_position[1])

    end_position = walk_left_the_map(two_dimensional_map, end_position)
    #print("end position X=", end_position[0], "Y=", end_position[1])

    return end_position

# init
two_dimensional_map_original = copy.deepcopy(two_dimensional_map)
symbol_new_obstruction_set = False
endlees_loop_counter = 0
#for rowIndex, rowData in enumerate(two_dimensional_map):
for rowIndex in range(len(two_dimensional_map)):
    #for (columnIndex, cellData) in enumerate(rowData):        
    for columnIndex in range(len(two_dimensional_map[rowIndex])):
        cellData = two_dimensional_map[rowIndex][columnIndex]
        
        if rowIndex == 6:
            pass

        ## put new obstacle
        if symbol_new_obstruction_set == False and cellData == symbol_open_space:
            two_dimensional_map[rowIndex][columnIndex] = symbol_new_obstruction
            symbol_new_obstruction_set = True
        else:
            continue

        print("new obstacle at", rowIndex, columnIndex)
        #for row in two_dimensional_map:
        #        print(''.join(row))

        guard_position = get_guard_coordinate(two_dimensional_map, symbol_guard)
        if guard_position == None:
            print("guard not found")
            break

        #print("guard position X=", guard_position[0], "Y=", guard_position[1])

        # start walking
        try:
            end_position = walk_up_the_map(two_dimensional_map, guard_position)
            #print("end position X=", end_position[0], "Y=", end_position[1])

            end_position = walk_right_the_map(two_dimensional_map, end_position)
            #print("end position X=", end_position[0], "Y=", end_position[1])

            end_position = walk_down_the_map(two_dimensional_map, end_position)
            #print("end position X=", end_position[0], "Y=", end_position[1])

            end_position = walk_left_the_map(two_dimensional_map, end_position)
            #print("end position X=", end_position[0], "Y=", end_position[1])

            ## walk to the end
            walk_round_counter = 0
            walk_round_counter_endlessloop = 20000

            while True:
                walk_round_counter += 1
                if walk_round_counter > walk_round_counter_endlessloop:
                    raise Exception("endless loop")

                end_position = walk_round(two_dimensional_map, walk_up_the_map, walk_right_the_map, walk_left_the_map, walk_down_the_map, end_position)
        except Exception as e:
            if str(e) == "endless loop":
                print("found endless loop")
                endlees_loop_counter += 1
                
                #for row in two_dimensional_map:
                #    print(''.join(row))

                symbol_new_obstruction_set = False
                two_dimensional_map = copy.deepcopy(two_dimensional_map_original)
                rowData = two_dimensional_map[rowIndex]
            else:
                print("reached the edge of the map")

                #for row in two_dimensional_map:
                #    print(''.join(row))

                symbol_new_obstruction_set = False
                two_dimensional_map = copy.deepcopy(two_dimensional_map_original)
                rowData = two_dimensional_map[rowIndex]

print("endless loop counter: ", endlees_loop_counter)                        