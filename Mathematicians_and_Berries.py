'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=2001
'''

with open('input.txt', 'r') as file:
    line = file.read()

reading =list(map(int,line.split()))


print(f"{reading[5]-reading[1]} {reading[2]-reading[0]}")