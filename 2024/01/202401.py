
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'list1.txt'), 'r') as file1:
    data1 = csv.reader(file1)

print(data1)