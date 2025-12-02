class ValueError (Exception):
    pass
def isCorrectRect(rect1,rect2):
    
    x1_left, y1_down = rect1[0]
    x1_right, y1_up = rect1[1]
    
    
    if x1_left< x1_right and y1_down<y1_up:
        pass
    else:
        raise ValueError ("1 прямоугольник не существует")
 
    x2_left, y2_down = rect2[0]
    x2_right, y2_up = rect2[1]
    if x2_left< x2_right and y2_down<y2_up:
        pass
    else:
        raise ValueError ("2 прямоугольник не существует")
    
    if (x1_right < x2_left or  
        x2_right < x1_left or 
        y1_up < y2_down or  
        y2_up < y1_down):  
        return 0
    
   
    else:
        
rect_1 = []
rect_2 = []

try:
    print("Коордианты первого прямоугольника")
    left_down_x = float(input("Введите x левого нижнего угла"))
    left_down_y = float(input("Введите y левого нижнего угла"))
    rect_1.append((left_down_x, left_down_y ))
    right_up_x = float(input("Введите x правого верхнего угла"))
    right_up_y = float(input("Введите y правого верхнего угла"))
    rect_1.append((right_up_x, right_up_y ))

    
    print("Коордианты второго прямоугольника")
    left_down_x = float(input("Введите x левого нижнего угла"))
    left_down_y = float(input("Введите y левого нижнего угла"))
    rect_2.append((left_down_x, left_down_y ))
    right_up_x = float(input("Введите x правого верхнего угла"))
    right_up_y = float(input("Введите y правого верхнего угла"))
    rect_2.append((right_up_x, right_up_y ))
    
    
    if isCorrectRect(rect_1, rect_2):
        print("Прямоугольники пересекаются")
    else:
        print("Прямоугольники не пересекаются")
except ValueError:
    print("Вводить можно только числа")
except ValueError as e:
    print(e)
    
    
