import os

f = open('input04.txt', 'r')
data = f.read()

find_word = 'XMAS'

def find_word_horizontally(data, find_word):
    lines = data.split('\n')
    number_finds = 0
    for line in lines:
        if find_word in line:
            number_finds += 1
    return number_finds

def find_word_vertically(data, find_word):
    lines = data.split('\n')
    number_finds = 0

    for i in range(len(lines[0])):
        column = ''.join([line[i] for line in lines])
        if find_word in column:
            number_finds += 1
    return number_finds

def find_word_diagonally(data, find_word):
    number_finds = 0
    lines = data.split('\n')
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + len(find_word) <= len(lines) and j + len(find_word) <= len(lines[i]):
                diagonal = ''.join([lines[i + k][j + k] for k in range(len(find_word))])
                if find_word in diagonal:
                    number_finds += 1
    return number_finds

def find_word_diagonally_reverse(data, find_word):
    number_finds = 0
    lines = data.split('\n')[::-1]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + len(find_word) <= len(lines) and j + len(find_word) <= len(lines[i]):
                diagonal = ''.join([lines[i + k][j + k] for k in range(len(find_word))])
                if find_word in diagonal:
                    number_finds += 1
    return number_finds

def find_word_in_grid(data, find_word):
    horizontal = find_word_horizontally(data, find_word) + find_word_horizontally(data, find_word[::-1])
    vertical = find_word_vertically(data, find_word) + find_word_vertically(data, find_word[::-1])
    diagonal = find_word_diagonally(data, find_word) + find_word_diagonally(data, find_word[::-1])
    diagonal_reversed = find_word_diagonally_reverse(data, find_word) + find_word_diagonally_reverse(data, find_word[::-1])

    return horizontal + vertical + diagonal + diagonal_reversed

def main():
    result = find_word_in_grid(data, find_word)
    print(f"Result: {result}")
    f.close()
    # Clean up the input file


if __name__ == "__main__":
    main()

