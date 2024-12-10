import re
import math

with open("Day6Puzzle1_Input_Sample.txt", "r") as file:
#with open("Day6Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

splittedInputData = inputData.split('\n')

two_dimensional_map = [list(line) for line in splittedInputData if line]

#print(f"value at x=6,y=4: {two_dimensional_map[6][4]} is position of the guard")

symbol_guard = "^"
symbol_obstruction = "#"
symbol_visited = "X"
symbol_open_space = "."

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

        if two_dimensional_map[new_position_x][position_y] == symbol_obstruction:
            print("obstruction found at", new_position_x, position_y)
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

        if two_dimensional_map[position_x][new_position_y] == symbol_obstruction:
            print("obstruction found at", position_x, new_position_y)
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

        if two_dimensional_map[position_x][new_position_y] == symbol_obstruction:
            print("obstruction found at", position_x, new_position_y)
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

        if two_dimensional_map[new_position_x][position_y] == symbol_obstruction:
            print("obstruction found at", new_position_x, position_y)
            break
        else:
            # mark as visited
            two_dimensional_map[new_position_x][position_y] = symbol_visited
            end_position = (new_position_x, position_y)

    return end_position

guard_position = get_guard_coordinate(two_dimensional_map, symbol_guard)
print("guard position X=", guard_position[0], "Y=", guard_position[1])

end_position = walk_up_the_map(two_dimensional_map, guard_position)
print("end position X=", end_position[0], "Y=", end_position[1])

end_position = walk_right_the_map(two_dimensional_map, end_position)
print("end position X=", end_position[0], "Y=", end_position[1])

end_position = walk_down_the_map(two_dimensional_map, end_position)
print("end position X=", end_position[0], "Y=", end_position[1])

end_position = walk_left_the_map(two_dimensional_map, end_position)
print("end position X=", end_position[0], "Y=", end_position[1])

## walk to the end
try:
    while True:
        end_position = walk_up_the_map(two_dimensional_map, end_position)
        print("end position X=", end_position[0], "Y=", end_position[1])

        end_position = walk_right_the_map(two_dimensional_map, end_position)
        print("end position X=", end_position[0], "Y=", end_position[1])

        end_position = walk_down_the_map(two_dimensional_map, end_position)
        print("end position X=", end_position[0], "Y=", end_position[1])

        end_position = walk_left_the_map(two_dimensional_map, end_position)
        print("end position X=", end_position[0], "Y=", end_position[1])
except Exception as e:
    print("reached the edge of the map")
    for row in two_dimensional_map:
        print(''.join(row))

# count the visited spaces
visited_spaces = 0
for row in two_dimensional_map:
    visited_spaces += row.count(symbol_visited)

visited_spaces += 1 # for not sample data. why?
print("visited spaces: ", visited_spaces)