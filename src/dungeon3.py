'''
Created on Nov. 22, 2023
Framework for an Adventure Game. Now with the ability to move
@author: Sebastian
'''

MAP_FILE = "cave_map.txt"

def load_map(map_file) :
    """
    Loads a map from a file as a grid (list of lists)
    eg.
    S*-
    ***
    --F would return [["S","*","-"],["*","*","*"],["-","-","F"]]
    """
    map = []
    file = open(map_file, "r")
    file = file.readlines()
    
    for line in file :
        line = line.strip() #removes newline character
        row = []
        for i in range(len(line)) :
            row.append(line[i])
        map.append(row)
    return map

def find_start(grid) :
    """
    Finds the starting position of the player on the map.
    eg. 
    [["S","*","-"],["*","*","*"],["-","-","F"]] would return [0,0]
    """
    for row in range(len(grid)) : #first to last row of map
        for col in range(len(grid[row])): #first to last  col in the row
            if grid[row][col] == "S": #only one Start
                return [row,col]

def get_command() :
    """
    Gets a command from the user.
    eg.
    aaa would return aaa
    """
    user = input("") 
    return user
    
def display_map(grid, player_position):
    """
    Displays the map.
    eg. [["S","*","-"],["*","*","*"],["-","-","F"]]
    would return
    @*-
    ***
    --F on the first turn
    """
    playerRow = player_position[0]
    playerCol = player_position[1]
    for row in range(len(grid)) :
        for col in range(len(grid[row])):
            if playerRow == row and playerCol == col: #special case for the tile containing the player position
                print("@", end="")
            else: #every other row
                print(f"{grid[row][col]}", end="")
        print()#new line character

def get_grid_size(grid):
    """
    Returns the size of the grid.
    eg. 
    [["S","*","-"],["*","*","*"],["-","-","F"]]
    would return [3,3]
    """
    rows = len(grid)
    cols = len(grid[0])     
    return [rows,cols]

def is_inside_grid(grid, position) :
    """
    Checks if a given position is valid (inside the grid).
    eg. 
    for [["S","*","-"],["*","*","*"],["-","-","F"]]
    [3,1] would not be inside the grid
    """
    grid_rows, grid_cols = get_grid_size(grid)
    if grid_rows > position[0] and position[0] >= 0:
        if grid_cols > position[1] and position[1] >= 0:
            return True
    return False        

def look_around(grid, player_position) :
    """
    Returns the allowed directions.
    eg.
    [["S","*","-"],["*","@","*"],["-","-","F"]]
    would return ['north','east','west']
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and (grid[row - 1][col] in allowed_objects):
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and (grid[row + 1][col] in allowed_objects):
        directions.append('south')
    if is_inside_grid(grid, [row, col + 1]) and (grid[row][col + 1] in allowed_objects):
        directions.append('east')
    if is_inside_grid(grid, [row, col - 1]) and (grid[row][col - 1] in allowed_objects):
        directions.append('west')
    return directions

def print_directions(map, pos):
    """
    eg.
    [["S","*","-"],["*","@","*"],["-","-","F"]], [1,1]
    would print: You can go north, east, west
    """
    directions = look_around(map, pos)
    list =[]
    print(f"You can go ", end="")
    for direction in directions :
        list.append(direction)
    for i in range(len(list)) :
        if i == 0 :
            print(list[i], end="")
        elif i >= 1 :
            print(f", {list[i]}", end="")
    print()
    
def move(direction, player_position, grid) :
    """
    Moves the player in the given direction.
    eg. [["S","*","-"],["*","@","*"],["-","-","F"]]
    move('west', [1,1], map) would return True and change player position to [0,1]
    """
    if direction in look_around(grid, player_position) :
        if direction == "north" :
            player_position[0] = player_position[0]-1
        elif direction == "south" :
            player_position[0] = player_position[0]+1
        elif direction == "east" :
            player_position[1] = player_position[1]+1
        elif direction == "west" :
            player_position[1] = player_position[1]-1
        return True
    return False

    
def main():
    """
    Main entry point for the game.
    """
    stop = False
    map = load_map(MAP_FILE)
    start = find_start(map)
    player_position = start
    while not stop:
        print_directions(map,player_position)
        input = get_command()
        if input == "escape" :
            stop = True
        elif input == "show map" :
            display_map(map,player_position)
        elif input == "go north" or input == "go south" or \
              input == "go east" or input== "go west" :
            success = move(input[3:], player_position, map)
            if success:
                print(f"You moved {input[3:]}")
            else :
                print("There is no way there")
        else:
            print("I do not understand")

if __name__ == '__main__':
    main()
