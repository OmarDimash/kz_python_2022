"""
FOR LOOP:

Цикл for используется для перебора последовательности (то есть списка, кортежа, словаря, набора или строки).

Это меньше похоже на ключевое слово for в других языках программирования и работает больше как метод итератора, который можно найти в других объектно-ориентированных языках программирования.

С помощью цикла for мы можем выполнить набор операторов, один раз для каждого элемента в списке, кортеже, наборе и т. д.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
"""
Перебор строки
Даже строки являются итерируемыми объектами, они содержат последовательность символов:
"""

for x in "banana":
  print(x)

"""
Заявление о перерыве
С помощью оператора break мы можем остановить цикл до того, как он просмотрит все элементы:
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

"""
Заявление о продолжении
С помощью оператора continue мы можем остановить текущую итерацию цикла и продолжить следующую:
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
"""
Функция диапазона()
Чтобы перебрать набор кода заданное количество раз, мы можем использовать функцию range(). Функция range() возвращает последовательность чисел, начиная с 0 по умолчанию, увеличиваясь на 1 (по умолчанию) и заканчивая указанным числом.
"""

for x in range(6):
  print(x)
 
#Обратите внимание, что range(6) — это не значения от 0 до 6, а значения от 0 до 5.
#Функция range() по умолчанию равна 0 в качестве начального значения, однако можно указать начальное значение, добавив параметр: range(2, 6), что означает значения от 2 до 6 (но не включая 6):
 
for x in range(2, 6):
  print(x)

#Функция range() по умолчанию увеличивает последовательность на 1, однако можно указать значение приращения, добавив третий параметр: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)
  
"""Еще в цикле For
Ключевое слово else в цикле for определяет блок кода, который будет выполнен после завершения цикла:"""

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
#Примечание. Блок else НЕ будет выполняться, если цикл остановлен оператором break.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

"""
Вложенные циклы
Вложенный цикл — это цикл внутри цикла.

«Внутренний цикл» будет выполняться один раз для каждой итерации «внешнего цикла»:
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

