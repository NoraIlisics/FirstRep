#Write a program which sums the integers from 1 to 10 using a for loop 
# (and prints the total at the end).

total = 0
for i in range(1,11):
    total += i

print(total)

#Can you think of a way to do this without using a loop?

total2 = sum(range(1,11))
print(total2)

#Write a program which finds the factorial of a given number.
#  E.g. 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is equal to 5 x 4 x 3 x 2 x 1, etc.. 
# Your program should only contain a single loop.

number = int(input("Choose a number: "))
num_fact = 1

for i in range(1, number+1):
    num_fact *= i 
print(num_fact)

#Write a program which prompts the user for 10 floating-point numbers and calculates their sum,
#  product and average. Your program should only contain a single loop.
#Rewrite the previous program so that it has two loops 
# – one which collects and stores the numbers, and one which processes them.