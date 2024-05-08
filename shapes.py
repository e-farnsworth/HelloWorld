# This will help you calculate the shapes areas.

def main():
    triangle_area = calculate_triangle(4,7)
    print(f'the area of the triangle is {triangle_area}')

def calculate_triangle(base, height):
    area = base * height / 2
    return area

main()
