
a = 5 
b = 67 
if a > b:
    print("a больше")
elif b > a:
    print("b больше")


x = -4
if x > 0: 
    print("положительный")
elif x < 0:
    print("отрицательный")


y = -4 
print(y*-1)
print(abs(y))

num1 = 23
num2 = 23
if num1 == num2:
    print("No")
else:
    print("Yes")



z = 86
if z > 100 or z < -100:
    print("-")
else:
    print("+")

sezon = 11
if sezon in (9,10,11):
    print("осень")
elif sezon in (12,1,2):
    print("зима")
elif sezon in (3,4,5):
    print("весна")
elif sezon in (6,7,8):
    print("лето")



n1 = 21
n2 = 43
n3 = 9
if n1 > 10 and n2 > 10 and n3 > 10:
    print("Yes")
else:
    print("No")


a = 23
b = 43
c = -4

count = 0

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print("Количество положительных чисел:", count)




years = 2
months = 6


total_months = years * 12 + months

total_days = total_months * 29


print(f"Общее количество дней: {total_days}")





a = 345
first_num = a
if first_num % 3 == 0 and first_num % 5 == 0:
    print("siuuu")
elif first_num % 3 == 0:
    print("ay ay ay")
elif first_num % 5 == 0:
    print("MOney")