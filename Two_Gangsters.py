'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1409
'''


with open('input.txt', 'r') as file:
    line = file.read()

cans_shot = list(map(int,line.split()))
total_cans = sum(cans_shot)-1

print(f"{total_cans-cans_shot[0]} {total_cans-cans_shot[1]}")

