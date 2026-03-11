'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1877
'''

with open('input.txt', 'r') as file:
    line = file.read()

lock_password =list(map(int,line.split()))

if(lock_password[0]%2==0 and lock_password[1]%2!=0):
    print('yes')
else:
    print('no')