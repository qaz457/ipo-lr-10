def isCorrectRect(rect):
    left_down = rect[0]
    right_up = rect[1]
    if left_down[0] < right_up[0] and left_down[1]<right_up[1]:
        return True
    else:
        return False
rect = []
try:
    
    left_down_x = float(input("Введите x левого нижнего угла"))
    left_down_y = float(input("Введите y левого нижнего угла"))
    rect.append((left_down_x, left_down_y ))
    right_up_x = float(input("Введите x правого верхнего угла"))
    right_up_y = float(input("Введите y правого верхнего угла"))
    rect.append((right_up_x, right_up_y ))
    if isCorrectRect(rect):
        print("Такой прямоугольник существует")
    else:
        print("Такого прямоугольника не существует")
except ValueError:
    print("Вводить можно только числа")