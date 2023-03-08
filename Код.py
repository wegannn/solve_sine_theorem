import math #Импортируем модуль math для использования математических функций

def solve_sine_theorem(angle1, angle2, angle3, side1, side2, side3, unknown):#Определяем функцию для решения теоремы синусовс помощью заданных углов и сторон треугольника, а также неизвестного параметра (угла или стороны)
    # Если неизвестный параметр - угол
    if unknown == "angle":  # Если неизвестен угол 1
        if angle1 is None:# Решаем угол 1 с помощью теоремы синусов
            angle1 = math.degrees(math.asin((math.sin(math.radians(angle2)) * side1) / side2)) # Возвращаем найденный угол
            return angle1
        elif angle2 is None: # Если неизвестен угол 2
            angle2 = math.degrees(math.asin((math.sin(math.radians(angle1)) * side2) / side1))  # Решаем угол 2 с помощью теоремы синусов
            return angle2 # Возвращаем найденный угол
        elif angle3 is None:
            angle3 = math.degrees(math.asin((math.sin(math.radians(angle1)) * side3) / side1))
            return angle3
        else:
            return "Ошибка: Известны три угла. Не удается решить для неизвестного угла."# Если известны все три угла, не можем решить для неизвестного угла, возвращаем ошибку
    elif unknown == "side": # Если неизвестный параметр - сторона
        if side1 is None:    # Если неизвестна сторона 1
            side1 = (math.sin(math.radians(angle1)) * side2) / math.sin(math.radians(angle2))        # Решаем сторону 1 с помощью теоремы синусов
            return side1         # Возвращаем найденную сторону
        elif side2 is None:    # Если неизвестна сторона 2
            side2 = (math.sin(math.radians(angle2)) * side1) / math.sin(math.radians(angle1))        # Решаем сторону 2 с помощью теоремы синусов
            return side2        # Возвращаем найденную сторону
        elif side3 is None:    # Если неизвестна сторона 3
            side3 = (math.sin(math.radians(angle3)) * side1) / math.sin(math.radians(angle1))        # Решаем сторону 3 с помощью теоремы синусов
            return side3        # Возвращаем найденную сторону
        else:# Если известны все три угла, не можем решить для неизвестного угла, возвращаем ошибку
            return "Ошибка: Известны три стороны. Не удается решить для неизвестной стороны"
    else:
        return "Ошибка: Неизвестный ввод для параметра 'unknown'."

#Вводим данные 
print("Введите углы и стороны треугольника (если значение неизвестно, введите 'None'):")
angle1 = input("Угол 1 (в градусах): ")
angle2 = input("Угол 2 (в градусах): ")
angle3 = input("Угол 3 (в градусах): ")
side1 = input("Сторона 1: ")
side2 = input("Сторона 2: ")
side3 = input("Сторона 3: ")
unknown = input("Что нужно найти (угол или сторону)? ")


#Если что-то неизвестно пишем None, известному приравниваем значение float
if angle1 == "None":
    angle1 = None
else:
    angle1 = float(angle1)

if angle2 == "None":
    angle2 = None
else:
    angle2 = float(angle2)

if angle3 == "None":
    angle3 = None
else:
    angle3 = float(angle3)

if side1 == "None":
    side1 = None
else:
    side1 = float(side1)

if side2 == "None":
    side2 = None
else:
    side2 = float(side2)

if side3 == "None":
    side3 = None
else:
    side3 = float(side3)


result = solve_sine_theorem(angle1, angle2, angle3, side1, side2, side3, unknown) #возвращает вычисленное значение неизвестной стороны или угла.


print("Результат: " + str(result)) #Выводим результат
