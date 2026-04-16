#Matthew Funchion

#finds the sum of the list of numbers
def function_1(num):
    sum = 0
    for i in num:
        sum += i
    return sum
    
#finds the mean of three numbers
def function_2(num1, num2, num3):
    answer = 0
    '''Adds the three parameters up and 
    usses floor divsion to find the mean'''
    answer = num1 + num2 + num3
    answer //= 3
    return answer

numbers_1 = [1,2,3,4,5]
sum_1 = function_1(numbers_1)
print(sum_1)
numbers_2 = [2,4,6,8,10]
sum_2 = function_1(numbers_2)
print(sum_2)
numbers_3 = [10,20,30,40,50]
sum_3 = function_1(numbers_3)
print(sum_3)

x1 = 10
y1 = 5
z1 = 18
mean_1 = function_2(x1,y1,z1)
print(mean_1)
x2 = 1
y2 = 2
z2 = 3
mean_2 = function_2(x2,y2,z2)
print(mean_2)
x3 = 80
y3 = 20
z3 = 50
mean_3 = function_2(x3,y3,z3)
print(mean_3)

