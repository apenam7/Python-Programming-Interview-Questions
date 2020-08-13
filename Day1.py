#Write a program which will find all such numbers which are divisible by 
#7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a 
#single line.

#Ariel

print(*(n for n in range(2000,3201) if n%7 == 0 and n%5!=0), sep = ',')


#Rob
emp = []
num = range(2000,3200)
for i in num:
    if i%7 ==0 and i%5 !=0:
        emp.append(i)
print(emp)

#Write a program which can compute the factorial of a given numbers.The results should be printed 
#in a comma-separated sequence on a single line.Suppose the following input is supplied to the 
#program: 8 Then, the output should be:40320

print("enter a number:")
fact = int(input())
def factorial (fact) : return 1 if fact <=1 else fact*factorial(fact-1)
resutl = factorial(fact)
print(resutl)


#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
#such that is an integral number between 1 and n (both included). and then the program should print 
#the dictionary.Suppose the following input is supplied to the program: 8

#Then, the output should be:

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}    

n = int(input("Enter an integer number: "))
dic = {x : x*x for x in range(n+1)}
print(dic)
#OR
n = int(input("Enter an integer number: "))
dic = dict(list(enumerate(x*x for x in range(n+1))))
print(dic)



