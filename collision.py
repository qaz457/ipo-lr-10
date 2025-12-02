class RectCorrectError (Exception):
    pass
def intersectionAreaRect(rect1,rect2):
    
    x1_left, y1_down = rect1[0]
    x1_right, y1_up = rect1[1]
    
    
    if x1_left< x1_right and y1_down<y1_up:
        pass
    else:
        raise RectCorrectError ("1 прямоугольник не существует")
 
    x2_left, y2_down = rect2[0]
    x2_right, y2_up = rect2[1]
    if x2_left< x2_right and y2_down<y2_up:
        pass
    else:
        raise RectCorrectError ("2 прямоугольник не существует")
    
    if (x1_right <= x2_left or  
        x2_right <= x1_left or 
        y1_up <= y2_down or  
        y2_up <= y1_down):  
        return 0
    
   
    else:
        intersect_left = max(x1_left, x2_left)
        intersect_right = min(x1_right, x2_right)
        intersect_bottom = max(y1_down, y2_down)
        intersect_top = min(y1_up, y2_up)

        width = intersect_right - intersect_left
        height = intersect_top - intersect_bottom
        
        area = width * height
        
        return area

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0
    
    if len(rectangles) == 1:
        rect = rectangles[0]
        x_left, y_down = rect[0]
        x_right, y_up = rect[1]
        return (x_right - x_left) * (y_up - y_down)
    
    for i, rect in enumerate(rectangles, 1):
        x_left, y_down = rect[0]
        x_right, y_up = rect[1]
        if x_left >= x_right or y_down >= y_up:
            raise RectCorrectError(f"{i} прямоугольник не существует")
    
    current_x_left, current_y_down = rectangles[0][0]
    current_x_right, current_y_up = rectangles[0][1]
    

    for i in range(1, len(rectangles)):
        x_left, y_down = rectangles[i][0]
        x_right, y_up = rectangles[i][1]
        
    
        new_x_left = max(current_x_left, x_left)
        new_x_right = min(current_x_right, x_right)
        new_y_down = max(current_y_down, y_down)
        new_y_up = min(current_y_up, y_up)

        if new_x_left >= new_x_right or new_y_down >= new_y_up:
            return 0  
        
        current_x_left, current_y_down = new_x_left, new_y_down
        current_x_right, current_y_up = new_x_right, new_y_up
    
    width = current_x_right - current_x_left
    height = current_y_up - current_y_down
    return width * height

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
    
    
