#Write a program that accepts a sequence of whitespace separated words as input 
#and prints the words after removing all duplicate words and sorting them alphanumerically.

#Suppose the following input is supplied to the program:

#hello world and practice makes perfect and hello world again
#Then, the output should be:

#again and hello makes perfect practice world
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a 
#console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.

imp = input().split()
[imp.remove(i) for i in imp if imp.count(i) > 1]
imp.sort()
print(" ".join(imp))

#OR

imp = sorted(list(set(input().split())))
print(" ".join(imp))

#OR

imp = input().split()
out = []
for i in imp:
    if i not in out:
        out.append(i)
print(" ".join(sorted(out)))


#Write a program which accepts a sequence of comma separated 4 digit binary 
#numbers as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#Example:

#0100,0011,1010,1001
#Then the output should be:

#1010
#Notes: Assume the data is input by console.

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

inp = input().split(",")
inp = [i for i in inp if int(i,2)%5 == 0]
print(",".join(inp))

#OR

def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked 
                                #from 'data' if found True by 'check' function
print(",".join(data))


#Write a program, which will find all such numbers between 1000 and 3000 (both included) 
#such that each digit of the number is an even number.The numbers obtained should be printed 
#in a comma-separated sequence on a single line.

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

def checker(x, y):
    lst_numbers = []
    for n in range(x, y+1): 
        flag = 1
        for d in str(n):  
            if ord(d)%2 != 0:
                flag = 0
        if flag == 1:
            lst_numbers.append(str(n))
    return lst_numbers

numbers = []
numbers = checker(1000,3000)
print(",".join(numbers))

#OR
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))

#OR

lst = [str(i) for i in range(1000,3001)] 
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))


#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:

#hello world! 123
#Then, the output should be:

#LETTERS 10
#DIGITS 3
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a 
#console input.

entry = str(input().replace(" ",""))
num_count,letter_count = 0,0
for i in entry:
    if i.isnumeric():
        num_count += 1
    elif i.isalpha():
        letter_count += 1

print("LETTERS " + str(letter_count))
print("DIGITS " + str(num_count))


