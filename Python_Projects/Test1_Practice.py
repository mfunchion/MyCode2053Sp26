def not_string(str):
    start = str[:3]
    if start == 'not':
        return str
    else:
        str = 'not' + str
        return str
    
string = 'python'
new = not_string(string)
print(new)

def swap(lst):
    min_index = lst.index(min(lst))
    tmp = lst[0]
    lst[0] = lst[min_index]
    lst[min_index] = tmp
    return lst

list = [5,2,3,4,1]
print(list)
new = swap(list)
print(new)

print(max(list))

def count_spaces(string):
    return sum(1 for c in string if c == " ")

str = 'the cow jumped over the moon '
total = count_spaces(str)
print(total)

def sum67(nums):
    count = 1
    sum = 0
    for i in nums:
        if i == 6:
            count = 0
        while count == 1:
            sum += i
            break
        if i == 7:
            count = 1
    return sum

numbers = [1,2,2,6,99,99,7]
print(sum67(numbers))