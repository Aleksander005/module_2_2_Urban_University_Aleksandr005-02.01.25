# Все ли равны?
print('''Вам предлагается ввсести числа для сравнения:
     -если все числа равны между собой, то программа выведет цифру 3; 
     -если хотя бы 2 из 3 введённых чисел равны между собой, то программа выведет цифру 2;
     -если равных чисел среди 3-х вообще нет, то программа выведет 0.''')
first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third and second == third: print( "Ваш результат 3") # все равны между собой
elif first == second or first == third or second == third: print("Ваш результат 2") # равны 2
else: print("Ваш результат 0") # С ПРОБЕОЛОМ ОДТНАКОВЫЕ ЦИФРЫ не ВЫДАЕТ "3" !!!!!!! 