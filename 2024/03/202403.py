
import os
import re


def calculate_multiplications(text):
    regex = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",text)
    return regex

def open_file(filename_param):

    dirname = os.path.dirname(__file__) # get the directory of the current file
    filename = os.path.join(dirname, filename_param) # join the directory with the input file 
    print('filename: ', filename)
    try:
        with open(filename, 'r') as file:
            input = file.read() # read the file and split it by lines
            return input
    except FileNotFoundError:
        print('File not found')

def get_mul_result(mul):
    mul = mul[4:-1]
    mul = mul.split(',')
    return int(mul[0]) * int(mul[1])

if (__name__ == '__main__'):
    val = 0
    data = open_file('input03.txt')
    mul_list = calculate_multiplications(data)
    for mul in mul_list:
        val += get_mul_result(mul)
    print(val)
