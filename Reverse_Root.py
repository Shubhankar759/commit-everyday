'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1001
'''

with open('input.txt', 'r') as file:
    line = file.read()

line = line.split()

square_roots = []
for i in line:
    square_roots.append(round(int(i)**0.5,4))

print(square_roots)