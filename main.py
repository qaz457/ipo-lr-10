import collision
from collision import RectCorrectError, intersectionAreaMultiRect
rectangles = []
try:
    print("Введите координаты 4 прямоугольников")
    
    for i in range(4):
        print(f"\nПрямоугольник {i+1}:")
        left_down_x = float(input("  Введите x левого нижнего угла: "))
        left_down_y = float(input("  Введите y левого нижнего угла: "))
        right_up_x = float(input("  Введите x правого верхнего угла: "))
        right_up_y = float(input("  Введите y правого верхнего угла: "))
        
        rectangles.append([(left_down_x, left_down_y), (right_up_x, right_up_y)])
    
    area = intersectionAreaMultiRect(rectangles)
    
    if area > 0:
        print("У всех прямоугольников есть общее пересечение!")
        print(f"Площадь пересечения всех прямоугольников: {area}")
    else:
        print(f"У прямоугольников нет общего пересечения.")
except ValueError:
    print("Вводить можно только числа")
except RectCorrectError as e:
    print(e)
    print(e)