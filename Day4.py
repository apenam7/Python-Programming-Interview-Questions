#Write a program that accepts a sentence and calculate the number of upper 
#case letters and lower case letters.

#Suppose the following input is supplied to the program:

#Hello world!
#Then, the output should be:

#UPPER CASE 1
#LOWER CASE 9
#Hints:
#In case of input data being supplied to the question, it should be assumed 
#to be a console input.

entry = input()
upper, lower = 0,0
for i in entry:
    if i.isalpha() and i.isupper():
        upper +=1
    elif i.isalpha() and i.islower():
        lower += 1

print("UPPER CASE ", upper)
print("LOWER CASE " + str(lower))

#OR

entry = input()
upper, lower = 0,0
for i in entry:
    upper += i.isupper()
    lower += i.islower()

print("UPPER CASE ", upper)
print("LOWER CASE " + str(lower))

#OR
entry = input()
upper = sum(1 for i in entry if i.isupper())
lower = sum(1 for i in entry if i.islower())

print("UPPER CASE ", upper)
print("LOWER CASE " + str(lower))


#Write a program that computes the value of a+aa+aaa+aaaa with a 
#given digit as the value of a.

#Suppose the following input is supplied to the program:

#9
#Then, the output should be:

#11106
#Hints:
#In case of input data being supplied to the question, it 
#should be assumed to be a console input.

a = input()
print(int(a) + int(2*a) + int(3*a) + int(4*a))

#OR

a = input()
print(sum(int(i*a) for i in range(1,5)))