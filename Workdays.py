'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1264
'''

with open('input.txt', 'r') as file:
    line = file.read()

input = list(map(int,line.split()))


print(f"{input[0]*(input[1]+1)}")