#sheet 7 lab1
print('"sheet7 lab 1"')


A = False
B = True

expression1 = not A and B or B
expression2 = A or A and B
expression3 = not (A and B or A)

false_expressions = []

if expression1 is False:
    false_expressions.append("not A and B or B")
if expression2 is False:
    false_expressions.append("A or A and B")
if expression3 is False:
    false_expressions.append("not (A and B or A)")

if not false_expressions:
    result = "All of the above"
else:
    result = ", ".join(false_expressions)

print(f"The false expression(s) is/are: {result}")

print("----------------------------------------------------")
#sheet 7 lab 2
print('"sheet7 lab 2"')
import math
print(math.trunc(1.5) - 15%3)

print("----------------------------------------------------")

#sheer 7 lab 3
print('"sheet7 lab 3"')
Q=5
T=2
if (Q>T or  Q>8) and (T<=4):
   R=Q*T

if (T==0 or  Q==2 or  Q>T) and (T>-5):
  R=4
print(R)

print("----------------------------------------------------")
print('"sheet7 lab 4"')
B=60
C=30
if (B/C) >=2:
 C=3
elif (B/C) ==2:
 C=11
print("The value of C after the code execution is:", C)
print("----------------------------------------------------")
print('"sheet7 lab 5"')
print("the correct answeer is while loop")
print("----------------------------------------------------")
print('"sheet7 lab 6"')
print("the correct answer is for i in range(21,31): and o	for i in range(11,1,-1):")
print("----------------------------------------------------")
print('"sheet7 lab 7"')
print('"the correct answer is 	while 1: and for i in x:  x.append(1)  and	while -3:  "')
print("----------------------------------------------------")
print('"sheet7 lab 8"')
i = 1
for x in range( 1,4) :
     i = i * x
     print('%d' %x)



