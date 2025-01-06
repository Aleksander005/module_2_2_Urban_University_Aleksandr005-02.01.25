for i in range (11,1,-1):
    for j in range (5,1,-1): # таблица по убыванию
        print(f'{i} * {j} = {i*j}')
        print(i*j)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_numbers =[]
not_even_numbers= []
for i in range(len(numbers)):
    i=i+1
    if i == 0:
       continue
    if i % 2== 0:
        even_numbers.append(i)
    if i % 2 != 0:
        not_even_numbers.append(i)

print(even_numbers)
print(not_even_numbers)
# сумма чисел
s=0
for i in range (1,3): # сумма от 1 до 5 (1+2+3+4=5)
    s +=i
    for j in range (1,3):
        k= j*i
        print(k)

for i in range (10,0,-1): # квадрат чисел по убыванию
    print(i*i)

a=1
for k in range(5): a+=1
print(a)

n= int (input())
s=0
for i in range (n):
    x= int(input())
    s+=x
print(s)













