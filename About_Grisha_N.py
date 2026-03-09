'''
Problem Statment 
https://acm.timus.ru/problem.aspx?space=1&num=2012
'''

with open('input.txt', 'r') as file:
    line = file.read()


f = int(line)

if (12-f)*45 < 240:
    print("YES")
else:
    print("NO")