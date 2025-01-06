
import os

def open_file(filename_param):

    dirname = os.path.dirname(__file__) # get the directory of the current file
    filename = os.path.join(dirname, filename_param) # join the directory with the input file 

    try:
        with open(filename, 'r') as file:
            input = file.read().splitlines() # read the file and split it by lines
            return input
    except FileNotFoundError:
        print('File not found')

def clean_data(data):
    for i in range(len(data)):
        data[i] = list(map(int, data[i].split()))
    return data

def calc_safe_reports(reports):
    
    report_safe = 0

    for list_of_levels in reports:
        num_safe = 0
        previous_level = -1
        two_levels_before = -1
        direction = -1

        for level in list_of_levels:
            if previous_level < 0:
                previous_level = int(level)
                num_safe += 1
                continue
            else:
                if int(level) > int(previous_level) and int(level) <= int(previous_level) + 3:
                    if direction == -1:
                        direction = 1
                    if direction == 1:
                        num_safe += 1
                        two_levels_before = previous_level
                        previous_level = int(level)
                elif int(level) > int(two_levels_before) and int(level) <= int(two_levels_before) + 3:
                    if direction == -1:
                        direction = 1
                    if direction == 1:
                        num_safe += 1
                        two_levels_before = previous_level
                        previous_level = int(level)
                elif int(level) < int(previous_level) and int(level) >= int(previous_level) - 3:
                    if direction == -1:
                        direction = 0
                    if direction == 0:
                        num_safe += 1
                        two_levels_before = previous_level
                        previous_level = int(level)
                elif int(level) < int(two_levels_before) and int(level) >= int(two_levels_before) - 3:
                    if direction == -1:
                        direction = 0
                    if direction == 0:
                        num_safe += 1
                        two_levels_before = previous_level
                        previous_level = int(level)
                else:
                    two_levels_before = previous_level
                    previous_level = int(level)
        if num_safe == len(list_of_levels):
            report_safe += 1
    return report_safe



if(__name__ == '__main__'):
    reports = open_file('data\\input.txt')

    result = calc_safe_reports(clean_data(reports))

    print(result)
    
    

            

