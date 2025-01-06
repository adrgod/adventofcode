
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

def pair_is_valid(dir, a, b):
    if a == None or b == None:
        return True
    if dir == 1:
        if b > a and b <= a +3:
            return True
        else:
            return False
    elif dir == 0:
        if b < a and b >= a - 3:
            return True
        else:
            return False
    else:
        return False
    
def get_direction(report):

    diff = [report[i+1] - report[i] for i in range(len(report)-1)]
    pos_diff = [ i > 0 for i in diff]
    neg_diff = [ i < 0 for i in diff]

    re = sum(pos_diff) - sum(neg_diff)

    if re > 0:
        return 1
    elif re == 0:
        return None
    elif re < 0:
        return 0
    

def number_of_errors_in_report(report):

    num_safe = 0
    previous_level = None
    three_levels_behind = None
    direction = None
    num_errors = 0
    for level in report:
        if previous_level == None:
            previous_level = int(level)
            continue
        else:
            direction = get_direction(report)
            if pair_is_valid(direction, previous_level, level):
                num_safe += 1
                three_levels_behind = previous_level
                previous_level = level
            else:
                if pair_is_valid(direction, three_levels_behind, level):
                    if num_errors == 0:
                        num_safe += 1
                        num_errors += 1
                    else:
                        num_errors += 1
                    three_levels_behind = previous_level
                    previous_level = level
                else:
                    num_errors += 1
    return num_errors


def report_is_safe(report):
    
    n_errors = number_of_errors_in_report(report)
    if n_errors <= 1:
        return True

def calc_safe_reports(list_of_reports):
    safe_reports = 0
    for report in list_of_reports:
        if report_is_safe(report):
            safe_reports += 1
    return safe_reports

if(__name__ == '__main__'):
    reports = open_file('data\\input.txt')

    result = calc_safe_reports(clean_data(reports))

    print(result)
    
    

            

