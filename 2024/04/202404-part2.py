
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
        ['M', 'S', 'S', 'M'],
        ['S', 'M', 'S', 'M'],
        ['S', 'M', 'M', 'S'],
        ['M', 'S', 'M', 'S']
    ]
    count = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if( grid[i][j] == 'A' and [grid[i-1][j-1], grid[i+1][j+1], grid[i+1][j-1], grid[i-1][j+1]] in patterns):
                count += 1 
            
    return count

if __name__ == "__main__":
    my_data = get_list()
    print(f"resut is: ", find_it(my_data))
