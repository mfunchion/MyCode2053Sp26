
print("Hello World!")

# one line

'''
block of comments
can span multiple lines
'''

x = 10
y = 1
z = 2
#ctrl forward slash to comment out highlighted code

x = "hello" #do not have to declare data type and can change it without error

x = 100//10
print(x)
y = 1.5
x = int(y)

min_val = min(1,3)
min_val = min([4,5,6,7])
r = 2**4 #to the power of 4 using two *
r = pow(2,4)
print(r)

#syntax for if statement
if x > 10:
    x = 5
    y = 100

if x>10 and y<5:
    x=0
    y=100

if x>10 or y<5:
    x=0
    y=100

if x>10:
    print("x")
elif y>20:
    print('y')
else:
    print("neither")

#for loops
for i in range(5):
    print(i)

lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(i, lst[i])

#starts at one rather than zero
for i in range(1,len(lst)):
    print(i, lst[i])

#starts at one and incriments by 2
for i in range(1,len(lst),2):
    print(i, lst[i])

#goes backwards through the list
for i in range(len(lst)-1,-1,-1):
    print(i, lst[i])

#faster than end but goes through the entire list
for i, val in enumerate(lst):
    print(i,val)

for value in lst:
    print(value)

count=0
while count<10:
    print(count)
    count += 1
#python does not have i++ or ++i


#in class exercise 1
for i in range(1,20):
    if i%3 == 0:
        print(i)

#in class exercise 2
sum = 0
for i in range(2,51,2):
    sum += i
print(sum)

#in class exercise 3
numbers=[5,8,2,15,10,3,7]
for i in numbers:
    if i>5:
        print(i,end=" ")

#take a look at the challenge. Will probably be on the exam


def hello():
    print("Hello World!")
hello()

def greeting(name="buddy"):
    print("Hello", name)
greeting("Bob")
greeting()

def swap(lst):
    tmp = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = tmp
lst=[0,3,8,4,5]
swap(lst)
print(lst)

'''
- can use double or single quotes to declare a string
- string concatenation allows for two or more strings to be joined together using a +
- Each character in a string has an index palce
    -same as an array 
        - title[5]
    -can use a negative to refer to the last character in a string
        - title[-1] or title[-3] (3 characters from the end)
    -can determine length using len()
    -can use * to produce multiple copies of a string 
        - 'Python' * 7
    -can compare strings using "==" and "!="
    -in and not in allow for detecting a substring

    email = "bob@gamil.com
    each letter has an index
    str[start:end]
    domain=email[4:13] can use [4:] if want to go through end of string
    username=email[0:3] can use [:3] if start is zerp
'''  
demo="Bob's email address is"
email="bob@gmail.com"
my_string=demo+" "+email
print(my_string)

for c in demo:
    print(c)
last_char=email[-1]
print(last_char)

#need for the hw
if "gmail" in email:
    print("has an gamil address")

#string slicing
domain=email[4:]
print(domain)
