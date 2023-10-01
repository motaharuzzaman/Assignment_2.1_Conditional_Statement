#Assignment on Conditional Statement
'''
1. Leap Year Checker: Write a Python program that takes a year as input and
determines if it is a leap year or not.
'''

year=int(input('Enter a year : '))
if year%4==0 and year%100!=0:
    print(year, 'is a leap year')
elif year%400==0:
    print(year, "is a leap year")
else:
    print(year, 'is not a leap year')


'''
2. Grades Classification: Write a Python program that takes a student’s percentage as
input and prints their corresponding grade according to the following criteria:
– 90% or above: A+
– 80-89%: A
– 70-79%: B
– 60-69%: C
– Below 60%: Fail
'''

score= int(input('Enter a score of the Exam out of 100: '))
if score >=90 and score <=100:
    print('The result is A+.')
elif score >=80 and score <90:
    print('The result is A.')
elif score >=70 and score <80:
    print('The result is B.')
elif score >=60 and score <70:
    print('The result is C.')
elif score >100:
    print('The input is invalid.')
else:
    print('The result is Fail.')

'''
3. Vowel or Consonant: Write a Python program that takes a single character as input
and determines whether it is a vowel or a consonant.
'''
vowel='AEIOUaeiou'
letter = input('Enter a letter: ')
if letter in vowel:
    print(letter, 'is a vowel.')
else:
    print(letter, 'is a consonant.')

'''
4. Triangle Type Checker: Write a Python program that takes three sides of a triangle
as input and determines whether it forms an equilateral, isosceles, or scalene triangle.
'''
a=int(input('Enter the length of the 1st side of the Triangle, a= : '))
b=int(input('Enter the length of the 2nd side of the Triangle, b= : '))
c=int(input('Enter the length of the 3rd side of the Triangle, c= : '))
if a==b==c:
    print('It is an Equilateral Triangle.')
elif a==b or b==c or c==a:
    print('It is an Isosceles Triangle')
else:
    print('It is a Scalene Triangle.')

'''
5. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b,
c) of a quadratic equation as input and calculates and prints the real roots (if they exist)
or a message indicating the complex roots.
'''
#A Quadratic Equation is : ax^2 + bx + c = 0

a=int(input('Enter a value of a: '))
b=int(input('Enter a value of b: '))
c=int(input('Enter a value of c: '))
discriminant = b**2-4*a*c
if discriminant < 0:
    print('The equation has complex roots.')
elif discriminant == 0:
    x1 = -b/(2*a)
    x2 = x1
    print("The roots of the equation are: ",x1, "and",x2)
else:
    x1 = (-b+(b**2-4*a*c)**.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**.5)/(2*a)
    print("The roots of the equation are: ",x1, "and",x2)