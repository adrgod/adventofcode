
my_data = []
filename = "input04.txt"

def get_list():
    try:
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f]
    except FileNotFoundError:
        print("File not found. Please check the file path.")

def find_it(grid):
    rows = len(grid)
    cols = len(grid[0])
    patterns = [
        ['M', 'M', 'S', 'S'],
        ['S', 'M', 'M', 'S'],
        ['S', 'S', 'M', 'M'],
        ['M', 'S', 'S', 'M'],
        ['M', 'S', 'M', 'S'],
        ['S', 'M', 'S', 'M']
    ]
    count = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            print(f"for point: {grid[i][j]}, left-up: {grid[i-1][j-1]}, right-down: {grid[i+1][j+1]}, left-down: {grid[i-1][j-1]}, right-up: {grid[i+1][j-1]}")
            if( grid[i][j] == 'A' and [grid[i-1][j-1], grid[i+1][j+1], grid[i-1][j+1], grid[i+1][j-1]] in patterns):
                count += 1
            # Check all patterns
            
    return count

if __name__ == "__main__":
    my_data = get_list()
    #print("My data is: ",my_data)
    print(f"resut is: ", find_it(my_data))


""" M M
 A
S S

S M
 A
S M

S S
 A
M M

M S
 A
M S """
