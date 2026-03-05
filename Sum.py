'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1068&locale=en
'''


with open('input.txt', 'r') as file:
    line = file.read()

line = int(line)
result = 0

if(line==0 or line==1):
    result=line
elif(line>0):
    result = (line*(line+1))//2
elif(line<0):
    result = (abs(line)*abs(line))//-2

print(result)