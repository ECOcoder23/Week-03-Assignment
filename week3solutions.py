#Draw Diamond Shape
def draw_top_portion(height):
    sum = 0 
    fill_order_list = list(range(1, height + 2, 1))
    for i in range(len(fill_order_list)):
        if (i % 2) == 1 and i < height + 2: 
           fill_line = "#" * (sum + i)
           print(fill_line.center(height))

def draw_bottom_portion(height):
    fill_order_list = list(range(0, height + 2, 1))
    for i in range(len(fill_order_list)):
        if (i % 2) == 1 and i > 0:
            fill_line = "#" * ((height + 1) - i)
            print(fill_line.center(height))

def draw_diamond(height):
    draw_top_portion(height)
    draw_bottom_portion(height) 

draw_diamond(13)

#Draw Right Triangle
def draw_right_triangle(height):
    sum = 0 
    fill_order_list = list(range(1, height + 1 , 1))
    for i in range(len(fill_order_list)):
        if i <= height: 
            print("#" * (sum + i))

draw_right_triangle(13)

#Compound Interest
def compound_interest(years: int, principal:int, percentage:int) -> float: 
   for year in range(years): 
     principal = ((1 + (percentage/100)) * principal)
   return principal 
print(compound_interest(5, 1000, 5))

#Hollow Square

def draw_square_ends(height, thickness): 
    char_fill_order = list(range(1, height + 1, 1))
    for i in range(len(char_fill_order)):
        if i <= thickness - 1:
            print("#" * height)

def draw_square_middle(height, thickness):
    char_fill_order = list(range(1, height, 1))
    for i in range(len(char_fill_order)):
        if height % 2 == 0:
            empty_space = ((height//2) - 2)
            if i <= empty_space:
                print("#" * thickness, " " * empty_space, "#" * thickness)
        else:
            empty_space = ((height//2) - 1)
            if i <= empty_space:
                print ("#" * thickness, " " * empty_space, "#" * thickness)

def draw_hollow_square(height, thickness):
    draw_square_ends(height, thickness)
    draw_square_middle(height, thickness)
    draw_square_ends(height, thickness)

draw_hollow_square(13, 3)