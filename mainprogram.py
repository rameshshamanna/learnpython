# if the functions is in same project and same folder, we can use import
# import functions as f

# if the functions is in different folder and same project, we can use import as
# import module.functions as f

# if the functions is in different folder and project, we can use import as

import sys
sys.path.append("C:\\Users\\shama\\Desktop\\Ramesh\\Personnel")
import functions as f

area = f.calculate_triangle_area(20, 10)
area1 = f.calculate_square_area(7)

print("area of trainagle is :", area)
print("area of square is ", area1)
