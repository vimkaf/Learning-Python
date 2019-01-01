'''
Exercise 2: Given 2D array calculate the sum of diagonal elements.

Ex: [[1,3,5],[1,4,6],[7,6,9] => sum of 1 + 4 + 9 => 14

'''

sample = [[2,0],[0,2]]
#sample = [[1,3,5],[1,4,6],[7,6,9]]
iterator = sum = 0
for x in sample:
    for y in x:
        sum += x[iterator]
        iterator += 1
        break
# OR         
def sum_of_diagonal(a):
 
    sum = 0
 
    for i in range(len(a)):
 
        sum += a[i][i]
 
    return sum
print(sum)

print(sum_of_diagonal(sample))


