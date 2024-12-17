from itertools import product

#with open("Day9Puzzle1_Input_Sample.txt", "r") as file:
with open("Day9Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

disk_map_raw = inputData
disk_map_splitted = []

for index, disk_map_entry in enumerate(disk_map_raw):
    if index % 2 == 0:
        # Process even index
        length_of_file = disk_map_entry
        if index == len(disk_map_raw) - 1:
            # last entry without free space entry
            length_of_free_space = 0
            disk_map_splitted.append((length_of_file, length_of_free_space))
    else:
        # Process odd index
        length_of_free_space = disk_map_entry
        disk_map_splitted.append((length_of_file, length_of_free_space))

#print(disk_map_splitted)

# generate blocks from disk_map_splitted
blocks = ''
for index, entry in enumerate(disk_map_splitted):
    for _ in range(int(entry[0])):
        blocks += str(index)
        #print("index: ", index, " as string: ", str(index))

    for _ in range(int(entry[1])):
        blocks += '.'

print(blocks)

# move file blocks from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks)
blocks_rearranged = blocks
print("len(blocks_rearranged): ", len(blocks_rearranged))

# find the last file block
for i in range(len(blocks_rearranged)-1, 0, -1):
    if i % 100 == 0:
        print("block nr.: ", i)
    
    if blocks_rearranged[i] != '.':
        last_file_block = i

        # find the first free space block
        first_free_space = blocks_rearranged.find('.')
        
        if first_free_space > last_file_block:
            break

        # replace the first free space block with the last file block
        blocks_rearranged = list(blocks_rearranged)
        blocks_rearranged[first_free_space] = blocks_rearranged[last_file_block]
        blocks_rearranged[last_file_block] = '.'
        blocks_rearranged = ''.join(blocks_rearranged)


print(blocks_rearranged)

# calculate filesystem checksum
checksum = 0
for index, entry in enumerate(blocks_rearranged):
    if entry == '.':
        break

    checksum += index * int(entry)

print(checksum) # wrong result 91486187825, should be higher (13-stellig statt 11-stellig)