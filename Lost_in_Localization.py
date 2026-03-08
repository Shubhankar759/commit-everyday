'''
Problem Statment 
https://acm.timus.ru/problem.aspx?space=1&num=1785
'''

with open('input.txt', 'r') as file:
    line = file.read()

def Anindilyakwa(numbers):
    match numbers:
        case num if 1 <= num <=  4:
            return "few"
        case num if 5 <= num <= 9:
            return "several"
        case num if 10 <= num <= 19:
            return "pack"
        case num if 20 <= num <=  49:
            return "lots"
        case num if 50 <= num <=  99:
            return "horde"   
        case num if 100 <= num <= 249:
            return "throng"
        case num if 250 <= num <=499:
            return "swarm"
        case num if 500 <= num <= 999:
            return "zounds"
        case num if 1000<= num:
            return "legion"

        case _:
            return "Invalid"
        
print(Anindilyakwa(int(line)))