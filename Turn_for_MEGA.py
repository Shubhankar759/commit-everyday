'''
Problem Statment
https://acm.timus.ru/problem.aspx?space=1&num=1787
'''

with open('input.txt', 'r') as file:
    line = file.read()

traffic_details = list(map(int,line.split()))
sum =0
for i in range(2,len(traffic_details)):

    if(traffic_details[0]<traffic_details[i]):
        sum += traffic_details[i]-traffic_details[0] 
    else:
        sum = 0 

print(sum)
