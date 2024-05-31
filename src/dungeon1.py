'''
Created on Nov. 22, 2023
Framework for an Adventure Game. Map loading and start locating
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
    aaa would return false
    """
    user = input("").lower() 
    return user


def main():
    """
    Main entry point for the game.
    """
    map = load_map(MAP_FILE)
    print(map)
    start = find_start(map)
    print(f"Starting position: {start}")
    while not get_command() == "escape" :
        print("I do not understand")

if __name__ == '__main__':
    main()
