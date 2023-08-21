def groupDivision(levels, maxSpread):
    levels.sort()
    
    # Initiate variables to keep track of the lowest skill of a group,
    # starting with the first element
    groups = 1
    current_level = levels[0]
    
    for level in levels:
        # If an element is above the lowest skill of the current
        # group + the max spread, begin a new group
        if level > (current_level + maxSpread):
            groups += 1
            current_level = level
            
    return groups

def numPaths(warehouse):
    paths_matrix = [[] * total_rows]

    total_rows = len(warehouse)
    total_columns = len(warehouse[0])
    current_row = 0
    current_column = 0
    next_rows = [[] * total_columns]
    total_paths = 0

    # Not out of bounds or on a 0 block after going down a row
    while current_row != total_rows or warehouse[current_row][current_column] != 0:
        if warehouse[current_row][current_column + 1] == 1:
            next_rows[current_column + 1].append(current_row)
            total_paths += 1

        current_row += 1

    current_column += 1

    while current_column != total_columns:
        for i, current_row in enumerate(next_rows[current_column]):
            total_paths -= 1
            
            while current_row != total_rows or warehouse[current_row][current_column] != 0 or current_row != next_rows[current_column][i + 1]:
                if warehouse[current_row][current_column + 1] == 1:
                    next_rows[current_column + 1].append(current_row)
                    total_paths += 1

                current_row += 1

                if current_row == next_rows[current_column][i + 1]:
                    total_paths += 1
        
        current_column += 1
    
    return total_paths # % (pow(10, 9) + 7)

print(numPaths([[0,0,0],[0,1,0],[0,0,0]]))
