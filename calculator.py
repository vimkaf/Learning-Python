#this file is used in module.py
def calculate(action='',*numbers):
    answer = 0
    x = 1
    if action is 'add':
        for num in numbers:
            answer +=num
    elif action is 'sub':
        for num in numbers:
            x -=num
    elif action is 'mul':
        for num in numbers:
            x *=num
        answer = x
    elif action is 'div':
        for num in numbers:
            x /= num
        answer = num    
        

    return answer


