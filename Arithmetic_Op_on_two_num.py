# Accept Two Numbers
 
num1 = input(" Enter the First Number(bigger): ")
num2 = input(" Enter the second number(smaller): ")

# Add. of two numbers
Sum = float(num1) + float(num2) 

# Subtract. of two numbers
dif = float(num1) - float(num2)

# Multiplication of two numbers
Mul = float(num1) * float(num2)

# Division. of two numbers
div = float(num1) / float(num2)

# Mod. of two numbers
mod = float(num1) % float(num2)

# Power a^b. two numbers
power = pow(int(num1),int(num2))

print('The sum is {0}'.format(Sum))
print('The difference is {0}'.format(dif))
print('The Multiplication is {0}'.format(Mul))
print('The Quotient is {0}'.format(div))
print('The Remainder is {0}'.format(mod))
print('The answer for a^b is {0}'.format(power))
