# Новая тема 
# тернарный оператор
# генератор списков
m = 5
if m >= 0:
    print("положительное")
else:
    print("отрицательное")
#№№№№№№№№№№№№№№№№№№№№№№№№№
print('положительное' if  m>= 0 else 'отрицательное')
##############################
age= 20
if age >= 18:
    status= "взрослый"
else:
    status = "несовершеннолетний"
##############################
status= "взрослый" if age >= 18 else "несовершеннолетний"
print(status)
##############################
def grade(score):
    return "отлично" if score >= 90 else "хорошо" if score >= 75 else "удовлетворительно" if score >= 60 else "двойка"
print(grade(85))
##############################
numbers = [-2, -1, 0, 1, 2]
sin = ['положительное' if n>0 else 'отрицательное' if n<0 else 'ноль' for n in numbers]
print(sin)
##############################
temeperatures_c = -5
print(f"на улице {'тепло' if temeperatures_c > 0 else 'холодно'}")
# Генератор списков
numbers = [i for i in range(1,100)]
print(numbers)
##############
numbers2 =[]
for i in range(1,100):
    numbers2.append(i)
print(numbers2)
##############
num_chet = [i for i in range(1,100) if i % 2 == 0]
print(num_chet)
##############
num_sp = [i**2 for i in range(1,7)]
print(num_sp)
##############
sing = ['положительное' if x > 0 else 'отрицательное' if x < 0 else 'ноль' for x in [-2, -1, 0, 1, 2]]
x in [[-2, -1, 0, 1, 2]]
print(sing)
##################
words = ['python', 'django', 'ai']
lengths = [len(word) for word in words]
print(lengths) 
    