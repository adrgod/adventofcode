
import csv
import os
import sys

sys.setrecursionlimit(1100)

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

list1 = []
list2 = []

def add_top_pair(l1, l2):
    if l1 == [] and l2 == []:
        return 0
    return abs(int(l2.pop(0)) - int(l1.pop(0))) + add_top_pair(l1, l2)


def get_list(filename):
    with open(os.path.join(__location__, filename), 'r') as file1:
        data1 = csv.reader(file1)

        for row in data1:
            for elem in row:
                if elem != "":
                    list1.append(elem)
    list1.sort()
    return list1

list1 = get_list('list1.txt')
list2 = get_list('list2.txt')

print(len(list1))
print(list1)
#print(add_top_pair(list1, list2))




