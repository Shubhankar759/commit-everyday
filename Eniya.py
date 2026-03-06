"""
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1293
"""


def multi(*args):
    if (args[0]>1 and args[0]<100 
        and args[1]>1 and args[1]<100 
        and args[2]>1 and args[2]<100):

        return 2*(args[0]*args[1]*args[2])
    else:
        return None

    

with open('input.txt', 'r') as file:
    line = file.read()

print(multi(*list(map(int, line.split()))))