#A function that multiplies a set of numbers

def product(*numbers):
    product = 0
    for num in numbers:
        product += num
    return product

answer = product(32,3,4,8,22,2.1,7,89)
print(answer)